from rest_framework.routers import DefaultRouter
from vehicle.apps import VehicleConfig
from vehicle.views import CarViewSet, MotoCreateAPIView, MotoListAPIView, MotoRetrieveAPIView, \
    MotoUpdateAPIView, MotoDestroyAPIView, MilageCreateAPIView
from django.urls import path

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(r'cars',CarViewSet, basename='cars')

urlpatterns = [
    path("moto/create/", MotoCreateAPIView.as_view(), name="moto-create"),
    path("moto/", MotoListAPIView.as_view(), name="moto-list"),
    path("moto/<int:pk>/", MotoRetrieveAPIView.as_view(), name="moto-get"),
    path("moto/update/<int:pk>/", MotoUpdateAPIView.as_view(), name="moto-update"),
    path("moto/delete/<int:pk>/", MotoDestroyAPIView.as_view(), name="moto-delete"),

    #milage
    path("milage/create/", MilageCreateAPIView.as_view(), name="milage-create" )

] + router.urls