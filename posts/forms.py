from django import forms
import django_filters
from .models import Post 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']


class PostFilterForm(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'body': ['icontains'],
            'created_at': ['gt', 'lt'],
        }
