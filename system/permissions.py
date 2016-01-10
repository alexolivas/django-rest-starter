from rest_framework import permissions


class ManageUsersPermission(permissions.BasePermission):
    message = 'You do not have permission to manage users.'

    def has_permission(self, request, view):
        if request.user.is_superuser:
            # Admin users can see everything
            return True
        else:
            has_permission = False
            for group in request.user.groups.all():
                if str(group.name).lower() == 'warehouse employees':
                    has_permission = True
                    break
            return has_permission
