from django.urls import path
from . import views

urlpatterns = [
    path('', views.greeting),
    path('readc/', views.read_cars),
    path('search_car_by_license/<str:license_id>/', views.search_by_license, name='search_by_license'),
]