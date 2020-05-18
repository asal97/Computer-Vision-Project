import datetime

from django.shortcuts import render
from registerApp.models import Plate, Owner, Vehicle
from taradodApp.models import Taradod
import jdatetime


def index(request):
    return render(request, 'index.html', {})


def table(request):
    Owner_lists = Owner.objects.all()
    all_Vehicle_list = Vehicle.objects.all()
    Taradod_list = Taradod.objects.all()

    Vehicle_list = []

    for vehicle in Vehicle.objects.all():
        Vehicle_list.append(vehicle.plate.get_status())

    for taradod in Taradod_list:
        print("Created at %s:%s" % (taradod.seen.hour, taradod.seen.minute))
        taradod.seen = jdatetime.datetime.fromgregorian(day=taradod.seen.day, month=taradod.seen.month.numerator,
                                                        year=taradod.seen.year, hour=taradod.seen.hour,
                                                        minute=taradod.seen.minute, second=taradod.seen.second,
                                                       )

        if taradod.plate in Vehicle_list:
            taradod.approved = True

    context = {
        'Taradod_list': Taradod_list,
        'Vehicle_list': all_Vehicle_list,
        'Owner_list': Owner_lists
    }
    return render(request, 'table.html', context)
