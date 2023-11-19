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

def list_bmw_cars(request):
  data = {}
  all_cars = Car.objects.filter(model="BMW")
  data["allc"] =all_cars
  return render(request, 'read_cars.html', context=data)

def list_2000_cars(request):
  data = {}
  all_cars = Car.objects.filter(year__gte=2000)
  data["allc"] =all_cars
  return render(request, 'read_cars.html', context=data)

def cars_1990_2000(request):
  data={}
  all_cars = Car.objects.filter(year__range=["1990", "2000"])
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)

def list_cars_shahad(request):
  data={}
  Person_record = Person.objects.get(name = "shahad")
  all_cars = Person_record.car.set.all()
  data['person'] = Person_record
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)


def search_by_license(request, license_id):
  data={}
  p = Car.objects.get(license = license_id)
  data['post'] = p
  return render(request, "search_car.html", context=data)

