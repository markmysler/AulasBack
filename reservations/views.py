from rest_framework import viewsets

from calendar_day.models import CalendarBlock
from calendar_day.serializers import CalendarBlockSerializer
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework.views import APIView
from rest_framework import status,permissions
from rest_framework.response import Response
from django.http import Http404
from datetime import datetime
from django.db.models import Q
from rest_framework.decorators import action

class ReservationViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
    @action(detail=True, methods=['post'])
    def partial_delete(self, request, pk=None):
        reservation = self.get_object()
        date_num = int(request.data.get('date_num'))
        month = int(request.data.get('month'))
        calendar_blocks = CalendarBlock.objects.filter(date_num = date_num, month = month, reservation_id = reservation.id)
        len_calendar_blocks = len(calendar_blocks)
        calendar_blocks.delete()
        print(request.data)
        return Response({'message': f'Successfully deleted {len_calendar_blocks} calendar block(s)'}, status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        
        current_month= datetime.now().month
        current_day= datetime.now().day
        
        # Filter CalendarBlock objects where month is the same and date_num is equal or greater than current day
        calendar_blocks = CalendarBlock.objects.filter(
            (Q(month=current_month, date_num__gte=current_day) | Q(month__gt=current_month)),
            reservation_id=instance.id,
        )
        
        # Serialize the CalendarBlock objects
        calendar_block_serializer = CalendarBlockSerializer(calendar_blocks, many=True)
        
        # Add the serialized CalendarBlock objects to the response
        response = Response({
            'reservation': serializer.data,
            'calendar_blocks': calendar_block_serializer.data,
        })
        
        return response

    
class MyReservations(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self, request, pk):
        # get all Reservation objects with a user_id equal to pk
        reservations = Reservation.objects.filter(user_id=pk)
        if len(reservations) != 0:
            serializer = ReservationSerializer(reservations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response([], status=status.HTTP_200_OK)
class AulaReservations(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self, request, pk):
        reservations = Reservation.objects.filter(aula_id=pk)
        if len(reservations) != 0:
            serializer = ReservationSerializer(reservations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response([], status=status.HTTP_200_OK)