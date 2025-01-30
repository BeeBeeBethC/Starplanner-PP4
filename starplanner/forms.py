from django import forms
from django.contrib.auth.models import User
from .models import Task

class TaskForm(forms.ModelForm):
    
    
    class Meta:
        model = Task
        fields= '__all__'
        labels = {
            'task': 'Task',
            'user': 'User',
            'priority': 'Priority',
            'description': 'Description',
        }
        widgets = {
            'task':forms.NumberInput(attrs={'placeholder':'e.g 1', 'class':'form-control'}),
            'user':forms.TextInput(attrs={'placeholder':'e.g Jbloggs', 'class':'form-control'}),
            'priority':forms.RadioSelect(attrs={'choices': 'PRIORITY_CHOICES', 'class':'form-control'}),
            'description':forms.Textarea(attrs={'placeholder':'describe your task here', 'class':'form-control'}),
        }