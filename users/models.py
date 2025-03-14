from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(null=True)
    bio = models.TextField(max_length=1000)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
