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
import csv
from django.http import HttpResponse
from django.db.models import Q

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


def get_this_month(taradod):
    today = datetime.datetime.now()
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


def get_this_year(taradod):
    result = []
    today = datetime.datetime.now()
    if datetime.date(datetime.datetime.now().year, 3, 21) < today.date() < datetime.date(datetime.datetime.now().year,
                                                                                         12, 31):
        year_second = 1
        year_first = 0
    else:
        year_first = -1
        year_second = 0

    if calendar.isleap(today.year):
        #########################  Farvardin #################################
        Month = taradod.filter(seen__gte=datetime.date(datetime.datetime.now().year + year_first, 3, 20),
                               seen__lte=datetime.date(
                                   datetime.datetime.now().year + year_first, 4, 19))
        result.append(len(Month))
        #########################  Ordibehesht #################################
        Month = taradod.filter(seen__gte=datetime.date(datetime.datetime.now().year + year_first, 4, 20),
                               seen__lte=datetime.date(
                                   datetime.datetime.now().year + year_first, 5, 20))
        result.append(len(Month))
        #########################  Khordad #################################
        Month = taradod.filter(seen__gte=datetime.date(datetime.datetime.now().year + year_first, 5, 21),
                               seen__lte=datetime.date(
                                   datetime.datetime.now().year + year_first, 6, 20))
        result.append(len(Month))
        #########################  Tir #################################
        Month = taradod.filter(seen__gte=datetime.date(datetime.datetime.now().year + year_first, 6, 21),
                               seen__lte=datetime.date(
                                   datetime.datetime.now().year + year_first, 7, 21))
        result.append(len(Month))
        #########################  Mordad #################################
        Month = taradod.filter(seen__gte=datetime.date(datetime.datetime.now().year + year_first, 7, 22),
                               seen__lte=datetime.date(
                                   datetime.datetime.now().year + year_first, 8, 21))
        result.append(len(Month))
        #########################  Shahrivar #################################
        Month = taradod.filter(seen__gte=datetime.date(datetime.datetime.now().year + year_first, 8, 22),
                               seen__lte=datetime.date(
                                   datetime.datetime.now().year + year_first, 9, 21))
        result.append(len(Month))
        #########################  Mehr #################################
        Month = taradod.filter(seen__gte=datetime.date(datetime.datetime.now().year + year_first, 9, 22),
                               seen__lte=datetime.date(
                                   datetime.datetime.now().year + year_first, 10, 21))
        result.append(len(Month))
        #########################  Aban #################################
        Month = taradod.filter(seen__gte=datetime.date(datetime.datetime.now().year + year_first, 10, 22),
                               seen__lte=datetime.date(
                                   datetime.datetime.now().year + year_first, 11, 20))
        result.append(len(Month))
        #########################  Azar #################################
        Month = taradod.filter(seen__gte=datetime.date(datetime.datetime.now().year + year_first, 11, 21),
                               seen__lte=datetime.date(
                                   datetime.datetime.now().year + year_first, 12, 20))
        result.append(len(Month))
        #########################  Dey #################################
        Month = taradod.filter(seen__gte=datetime.date(datetime.datetime.now().year + year_first, 12, 21),
                               seen__lte=datetime.date(
                                   datetime.datetime.now().year + year_first, 12, 31))
        mid_year = len(Month)

        Month = taradod.filter(seen__gte=datetime.date(datetime.datetime.now().year + year_second, 1, 1),
                               seen__lte=datetime.date(
                                   datetime.datetime.now().year + year_second, 1, 19))
        mid_year += len(Month)
        result.append(mid_year)
        #########################  Bahman #################################
        Month = taradod.filter(seen__gte=datetime.date(datetime.datetime.now().year + year_second, 1, 20),
                               seen__lte=datetime.date(
                                   datetime.datetime.now().year + year_second, 2, 18))
        result.append(len(Month))
        #########################  Esfand #################################
        Month = taradod.filter(seen__gte=datetime.date(datetime.datetime.now().year + year_second, 2, 19),
                               seen__lte=datetime.date(
                                   datetime.datetime.now().year + year_second, 3, 20))
        result.append(len(Month))

    return result


def table(request):
    Taradod_list = Taradod.objects.all()
    Vehicle_list = []

    for vehicle in Vehicle.objects.all():
        if vehicle.active:
            Vehicle_list.append(vehicle.plate.get_status())

    # getting data for the diagram for table page
    today = get_total_today(Taradod_list)
    last_hour = today[len(today) - 1]
    today = today[0:len(today) - 1]
    print("last ", last_hour)

    week = get_week_day(Taradod_list)
    last_day = week[len(week) - 1]
    week = week[0:len(week) - 1]

    days_of_month = get_this_month(Taradod_list)
    last_day_month = days_of_month[len(days_of_month) - 1]
    days_of_month = days_of_month[0:len(days_of_month) - 1]

    months_of_year = get_this_year(Taradod_list)
    last_month = months_of_year[len(months_of_year) - 1]
    months_of_year = months_of_year[0:len(months_of_year) - 1]

    # checking whether the car is in our registered data
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

        'monthsCount': np.sum(months_of_year) + last_month,
        'months': months_of_year,
        'last_month': last_month,

        'days': days_of_month,
        'daysCount': np.sum(days_of_month) + last_day_month,
        'last_day_month': last_day_month,

        'weekCount': np.sum(week) + last_day,
        'week': week,
        'last_day': last_day,

        'todayCount': np.sum(today) + last_hour,
        'today': today,
        'last_hour': last_hour,

        'Taradod_list': Taradod_list,
    }
    return render(request, 'table.html', context)


def download_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'
    writer = csv.writer(response)
    writer.writerow(['پلاک', 'تاریخ تردد', 'وضعیت تردد'])
    traffics = Taradod.objects.all().values_list('plate', 'seen',
                                                 'approved')  # TODO: use Q() for filter some specific data
    for traffic in traffics:
        writer.writerow(traffic)
    return response
