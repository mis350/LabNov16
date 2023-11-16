from django.contrib import admin

# Register your models here.

from .models import Person, Car

class CarInLine(admin.TabularInline):
  model=Car

class PersonAdmin(admin.ModelAdmin):
  list_display=("driver_id", "name", "address")
  search_fields = ("name", "model")
  inlines = (CarInLine,)

class CarAdmin(admin.ModelAdmin):
  list_display=("license", "model", "year", "person")
  search_fields = ("name", "model")

admin.site.register(Person, PersonAdmin)
admin.site.register(Car, CarAdmin)