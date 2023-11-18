from django.shortcuts import render , get_object_or_404
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


def List_BMW_Cars(request):
  context = {}
  all_cars = Car.objects.filter(model = "BMW")
  context['allc'] = all_cars
  return render (request, 'read_cars.html', context)

def List_cars_above_2000(request):
  data = {}


  all_cars = Car.objects.filter(year__gte = 2000)
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)

def Car_1990_2000(request):
  data = {}


  all_cars = Car.objects.filter(year__range=["1990", "2000"])
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)


def Cars_Owned_by_Mohammad_Jamal(request):
  data = {}


  person_record = Person.objects.get(name = 'Ali')
  all_cars = person_record.car_set.all()
  data['person'] = person_record
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)

def license(request , license_id):
  
  all_cars = get_object_or_404(Car, license_id=KWT123)

  data = {'car': all_cars}

  

  

  return render(request, "read_cars.html" , context=data)