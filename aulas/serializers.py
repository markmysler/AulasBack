from rest_framework import serializers
from .models import Aula

class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aula
        fields=(
            'id',
            'name',
            'max_capacity',
            'has_negatoscope',
            'has_screen'
        )