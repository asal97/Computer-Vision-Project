from django import forms
from django.forms import ModelForm
from .models import Plate, Vehicle, Owner


class PlateRegisterForm(ModelForm):
    class Meta:
        model = Plate
        fields = ['plate_type', 'firstNum', 'alpha', 'secondNum', 'cityNum']


class VehicleRegisterForm(ModelForm):
    # plate = forms.ModelChoiceField(Plate.objects.all())
    # owner = forms.ModelChoiceField(Owner.objects.all())

    class Meta:
        model = Vehicle
        fields = ['plate', 'type', 'color', 'owner', 'img']
        widgets = {
            'plate': forms.Select(choices=Plate.objects.all(), attrs={'class': 'form-control'}),
            'owner': forms.Select(choices=Owner.objects.all(), attrs={'class': 'form-control'}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': False}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'})
        }
