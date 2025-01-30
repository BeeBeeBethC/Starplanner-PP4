from django.db import models

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    task = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100, unique=True)
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES, default='medium')
    description = models.TextField(max_length=500)
    
# this is a full string representation of the tasks
    def __str__(self):
        return (f"ID:{self.task}: Added By: {self.user}, Priority: {self.priority}, Task Description: {self.description}")
