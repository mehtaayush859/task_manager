# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    # assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    priority = models.CharField(max_length= 20, null=False, blank=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
