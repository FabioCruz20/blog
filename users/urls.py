from django.urls import path, include
import django.contrib.auth.views as auth_views
from . import views

# see https://docs.djangoproject.com/en/5.1/topics/auth/default/#using-the-views

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path(
        'logout/', 
        auth_views.LogoutView.as_view(
            template_name='registration/logged_out_1.html'
        ), 
        name='logout'
    ),
    path(
        'password_reset/', 
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset.html'
        ), 
        name='password_reset'
    ),
    path(
        'password_reset/done/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done_1.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm_1.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_change_done_1.html'
        ),
        name='password_reset_complete'
    ),
]
