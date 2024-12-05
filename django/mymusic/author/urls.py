from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>/', views.author_detail, name='author_detail'),  # Используем имя автора в URL
]