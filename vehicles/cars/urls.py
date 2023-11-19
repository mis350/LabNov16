from django.urls import path
from . import views

urlpatterns = [
    path('', views.greeting, name= 'greeting'),
    path('readc/', views.read_cars , name = 'all cars'),
    path('list_bmw_cars/', views.list_bmw_cars, name = 'bmws'),
    path('list_2000_cars/', views.list_2000_cars, name = '2000 cars'),
    path('between/', views.cars_1990_2000, name="list_between"),
    path('name/', views.list_cars_shahad, name="list_name"),
    path('search_license/<str:license_id>/', views.search_by_license, name='search_by_license'),
]
