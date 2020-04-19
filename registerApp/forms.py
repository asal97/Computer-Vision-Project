from django import forms
from django.forms import ModelForm
from .models import Plate, Vehicle, Owner


class PlateRegisterForm(ModelForm):
    class Meta:
        model = Plate
        fields = ['plate_type', 'firstNum', 'alpha', 'secondNum', 'cityNum']


class VehicleRegisterForm(ModelForm):
    plate = forms.ModelChoiceField(Plate.objects.all())
    owner = forms.ModelChoiceField(Owner.objects.all())

    class Meta:
        model = Vehicle
        fields = ['plate', 'type', 'color', 'owner', 'img']
        widgets = {
            'plate': forms.Select(attrs={'class': 'form-control'}) #TODO: ADD CLASS HERE :/
        }
