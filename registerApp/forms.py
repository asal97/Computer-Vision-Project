from django import forms
from django.forms import ModelForm
from .models import Plate, Vehicle, Owner, \
    ALPHA_CHOICES, PLATE_CHOICES
from django.core.validators import MaxValueValidator, MinValueValidator


class RegisterForm(forms.Form):
    owner_firstname = forms.CharField(max_length=20, required=True)
    owner_lastname = forms.CharField(max_length=30, required=True)
    owner_nationalcode = forms.CharField(max_length=10, required=True)
    owner_phone = forms.CharField(max_length=11)
    owner_description = forms.CharField(widget=forms.Textarea)
    owner_picture = forms.ImageField()

    plate_type = forms.ChoiceField(choices=PLATE_CHOICES)
    plate_firstnum = forms.IntegerField()
    plate_secondnum = forms.IntegerField()
    plate_citynum = forms.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(10)])
    plate_alpha = forms.ChoiceField(choices=ALPHA_CHOICES)

    vehicle_color = forms.CharField(max_length=10)
    vehicle_type = forms.CharField(max_length=20)
    vehicle_picture = forms.ImageField()


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
