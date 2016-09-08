from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
# from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.throttling import AnonRateThrottle
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from serializers import TokenSerializer, LoginSerializer
# from social.apps.django_app import load_strategy
# from social.apps.django_app.utils import load_backend
# from social.backends.oauth import BaseOAuth1, BaseOAuth2
# from social.exceptions import A   uthAlreadyAssociated
# from permissions import IsAuthenticatedOrCreate
# from serializers import SignUpSerializer


# class SignUp(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = SignUpSerializer
#     permission_classes = (IsAuthenticatedOrCreate,)
#
#
# class SocialSignUp(generics.CreateAPIView):
#     User = get_user_model()
#
#     queryset = User.objects.all()
#     serializer_class = SocialSignUpSerializer
#     # This permission is nothing special, see part 2 of this series to see its entirety
#     permission_classes = (IsAuthenticatedOrCreate,)
#
#     def create(self, request, *args, **kwargs):
#         """
#         Override `create` instead of `perform_create` to access request
#         request is necessary for `load_strategy`
#         """
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         provider = request.data['provider']
#
#         # If this request was made with an authenticated user, try to associate this social
#         # account with it
#         authed_user = request.user if not request.user.is_anonymous() else None
#
#         # `strategy` is a python-social-auth concept referencing the Python framework to
#         # be used (Django, Flask, etc.). By passing `request` to `load_strategy`, PSA
#         # knows to use the Django strategy
#         strategy = load_strategy(request)
#         # Now we get the backend that corresponds to our user's social auth provider
#         # e.g., Facebook, Twitter, etc.
#         backend = load_backend(strategy=strategy, name=provider, redirect_uri=None)
#
#         if isinstance(backend, BaseOAuth1):
#             # Twitter, for example, uses OAuth1 and requires that you also pass
#             # an `oauth_token_secret` with your authentication request
#             token = {
#                 'oauth_token': request.data['access_token'],
#                 'oauth_token_secret': request.data['access_token_secret'],
#             }
#         elif isinstance(backend, BaseOAuth2):
#             # We're using oauth's implicit grant type (usually used for web and mobile
#             # applications), so all we have to pass here is an access_token
#             token = request.data['access_token']
#
#         try:
#             # if `authed_user` is None, python-social-auth will make a new user,
#             # else this social account will be associated with the user you pass in
#             user = backend.do_auth(token, user=authed_user)
#         except AuthAlreadyAssociated:
#             # You can't associate a social account with more than user
#             return Response({"errors": "That social media account is already in use"},
#                             status=status.HTTP_400_BAD_REQUEST)
#
#         if user and user.is_active:
#             # if the access token was set to an empty string, then save the access token
#             # from the request
#             auth_created = user.social_auth.get(provider=provider)
#             if not auth_created.extra_data['access_token']:
#                 # Facebook for example will return the access_token in its response to you.
#                 # This access_token is then saved for your future use. However, others
#                 # e.g., Instagram do not respond with the access_token that you just
#                 # provided. We save it here so it can be used to make subsequent calls.
#                 auth_created.extra_data['access_token'] = token
#                 auth_created.save()
#
#             # Set instance since we are not calling `serializer.save()`
#             serializer.instance = user
#             headers = self.get_success_headers(serializer.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED,
#                             headers=headers)
#         else:
#             return Response({"errors": "Error with social authentication"},
#                             status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    """
    This endpoint generates a new token effectively granting a user access to the system

    * This API doesn't require authentication or permission
    """
    authentication_classes = ()
    permission_classes = (AllowAny,)
    throttle_classes = (AnonRateThrottle,)
    serializer_class = LoginSerializer

    def get_serializer_class(self):
        return self.serializer_class

    def post(self, request, format=None):
        if 'email' in request.POST and 'password' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')

            # We are using email as the username, authenticate with that instead of the username
            user = self.authenticate_by_email(email, password)
            if user is not None:
                if user.is_active:
                    # Get the user's existing token, if one doesn't exist generate a new one
                    user_token, created = Token.objects.get_or_create(user=user)

                    results = dict()

                    # Serialize the user and token so the data can be passed back to the caller
                    token_serializer = TokenSerializer(user_token)
                    results['token'] = token_serializer.data['key']
                    results['user'] = token_serializer.data['user']

                    return Response(results, status=status.HTTP_200_OK)
                else:
                    # This user is not active in the system
                    message = {'message': 'This account is inactive.'}
                    return Response(message, status=status.HTTP_401_UNAUTHORIZED)
            else:
                # Incorrect username/password combination
                message = {'message': 'Invalid credentials.'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

        message = {'message': 'Missing username and/or password.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def authenticate_by_email(email, password):
        # We are using an email as the username, so we can't use django's built in authentication,
        # Let's authenticate by grabbing the user by email and checking the password
        try:
            # Grab the user by email, once we have the user we will pass in the username
            # to django's built in authentication system
            user_details = User.objects.get(email=email)

            # Use django's built in authentication
            user = authenticate(username=user_details.username, password=password)

            if user is not None:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None


class Logout(APIView):
    """
    This endpoint revokes a user's token effectively logging them out of the system

    * Requires token authentication.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):

        if request.user and request.user.pk:
            # No need to check if token exists because the user would not be able to call
            # this endpoint if a token did in fact not exist
            user_token = Token.objects.get(user=request.user.pk)
            user_token.delete()
            message = {
                'message': 'Successfully logged out'
            }
            return Response(message, status=status.HTTP_200_OK)
        else:
            message = {
                'message': 'Unable to find user in the request'
            }
            return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
