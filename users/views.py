from django.http import Http404
from rest_framework.generics import RetrieveAPIView
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework import permissions


class UserDetail(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    
    def get_object(self):
            token_key = self.kwargs.get("token")
            try:
                token = Token.objects.get(key=token_key)
                return token.user
            except Token.DoesNotExist:
                raise Http404("No User matches the given token.")
            
