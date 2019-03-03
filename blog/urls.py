from django.urls import path
from . import views

name = 'blog'

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]
