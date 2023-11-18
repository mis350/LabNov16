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

def list_bmw(request):
  data={}
  all_cars = Car.objects.filter(model="bmw")
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)

def list_gte(request):
  data={}
  all_cars = Car.objects.filter(year__gte="200")
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)

def list_between(request):
  data={}
  all_cars = Car.objects.filter(year__range=["1999","2000"])
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)


def list_by_name(request):
  data={}

  all_cars = p.car_set.all()
  p = Person.objects.get(name='Mohammad Jamal')
  data['person'] = p
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)

def search_by_license(request, license_id):
  p = Car.objects.get(license= license_id)
  data={}
  #data['allc'] = p
  data = {'allc': p}
  return render(request, "car_search.html", data)