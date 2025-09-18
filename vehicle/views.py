from django.shortcuts import render
from rest_framework import viewsets, status
from vehicle.serliazers import CarSerializer
from vehicle.models import Car
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class CarViewSet(viewsets.ModelViewSet):
    """
        Простой ViewSet-класс для вывода списка автомобилей и информации по одному объекту
    """
    serializer_class = CarSerializer
    queryset = Car.objects.all()


    def create(self, request, *args, **kwargs):
        # Проверяем, является ли данные списком
        if isinstance(request.data, list):
            # Массовое создание объектов
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Одиночное создание объекта
            return super().create(request, *args, **kwargs)
