from rest_framework.permissions import BasePermission
from rest_framework.exceptions import NotAcceptable, PermissionDenied


USER_GROUPS = {
    'superuser': [
        '*'
    ],
    'user': [
        'can_change_password'
    ]
}


class UserPermission(BasePermission):
    def __init__(self, permission):
        super(UserPermission, self).__init__()
        self.permission = permission

    def has_permission(self, request, view):
        if not request.user.groups:
            raise NotAcceptable(detail='group has to be in the user object')
        if '*' in USER_GROUPS.get(request.user.groups[0]):
            return True
        if not USER_GROUPS.get(request.user.groups[0]) or self.permission not in USER_GROUPS.get(
            request.user.groups[0]
        ):
            raise PermissionDenied(detail='user has no permission to perform this task')
        return True
