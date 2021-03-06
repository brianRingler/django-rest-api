from rest_framework import permissions 

class UpdateOwnProfile(permissions.BasePermission):
    '''Allow user to edit their own profile'''

    def has_object_permission(self, request, view, obj):
        '''Check user is trying to edit their own profile'''

        # if request method is Get, Options or Head it is in SAFE_METHODS and return True
        if request.method in permissions.SAFE_METHODS:
            return True
        # Not safe method get the users id they are NOT authenticated
        return obj.id == request.user.id