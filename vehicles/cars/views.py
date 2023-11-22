from django.shortcuts import render, redirect
from .forms import SearchForm
from .models import Person, Car

# Create your views here.
def greeting(request):
  data={}
  if request.method == 'POST':
    form = SearchForm(request.POST)
    if form.is_valid():
      search_query = form.cleaned_data['search_query']
      return redirect('search', search_query=search_query)
    else:
        form = SearchForm()
        return render(request, 'greeting.html', {'form': form})

  return render(request, "greeting.html", context=data)

def read_cars(request):
  data={}
  all_cars = Car.objects.all()
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)

def list_bmw_cars(request):
  data={}
  all_cars = Car.objects.filter(model="BMW")
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)

def list_2000_cars(request):
  data={}
  all_cars = Car.objects.filter(year__gte=2000)
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)

def list_1990_2000(request):
  data={}
  all_cars = Car.objects.filter(year__range=["1990", "2000"])
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)

def list_cars_Mohammad_Jamal(request):
  data={}
  person_record = Person.objects.get(name = "Mohammad Jamal")
  all_cars = person_record.car_set.all()
  data['person'] = person_record
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)

def search_car(request, search_query):

    results = Car.objects.filter(license__icontains=search_query)
    data={'results': results, 'search_query': search_query}
    car_record = Car.objects.get(license = search_query)
    data['allc'] = car_record

    return render(request, 'search_car.html', context = data)