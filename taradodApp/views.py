from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Taradod
from registerApp.models import Vehicle

ALPHA_MAP = {x: y + 1 for y, x in enumerate(
    ['الف', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع',
     'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی', 'D', 'S']
)}


def traffic_report(request, traffic_id):
    this_traffic = get_object_or_404(Taradod, id=traffic_id)
    plate_split = this_traffic.plate.split('-')
    if len(plate_split) == 3:  # پلاک انزلی
        vehicle = Vehicle.objects.filter(
            (Q(plate__plate_type=2) & Q(plate__firstNum=int(plate_split[2])) & Q(plate__secondNum=int(plate_split[1])))
        )
    else:  # پلاک عادی
        vehicle = Vehicle.objects.filter(
            (Q(plate__plate_type=1) & Q(plate__alpha=ALPHA_MAP[plate_split[2].strip()]) &
             Q(plate__firstNum=int(plate_split[3])) & Q(plate__secondNum=int(plate_split[1])))
        )
    context = {
        'this_traffic': this_traffic,
        'this_vehicle': vehicle[0]
    }
    return render(request, 'traffic_report.html', context)
