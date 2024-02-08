from rest_framework import serializers
from .models import CalendarBlock

class CalendarBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model=CalendarBlock
        fields=(
            'aula_id',
            'month',
            'date_num',
            'week_day',
            'timeblock',
            'reservation_id',
        )