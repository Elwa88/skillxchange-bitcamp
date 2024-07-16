from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import CustomUser
from django.shortcuts import get_object_or_404

class OtherPermissions(BasePermission):
    def has_permission(self, request, view):
        return True
        
class SkillsPermissions(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = get_object_or_404(CustomUser, pk=request.user.pk)
        if user.is_admin:
            return True
        if request.method in SAFE_METHODS:
            return True
        else:
            if request.method == "POST":
                return user.is_manager or user.is_admin
            if request.method in ['PUT','DELETE']:
                return obj.tutor == request.user
