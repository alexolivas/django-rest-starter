def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': 'add user details serializer here'
    }


