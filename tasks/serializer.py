from rest_framework import serializers
from .models import my_task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = my_task
        fields = '__all__'
