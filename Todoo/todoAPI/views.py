from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


@api_view(['GET'])
def finish_task(request, id):
    task = Task.objects.get(pk=id)
    data = {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "due_date": task.due_date,
        "status": "finished"
    }
    serializer = TaskSerializer(task, data=data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(data=serializer.data, status=200)

@api_view(['GET'])
def filter_tasks(request, type):
    tasks = Task.objects.all()
    result = []
    if type == 'finished':
        for task in tasks:
            if task.status == 'finished':
                result.append(task)
    elif type == 'unfinished':
        for task in tasks:
            if task.status != 'finished':
                result.append(task)
    else:
        return JsonResponse({"error": "unvalid paramter"}, status=400)
    serializer = TaskSerializer(result, many=True)
    return JsonResponse(serializer.data, safe=False, status=200)
