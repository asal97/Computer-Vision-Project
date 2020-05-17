from django.shortcuts import render
from registerApp.models import Plate, Owner, Vehicle
from taradodApp.models import Taradod


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
        if taradod.plate in Vehicle_list:
            print("!!! ",taradod.plate)
            taradod.approved = True
    print("!!!!!!!!!!!!!!!!!!!!!!!!")
    print(Taradod_list)
    print("!!!!!!!!!!!!!!!!!!!!!!!!")
    print(Vehicle_list)
    print("!!!!!!!!!!!!!!!!!!!!!!!!")

    print(all_Vehicle_list)

    return render(request, 'table.html', {
        'Taradod_list' : Taradod_list,
        'Vehicle_list': all_Vehicle_list,
        'Owner_list': Owner_lists
    })
