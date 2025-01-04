from django import forms
from .models import Task
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assignee', 'priority', 'completed']


class AssigneeForm(forms.Form):
    assignee = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Select Assignee")