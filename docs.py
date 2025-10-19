from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(
    title='Your API',
    description='API for your application',
    version='1.0.0'
)

urlpatterns = [
    path('docs/', schema_view, name='swagger-ui'),
]
