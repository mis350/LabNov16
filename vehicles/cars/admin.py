from django.contrib import admin

# Register your models here.

from .models import Person, Car

class CarInLine(admin.TabularInline):
  model=Car

class PersonAdmin(admin.ModelAdmin):
  list_display=("driver_id", "name", "address")
  inlines = (CarInLine,)
  search_fields = ["name",]

class CarAdmin(admin.ModelAdmin):
  list_display=("license", "model", "year", "person")
  search_fields = ["model",]

admin.site.register(Person, PersonAdmin)
admin.site.register(Car, CarAdmin)