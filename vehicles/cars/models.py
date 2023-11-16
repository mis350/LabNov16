from django.db import models

# Create your models here.

class Person(models.Model):
  driver_id = models.CharField("Driver ID", max_length=12, null=False, unique=True)
  name = models.CharField("Driver Name", max_length=50, null=False)
  address = models.CharField("Driver Address", max_length=100, null=False)

  def __str__(self):
    return f"{self.name}"

class Car(models.Model):
  CarChoice=(
    ("BMW", "BMW MOTORS"),
    ("FORD", "FORD MOTORS"),
    ("GM", "GENERAL MOTORS"),
    ("AUDI", "AUDI MOTORS"),
  )

  license = models.CharField("Car License", max_length=10, null=False, unique=True)
  model = models.CharField("Car Model", max_length=30, null=False, choices=CarChoice)
  year = models.IntegerField("Car Make Year", null=False)
  person = models.ForeignKey(Person, on_delete=models.CASCADE)

  def __str__(self):
    return f"Model: {self.model} - Year: {self.year} - License: {self.license}"