from django.urls import path, include
import django.contrib.auth.views as auth_views
from . import views

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', views.profile_view, name='profile'),
]
