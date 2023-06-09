from django.urls import path
from .views import SensorsView, SensorView, AddMeasurement

urlpatterns = [
    path('sensors', SensorsView.as_view()),
    path('sensor/<pk>', SensorView.as_view()),
    path('add_measurement', AddMeasurement.as_view()),
]
