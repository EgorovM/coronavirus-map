from django.contrib import admin
from django.urls import path

from map import views


urlpatterns = [
    path('', views.map),
    path('map/calls/geojson/', views.geojson)
]
