from rest_framework import serializers
from .models import TasksModel

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksModel
        fields = ['id', 'owner', 'title', 'description', 'status', 'created_at', 'updated_at']
