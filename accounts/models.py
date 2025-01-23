from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# registering a new user
class register(models.Model):
    user_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=14)
    password_confirm = models.CharField(max_length=14)
    email_address = models.EmailField(unique=True)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['user_id']

    def __str__(self):
        return (f"Username: {self.user_id}, Email: {self.email_address}, First Name: {self.firstname}, Last Name: {self.lastname}")