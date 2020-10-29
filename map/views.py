from django.shortcuts import render
from django.http import JsonResponse

from map.models import Sick


def map(request):
    if request.method == "POST":
        sick = Sick.from_post(request.POST)
        sick.save()


    points = Sick.get_points_dict()

    return render(request, 'map/map.html', locals())


def geojson(request):
    geojson = Sick.get_geojson()

    return JsonResponse(geojson)
