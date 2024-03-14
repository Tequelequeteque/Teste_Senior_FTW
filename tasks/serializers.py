from .models import Tasks
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    priority = serializers.CharField(source='get_priority_display')
    class Meta:
        model = Tasks
        fields = '__all__'