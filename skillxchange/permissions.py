from rest_framework.permissions import BasePermission, SAFE_METHODS

class CustomPermissions(BasePermission):
    # def has_permission(self, request, view):
    #     if request.method in SAFE_METHODS:
    #         return request.user and request.user.is_authenticated
        
    #     elif request.method == "POST":
    #         return request.user and request.user.is_authenticated and request.user.is_manager
        
    #     else:
    #         return request.user and request.user.is_authenticated and request.user.is_admin
        
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            if request.user and request.user.is_authenticated:
                return True
        
        elif request.method == "POST":
           return request.user.is_manager or request.user.is_admin
 
        elif request.method in ['PUT','DELETE']:
            return obj.tutor == request.user or request.user.is_admin 
        
        else:
            return request.user and request.user.is_admin