from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    task_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, unique=True)
    priority = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    comment = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name