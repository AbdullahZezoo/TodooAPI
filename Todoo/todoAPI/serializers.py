from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'due_date', 'status')


