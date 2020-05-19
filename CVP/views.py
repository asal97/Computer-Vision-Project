import datetime
import numpy as np
from django.shortcuts import render
from registerApp.models import Plate, Owner, Vehicle
from taradodApp.models import Taradod
import jdatetime
from django.db.models import Count
from django.db.models.functions import ExtractDay, ExtractHour
from calendar import monthrange

from collections import Counter


def index(request):
    Taradod_list = Taradod.objects.all()
    Vehicle_list = []

    for vehicle in Vehicle.objects.all():
        Vehicle_list.append(vehicle.plate.get_status())

    Taradod_list = Taradod_list.filter(seen__week_day=((datetime.datetime.today().weekday()) + 2) % 7)

    print("today " + str(datetime.datetime.today().weekday()))
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
    }

    return render(request, 'index.html', context)


def get_countHour(Tlist):
    this_hour = datetime.datetime.now().replace(minute=0, second=0, microsecond=0)
    one_hour_later = this_hour + datetime.timedelta(hours=1)
    Tlist.filter(date__range=(this_hour, one_hour_later))


def get_total_today(taradod):
    print("hour ",datetime.datetime.now().astimezone().hour)
    qn = taradod.filter(
        seen__day=datetime.datetime.now().astimezone().day
    ).annotate(
        hour=ExtractHour('seen'),
    ).values(
        'hour'
    ).annotate(
        n=Count('pk')
    ).order_by('hour')

    print("qn12 hour ", qn)

    data = Counter({d['hour']: d['n'] for d in qn})

    ds = 23
    result = [data[i] for i in range(0, ds + 1)]
    print("result hour ", result)
    return result

def table(request):
    Owner_lists = Owner.objects.all()
    all_Vehicle_list = Vehicle.objects.all()
    Taradod_list = Taradod.objects.all()

    Vehicle_list = []
    today = get_total_today(Taradod_list)
    for vehicle in Vehicle.objects.all():
        Vehicle_list.append(vehicle.plate.get_status())


    qs = Taradod_list.filter(
        seen__year=datetime.datetime.now().year,
        seen__month=datetime.datetime.now().month
    ).annotate(
        day=ExtractDay('seen'),
    ).values(
        'day'
    ).annotate(
        n=Count('pk')
    ).order_by('day')

    print("days ", qs)

    data = Counter({d['day']: d['n'] for d in qs})

    __, ds = monthrange(datetime.datetime.now().year, datetime.datetime.now().month)
    print("data ", ds)
    result = [data[i] for i in range(1, ds + 1)]
    print("day result ", result)
    print("len day", len(result))


    # Taradod_list = Taradod_list.filter(seen__week_day=((datetime.datetime.today().weekday()) + 2) % 7)
    print("today " + str(datetime.datetime.today().weekday()))
    for taradod in Taradod_list:
        taradod.seen = jdatetime.datetime.fromgregorian(day=taradod.seen.day, month=taradod.seen.month.numerator,
                                                        year=taradod.seen.year, hour=taradod.seen.astimezone().hour,
                                                        minute=taradod.seen.astimezone().minute,
                                                        second=taradod.seen.astimezone().second
                                                        )

        if taradod.plate in Vehicle_list:
            taradod.approved = True

    context = {
        'todayCount': np.sum(today),
        'today': today,
        'Taradod_list': Taradod_list,
        'Vehicle_list': all_Vehicle_list,
        'Owner_list': Owner_lists
    }
    return render(request, 'table.html', context)
