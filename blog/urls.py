from django.urls import path
from . import views


# Create a path object with an empty path, the home() function in views.py
# And named 'blog-home'
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]