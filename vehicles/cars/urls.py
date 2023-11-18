from django.urls import path
from . import views

urlpatterns = [
    path('', views.greeting),
    path('readc/', views.read_cars),
    path('readb/', views.List_BMW_Cars),
    path('reada/', views.List_cars_above_2000),
    path('readk/', views.Car_1990_2000),
    path('readf/', views.Cars_Owned_by_Mohammad_Jamal),
    path('search/<slug:license_id>/', views.license),
    
]
