from django.db import models
from django.contrib.auth.models import User

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

class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    email = models.EmailField(default='example@example.com')
    phone = models.CharField(max_length=11, default='01234567891')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"profile belonging to {self.name.username}"