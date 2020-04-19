from django.shortcuts import render
from .forms import PlateRegisterForm


def register(request):
    plate_form = PlateRegisterForm(request.POST or None)
    if request.method == 'POST':
        if request.POST.get('form_name') == 'plate_register':
            plate_form.save()

    context = {
        'plate_form': plate_form
    }

    return render(request, 'form.html', context)
