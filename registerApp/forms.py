from django.forms import ModelForm
from .models import Plate


class PlateRegisterForm(ModelForm):
    class Meta:
        model = Plate
        fields = ['plate_type', 'firstNum', 'alpha', 'secondNum', 'cityNum']
