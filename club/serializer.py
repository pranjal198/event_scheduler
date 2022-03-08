from rest_framework import serializers
from .models import club


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = club
        fields = '__all__'