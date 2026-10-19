from django.urls import path
from . import views

urlpatterns = [
    path('containers/', views.containers, name='containers'),
]