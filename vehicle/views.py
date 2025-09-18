from django.shortcuts import render
from rest_framework import viewsets
from vehicle.serliazers import CarSerializer
from vehicle.models import Car


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

