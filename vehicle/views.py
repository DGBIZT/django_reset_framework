from django.shortcuts import render
from rest_framework import viewsets, status, generics
from vehicle.serliazers import CarSerializer, MotoSerializer, MilageSerializers
from vehicle.models import Car, Moto, Milage
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

class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoSerializer

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
