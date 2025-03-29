from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('post/<int:post_id>/', views.detail, name='detail'),  # Детальная страница поста
    path('category/<slug:category_slug>/', views.category, name='category'),  # Страница категории
]