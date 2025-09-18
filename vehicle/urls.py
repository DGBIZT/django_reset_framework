from rest_framework.routers import DefaultRouter
from vehicle.apps import VehicleConfig
from vehicle.views import CarViewSet

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(r'cars',CarViewSet, basename='cars')



urlpatterns = [

] + router.urls