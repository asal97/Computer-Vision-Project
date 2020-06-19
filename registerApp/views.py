from django.shortcuts import render
from .forms import RegisterForm
from .models import Owner, Plate, Vehicle
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

import enum


def register(request):
    # register_form = RegisterForm(request.POST or None)
    status = 0
    if request.method == 'POST':
        if request.POST.get('form-key') == 'ثبت-مشخصات':
            # status = 1
            register_form = RegisterForm(request.POST, request.FILES)
            if register_form.is_valid():
                try:
                    if register_form.cleaned_data['owner_select'] == 'old_owner':
                        owner_obj = Owner.objects.get(nationalCode=register_form.cleaned_data['owner_nationalcode'])

                    else:
                        owner_obj = Owner(first_name=register_form.cleaned_data['owner_firstname'] or "-",
                                          family_name=register_form.cleaned_data['owner_lastname'] or "-",
                                          nationalCode=register_form.cleaned_data['owner_nationalcode'],
                                          phone=register_form.cleaned_data['owner_phone'] or "-",
                                          img=register_form.cleaned_data['owner_picture'],
                                          description=register_form.cleaned_data['owner_description'])
                        owner_obj.save()
                except Owner.DoesNotExist:
                    status = -1
                except IntegrityError:
                    status = -1
                else:
                    try:
                        if register_form.cleaned_data['plate_type'] == '1':
                            plate_obj = Plate(plate_type='1',
                                              firstNum=register_form.cleaned_data['plate_firstnum'],
                                              secondNum=register_form.cleaned_data['plate_secondnum'],
                                              cityNum=register_form.cleaned_data['plate_citynum'],
                                              alpha=register_form.cleaned_data['plate_alpha'])
                        else:
                            plate_obj = Plate(plate_type='2',
                                              firstNum=register_form.cleaned_data['plate_firstnum'],
                                              secondNum=register_form.cleaned_data['plate_secondnum'])

                        vehicle_obj = Vehicle(owner=owner_obj,
                                              plate=plate_obj,
                                              color=register_form.cleaned_data['vehicle_color'],
                                              type=register_form.cleaned_data['vehicle_type'],
                                              img=register_form.cleaned_data['vehicle_picture'])
                        plate_obj.save()
                        vehicle_obj.save()
                    except IntegrityError:
                        status = -1
                    else:
                        status = 1
    context = {
        'register_form': RegisterForm(),
        'status': status
    }

    return render(request, 'form.html', context)
