from rest_framework import permissions
from .models import *

class AnswerPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['create', 'update', 'destroy']:
            return request.user.is_staff
        else:
            return False
        
    def has_object_permission(self, request, view, obj):
        if not request.user.is_staff:
            return False
        if view.action in ['create', 'update', 'destroy']:
            return obj == request.user.is_staff
        else:
            return False