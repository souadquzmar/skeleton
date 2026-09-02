from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field="username", read_only=True)
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
