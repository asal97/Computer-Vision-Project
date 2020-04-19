from django.shortcuts import render
from .forms import PlateRegisterForm, VehicleRegisterForm


def register(request):
    plate_form = PlateRegisterForm(request.POST or None)
    vehicle_form = VehicleRegisterForm(request.POST or None)

    if request.method == 'POST':
        if request.POST.get('form_name') == 'plate_register':
            plate_form.save()
        elif request.POST.get('form_name') == 'vehicle_register':
            vehicle_form.save()

    context = {
        'plate_form': PlateRegisterForm(),
        'vehicle_form': VehicleRegisterForm()
    }

    return render(request, 'form.html', context)
