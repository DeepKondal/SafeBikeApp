from django.shortcuts import render
from .observable import Observer
from .models import RecordedValue
from .observable import LocationHistoryObserver
import csv
import time
import json

import datetime

from django.shortcuts import render
from .models import RecordedValue
# Create a global instance of the observer
location_history_observer = LocationHistoryObserver()


def interval_recording(request):
    intervals = [0,1, 2, 3, 4, 5, 10, 15, 30, 60]  # Specify available intervals
    selected_interval = int(request.GET.get('interval', 0))
    file_path = 'S-S1.csv'  # Update with your actual file path
    recorded_values = []

    if selected_interval > 0:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                recorded_values.append({
                    'latitude': float(row['latitude']),
                    'longitude': float(row['longitude']),
                    'date': datetime.datetime.now().isoformat()
                })

    recorded_values_json = json.dumps(recorded_values)
    return render(request, 'gps/interval_recording.html', {'intervals': intervals, 'selected_interval': selected_interval, 'recorded_values': recorded_values_json})

def location_history(request):
    recorded_values = RecordedValue.objects.all()
    return render(request, 'gps/location_history.html', {'recorded_values': recorded_values})

def home(request):
    return render(request, 'gps/home.html')


# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def save_recorded_value(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Process and save the recorded value to the database
        # (You'll need to adapt this based on your model structure)
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        date = data.get('date')
        RecordedValue.objects.create(latitude=latitude, longitude=longitude, date=date)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
