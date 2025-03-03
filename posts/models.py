from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.title)}_{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)
