from django.shortcuts import render
from rest_framework.views import APIView
from .models import Aula
from .serializers import AulaSerializer
from rest_framework.response import Response
# Create your views here.

class AulasList(APIView):
    def get(self, request, format=None):
        aulas = Aula.objects.all()
        serializer = AulaSerializer(aulas,many=True)
        return Response(serializer.data)
