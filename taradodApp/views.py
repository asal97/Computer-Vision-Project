from django.shortcuts import render, get_object_or_404
from .models import Taradod


def traffic_report(request, traffic_id):
    this_traffic = get_object_or_404(Taradod, id=traffic_id)
    context = {
        'this_traffic': this_traffic
    }
    return render(request, 'traffic_report.html', context)
