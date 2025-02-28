from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField()
    bio = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    