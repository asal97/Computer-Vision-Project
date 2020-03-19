from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Plate(models.Model):
    firstNum = models.IntegerField(validators=[MaxValueValidator(99), MinValueValidator(1)])
    SecondNum = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(100)])
    cityNum = models.IntegerField(validators=[MaxValueValidator(99), MinValueValidator(10)])
    alphaCode = models.CharField(max_length=5)

    def __str__(self):
        return self.firstNum


class Car(models.Model):
    plate = models.OneToOneField(Plate, on_delete=models.CASCADE)
    color = models.CharField(max_length=10, blank=True)
    type = models.CharField(max_length=20)
    authorized = models.BooleanField(default=False)

    def __str__(self):
        return self.type


class Owner(models.Model):
    first_name = models.CharField(max_length=20)
    family_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11, blank=True)
    nationalCode = models.CharField(max_length=10)
    description = models.TextField(max_length=300)
    Car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
