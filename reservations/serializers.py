from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields=(
            'id', 'aula_id', 'user_id', 'user_category', 'start_date', 'end_date', 'frequency', 'times'
        )