from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path('my/', views.posts_user, name='my_list'),
    path('', views.posts_list, name='list'),
    path('new/', views.post_new, name='new'),
    path('<int:id>/edit/', views.post_edit, name='edit'),
    path('<int:id>/delete/', views.post_delete, name='delete'),
    path('<int:id>/', views.post_page, name='page'),
]
