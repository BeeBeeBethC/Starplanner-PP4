from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    title = models.CharField(max_length=200, unique=True)
    task = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES, default='low')
    description = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    
# this is a full string representation of the tasks
    def __str__(self):
        return (f"ID:{self.task}: Added By: {self.user}, Priority: {self.priority}, Task Description: {self.description}")