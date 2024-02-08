from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework import status,permissions
from rest_framework.response import Response

from allowed_emails.models import AllowedEmail



class CustomUserViewSet(DjoserUserViewSet):
    permission_classes=[permissions.AllowAny]
    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        try:
            isAllowed = AllowedEmail.objects.get(email=email)
            isAllowed.delete()
            return super().create(request, *args, **kwargs)
        except AllowedEmail.DoesNotExist:
            return Response({'error': 'Email not allowed'})
