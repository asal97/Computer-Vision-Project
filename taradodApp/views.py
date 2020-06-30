import jdatetime
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.db.models import Q
from .models import Taradod
from registerApp.models import Vehicle
import pusher

ALPHA_MAP = {x: y + 1 for y, x in enumerate(
    ['الف', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع',
     'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی', 'D', 'S']
)}


def add_row(request):
    # TODO: استفاده از داده های واقعی
    taradod_obj = Taradod(
        plate='test-pelak',
    )
    taradod_obj.save()

    pusher_client = pusher.Pusher(
        app_id='1027643',
        key='d98471de37bd168f6edc',
        secret='646d9c2d79eb6359a95d',
        cluster='ap1',
        ssl=True
    )

    pusher_client.trigger('plate-detection', 'add-table-row', {'new-plate': taradod_obj.plate,
                                                               'new-seen-hour': 'TODO',
                                                               'new-seen-minute': 'TODO',
                                                               'new-seen-second': 'TODO',
                                                               'new-seen-date': 'TODO',
                                                               'new-img': 'TODO',
                                                               'new-approved': taradod_obj.approved,
                                                               'new-url': taradod_obj.get_absolute_url()})
    return HttpResponse(200)


def traffic_report(request, traffic_id):
    this_traffic = get_object_or_404(Taradod, id=traffic_id)
    plate_split = this_traffic.plate.split('-')
    taradods = Taradod.objects.filter(
        Q(plate=this_traffic.plate)
    )
    for taradod in taradods:
        taradod.seen = jdatetime.datetime.fromgregorian(day=taradod.seen.day, month=taradod.seen.month.numerator,
                                                        year=taradod.seen.year, hour=taradod.seen.astimezone().hour,
                                                        minute=taradod.seen.astimezone().minute,
                                                        second=taradod.seen.astimezone().second)
    if len(plate_split) == 3:  # پلاک انزلی
        vehicle = Vehicle.objects.filter(
            (Q(plate__plate_type=2) & Q(plate__firstNum=int(plate_split[2])) & Q(plate__secondNum=int(plate_split[1])))
        )
    else:  # پلاک عادی
        vehicle = Vehicle.objects.filter(
            (Q(plate__plate_type=1) & Q(plate__alpha=ALPHA_MAP[plate_split[2].strip()]) &
             Q(plate__firstNum=int(plate_split[3])) & Q(plate__secondNum=int(plate_split[1])))
        )

    # changing active status of the current car with button form
    if request.method == 'POST':
        car = Vehicle.objects.get(id=vehicle[0].id)
        car.active = False
        car.save()

    # end of action

    context = {
        'this_traffic': this_traffic,
        'this_vehicle': vehicle[0],
        'taradods': taradods
    }
    return render(request, 'traffic_report.html', context)
