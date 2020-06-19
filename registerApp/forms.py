from django import forms
from django.forms import ModelForm
from .models import Plate, Vehicle, Owner, \
    ALPHA_CHOICES, PLATE_CHOICES
from django.core.validators import MaxValueValidator, MinValueValidator

OWNER_CHOICES = (
    ("new_owner", "ثبت مالک جدید"),
    ("old_owner", "از مالکین ثبت شده در سیستم"),)


class RegisterForm(forms.Form):
    owner_select = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=OWNER_CHOICES)

    owner_firstname = forms.CharField(max_length=20, required=False)
    owner_lastname = forms.CharField(max_length=30, required=False)
    owner_nationalcode = forms.CharField(max_length=10, required=True)
    owner_phone = forms.CharField(max_length=11, required=False)
    owner_description = forms.CharField(widget=forms.Textarea, required=False)
    owner_picture = forms.ImageField(required=False)

    plate_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=PLATE_CHOICES)
    plate_firstnum = forms.IntegerField(required=True)
    plate_secondnum = forms.IntegerField(required=True)
    plate_citynum = forms.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(10)], required=False)
    plate_alpha = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=ALPHA_CHOICES,
                                    required=False)

    vehicle_color = forms.CharField(max_length=10, required=True)
    vehicle_type = forms.CharField(max_length=20, required=True)
    vehicle_picture = forms.ImageField(required=False)
