from django.db import models
from datetime import datetime

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    due_date = models.DateTimeField()
    status = models.CharField(default="pending", max_length=10)

    def __str__(self):
        return self.title


