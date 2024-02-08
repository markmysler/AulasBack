from calendar_day.serializers import CalendarBlockSerializer
from .models import Aula
from .serializers import AulaSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.utils import timezone
from calendar_day.models import CalendarBlock

# Create your views here.


class AulasViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        
        

        
        # Get the CalendarBlock objects for the current Aula
        calendar_blocks = CalendarBlock.objects.filter(
            aula_id=instance.id,
        )
        
        # Serialize the CalendarBlock objects
        calendar_block_serializer = CalendarBlockSerializer(calendar_blocks, many=True)
        
        # Add the serialized CalendarBlock objects to the response
        response = Response({
            'aula': serializer.data,
            'calendar_blocks': calendar_block_serializer.data,
        })
        
        return response

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)