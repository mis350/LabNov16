from django.urls import path
from .import views 



urlpatterns = [
    path('', views.greeting),
    path('readc/', views.read_cars, name="read_cars"),
    path('bmw/', views.list_bmw, name="list_bmw"),
    path('2000/', views.list_gte, name="list_2000"),
    path('between/', views.list_bet, name="list_between"),
    path('name/', views.list_name, name="list_name"),
    path('search-car/<str:license_id>/', views.search_by_license),
]