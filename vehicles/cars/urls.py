from django.urls import path
from . import views

urlpatterns = [
    path('', views.greeting, name='greeting'),
    path('readc/', views.read_cars, name='allcars'),
    path('list_bmw_cars/', views.list_bmw_cars, name='bmws'),
    path('list_2000_cars/', views.list_2000_cars),
    path('list_1990_2000/', views.list_1990_2000),
    path('list_cars_Mohammad_Jamal/', views.list_cars_Mohammad_Jamal),
    path('search_car/<str:search_query>', views.search_car, name='search'),
    
]