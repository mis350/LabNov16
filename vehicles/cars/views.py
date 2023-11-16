from django.shortcuts import render
from .models import Person, Car

# Create your views here.
def greeting(request):
  data={}
  return render(request, "greeting.html", context=data)

def read_cars(request):
  data={}
  all_cars = Car.objects.all()
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)