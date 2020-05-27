import datetime
import numpy as np
from django.shortcuts import render
from registerApp.models import Plate, Owner, Vehicle
from taradodApp.models import Taradod
import jdatetime
from django.db.models import Count
import calendar
from django.db.models.functions import ExtractDay, ExtractHour, ExtractWeekDay
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


def get_this_month(taradod):
    today = datetime.datetime.now()
    if calendar.isleap(today.year):
        if datetime.date(datetime.datetime.now().year, 3, 20) <= today.date() <= datetime.date(
                datetime.datetime.now().year, 4, 19):
            start = datetime.date(datetime.datetime.now().year, 3, 20)
            end = datetime.date(datetime.datetime.now().year, 4, 19)

        elif datetime.date(datetime.datetime.now().year, 4, 20) <= today.date() <= datetime.date(
                datetime.datetime.now().year, 5, 20):
            start = datetime.date(datetime.datetime.now().year, 4, 20)
            end = datetime.date(datetime.datetime.now().year, 5, 19)

        elif datetime.date(datetime.datetime.now().year, 5, 21) <= today.date() <= datetime.date(
                datetime.datetime.now().year, 6, 20):
            start = datetime.date(datetime.datetime.now().year, 5, 21)
            end = datetime.date(datetime.datetime.now().year, 6, 20)

        elif datetime.date(datetime.datetime.now().year, 6, 21) <= today.date() <= datetime.date(
                datetime.datetime.now().year, 7, 21):
            start = datetime.date(datetime.datetime.now().year, 6, 21)
            end = datetime.date(datetime.datetime.now().year, 7, 21)

        elif datetime.date(datetime.datetime.now().year, 7, 22) <= today.date() <= datetime.date(
                datetime.datetime.now().year, 8, 21):
            start = datetime.date(datetime.datetime.now().year, 7, 22)
            end = datetime.date(datetime.datetime.now().year, 8, 21)

        elif datetime.date(datetime.datetime.now().year, 8, 22) <= today.date() <= datetime.date(
                datetime.datetime.now().year, 9, 21):
            start = datetime.date(datetime.datetime.now().year, 8, 22)
            end = datetime.date(datetime.datetime.now().year, 9, 21)

        elif datetime.date(datetime.datetime.now().year, 9, 22) <= today.date() <= datetime.date(
                datetime.datetime.now().year, 10, 21):
            start = datetime.date(datetime.datetime.now().year, 9, 22)
            end = datetime.date(datetime.datetime.now().year, 10, 21)

        elif datetime.date(datetime.datetime.now().year, 10, 22) <= today.date() <= datetime.date(
                datetime.datetime.now().year, 11, 20):
            start = datetime.date(datetime.datetime.now().year, 10, 22)
            end = datetime.date(datetime.datetime.now().year, 11, 20)

        elif datetime.date(datetime.datetime.now().year, 11, 21) <= today.date() <= datetime.date(
                datetime.datetime.now().year, 12, 20):
            start = datetime.date(datetime.datetime.now().year, 11, 21)
            end = datetime.date(datetime.datetime.now().year, 12, 20)

        elif datetime.date(datetime.datetime.now().year, 12, 21) <= today.date() <= datetime.date(
                datetime.datetime.now().year + 1, 1, 19):
            start = datetime.date(datetime.datetime.now().year, 12, 21)
            end = datetime.date(datetime.datetime.now().year + 1, 1, 19)

        elif datetime.date(datetime.datetime.now().year - 1, 12, 21) <= today.date() <= datetime.date(
                datetime.datetime.now().year, 1, 19):
            start = datetime.date(datetime.datetime.now().year - 1, 12, 21)
            end = datetime.date(datetime.datetime.now().year, 1, 19)

        elif datetime.date(datetime.datetime.now().year, 1, 20) <= today.date() <= datetime.date(
                datetime.datetime.now().year, 2, 18):
            start = datetime.date(datetime.datetime.now().year, 1, 20)
            end = datetime.date(datetime.datetime.now().year, 2, 18)

        elif datetime.date(datetime.datetime.now().year, 2, 19) <= today.date() <= datetime.date(
                datetime.datetime.now().year, 3, 20):
            start = datetime.date(datetime.datetime.now().year, 11, 21)
            end = datetime.date(datetime.datetime.now().year, 12, 20)

    Month = taradod.filter(seen__gte=start,
                           seen__lte=end)
    lastCar = Month[0]
    days = []
    date = lastCar.seen.date() - datetime.date(datetime.datetime.now().year, 5, 21)
    for i in range(0, date.days):
        days.append(0)
    count = 0
    for car in Month:
        if car.seen.day == lastCar.seen.day:
            count += 1
        else:
            days.append(count)
            count = 0
    days.append(count)

    if Month[len(Month) - 1].seen.date() < end:
        for i in range(0,
                       (end - Month[len(Month) - 1].seen.date()).days):
            days.append(0)
    return days


def table(request):
    print("weekday ", (datetime.datetime.now().weekday() + 2) % 7)
    Owner_lists = Owner.objects.all()
    all_Vehicle_list = Vehicle.objects.all()
    Taradod_list = Taradod.objects.all()

    days_of_month = get_this_month(Taradod_list)
    Vehicle_list = []
    today = get_total_today(Taradod_list)
    for vehicle in Vehicle.objects.all():
        Vehicle_list.append(vehicle.plate.get_status())

    week = get_week_day(Taradod_list)

    # Month = Taradod_list.filter(seen__gte=datetime.date(datetime.datetime.now().year, 5, 21),
    #                             seen__lte=datetime.date(datetime.datetime.now().year, 6, 20))
    # lastCar = Month[0]
    # days = []
    # date = lastCar.seen.date() - datetime.date(datetime.datetime.now().year, 5, 21)
    # print("kabise ast", calendar.isleap(datetime.datetime.now().year))
    # for i in range(0, date.days):
    #     days.append(0)
    # count = 0
    # for car in Month:
    #     print("car ", car)
    #     if car.seen.day == lastCar.seen.day:
    #         count += 1
    #         print("count! ", count)
    #     else:
    #         print("count dar else ", count)
    #         days.append(count)
    #         count = 0
    # days.append(count)
    #
    # if Month[len(Month) - 1].seen.date() < datetime.date(datetime.datetime.now().year, 6, 20):
    #     for i in range(0,
    #                    (datetime.date(datetime.datetime.now().year, 6, 20) - Month[len(Month) - 1].seen.date()).days):
    #         days.append(0)
    #
    # print("akharish ", Month[len(Month) - 1])
    #
    # print(days)
    # print("tule mahe", len(days))
    # print("ekhh ", date.days)
    # print("ekh ", lastCar.seen.date() - datetime.date(datetime.datetime.now().year, 5, 21))
    # print("day ", lastCar.seen.day)
    # print("month ", Month)

    # qs = Taradod_list.filter(
    #     seen__year=datetime.datetime.now().year,
    #     seen__month=datetime.datetime.now().month
    # ).annotate(
    #     day=ExtractDay('seen'),
    # ).values(
    #     'day'
    # ).annotate(
    #     n=Count('pk')
    # ).order_by('day')
    #
    # print("days ", qs)
    #
    # data = Counter({d['day']: d['n'] for d in qs})
    #
    # __, ds = monthrange(datetime.datetime.now().year, datetime.datetime.now().month)
    # print("data ", ds)
    # result = [data[i] for i in range(1, ds + 1)]
    # print("day result ", result)
    # print("len day", len(result))

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
        'days': days_of_month,
        'daysCount': np.sum(days_of_month),
        'weekCount': np.sum(week),
        'week': week,
        'todayCount': np.sum(today),
        'today': today,
        'Taradod_list': Taradod_list,
        'Vehicle_list': all_Vehicle_list,
        'Owner_list': Owner_lists
    }
    return render(request, 'table.html', context)
