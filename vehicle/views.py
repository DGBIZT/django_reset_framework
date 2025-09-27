from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated

from vehicle.serliazers import CarSerializer, MotoSerializer, MilageSerializers, MotoMilageSerializers, MotoCreateSerializer
from vehicle.models import Car, Moto, Milage
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class CarViewSet(viewsets.ModelViewSet):
    """
        Простой ViewSet-класс для вывода списка автомобилей и информации по одному объекту
    """
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [IsAuthenticated]


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

class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer

class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()

class MotoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()

class MotoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()

class MotoDestroyAPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()


class MilageCreateAPIView(generics.CreateAPIView):
    serializer_class = MilageSerializers

class MotoMilageListAPIView(generics.ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class = MotoMilageSerializers

class MilageListAPIView(generics.ListAPIView):
    """ Для вывода списка пробегов. Фильтр"""
    serializer_class = MilageSerializers
    queryset = Milage.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('car', 'moto',)
    ordering_fields = ("year",)
