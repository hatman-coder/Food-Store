from rest_framework import  permissions
from django.http.response import JsonResponse

class AdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        try:
            admin_permission = bool(request.user and request.user.is_staff)
            return request.method == 'GET' or admin_permission
        except ObjectDoesNotExists:
            return JsonResponse({
                "detail": "Error ! You have no permission"
            })