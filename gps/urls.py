from django.urls import path
from .views import interval_recording, location_history,home,save_recorded_value

urlpatterns = [
    path('', home, name='home'),
    path('interval-recording/', interval_recording, name='interval_recording'),
    path('location-history/', location_history, name='location_history'),
    path('save-recorded-value/', save_recorded_value, name='save_recorded_value'),
]
