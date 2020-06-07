import datetime
import numpy as np
from django.shortcuts import render
from registerApp.models import Plate, Owner, Vehicle
from taradodApp.models import Taradod
import jdatetime
from django.db.models import Count
from django.db.models.functions import ExtractDay, ExtractHour, ExtractWeekDay
from calendar import monthrange

from collections import Counter


def index(request):
    Taradod_list = Taradod.objects.all()
    Vehicle_list = []

    for vehicle in Vehicle.objects.all():
        if vehicle.active:
            Vehicle_list.append(vehicle.plate.get_status())

    Taradod_list = Taradod_list.filter(seen__week_day=((datetime.datetime.today().weekday()) + 2) % 7)

    for taradod in Taradod_list:
        taradod.seen = jdatetime.datetime.fromgregorian(day=taradod.seen.day, month=taradod.seen.month.numerator,
                                                        year=taradod.seen.year, hour=taradod.seen.astimezone().hour,
                                                        minute=taradod.seen.astimezone().minute,
                                                        second=taradod.seen.astimezone().second
                                                        )
        print("nmidunam! ", taradod.seen.time)
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
    qn = taradod.filter(
        seen__day=datetime.datetime.now().astimezone().day
    ).annotate(
        hour=ExtractHour('seen'),
    ).values(
        'hour'
    ).annotate(
        n=Count('pk')
    ).order_by('hour')

    data = Counter({d['hour']: d['n'] for d in qn})

    ds = 23
    result = [data[i] for i in range(0, ds + 1)]
    return result


def get_week_day(taradod):
    week = taradod.annotate(weekday=ExtractWeekDay('seen')).values('weekday').annotate(count=Count('id')).values(
        'weekday', 'count')
    data = Counter({d['weekday']: d['count'] for d in week})
    result = [data[i] for i in range(0, 7)]
    print("week result ", result)

    return result


def table(request):
    print("weekday ", (datetime.datetime.now().weekday() + 2) % 7)
    Owner_lists = Owner.objects.all()
    all_Vehicle_list = Vehicle.objects.all()
    Taradod_list = Taradod.objects.all()

    Vehicle_list = []
    today = get_total_today(Taradod_list)
    for vehicle in Vehicle.objects.all():
        if vehicle.active:
            Vehicle_list.append(vehicle.plate.get_status())


    week = get_week_day(Taradod_list)

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
        print("nmidunam! ", taradod.seen.time)
        if taradod.plate in Vehicle_list:
            taradod.approved = True

    context = {
        'weekCount': np.sum(week),
        'week': week,
        'todayCount': np.sum(today),
        'today': today,
        'Taradod_list': Taradod_list,
        'Vehicle_list': all_Vehicle_list,
        'Owner_list': Owner_lists
    }
    return render(request, 'table.html', context)