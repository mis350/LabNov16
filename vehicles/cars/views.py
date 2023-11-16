from django.shortcuts import render
from .models import Person, Car

# Create your views here.
def greeting(request):
  posts = Car.objects.all()
  data={}
  return render(request, "greeting.html", context=data)

def read_cars(request):
  data={}
  all_cars = Car.objects.all()
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)

def list_bmw(request):
  data={}
  all_cars = Car.objects.filter(model="BMW")
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)

def list_gte(request):
  data={}
  all_cars = Car.objects.filter(year__gte="2000")
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)


def list_bet(request):
  data={}
  all_cars = Car.objects.filter(year__range=["1990", "2000"])
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)


def list_name(request):
  person_record= Person.objects.get(name="Mohammad Jamal")
  all_cars = person_record.car_set.all()
  data={}
  data['person'] = person_record
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)


def search_by_license(request, license_id):
  p = Car.objects.get(license=license_id)
  data={}
  data['post'] = p
  return render(request, "search_car.html", data)