from django.urls import path
from . import views

urlpatterns = [
    path('', views.greeting),
    path('readc/', views.read_cars),
]