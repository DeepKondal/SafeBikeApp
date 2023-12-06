from django.shortcuts import render
from .observable import Observer
from .models import RecordedValue
from .observable import LocationHistoryObserver,Observable
import csv
import time
import json

import datetime

from django.shortcuts import render
from .models import RecordedValue
# Create a global instance of the observer
# Create a global instance of the observer
location_history_observer = LocationHistoryObserver()

# Create a global instance of the observable
observable = Observable()
observable.add_observer(location_history_observer)

def interval_recording(request):
    intervals = [0, 1, 2, 3, 4, 5, 10, 15, 30, 60]
    selected_interval = int(request.GET.get('interval', 0))
    file_path = 'S-S1.csv'
    recorded_values = []

    if selected_interval > 0:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Read only the required number of rows based on the selected interval
            for _ in range(selected_interval * 12):  # Assuming 12 rows per minute
                row = next(reader, None)
                if not row:
                    break
                
                recorded_values.append({
                    'latitude': float(row['latitude']),
                    'longitude': float(row['longitude']),
                    'date': datetime.datetime.now().isoformat()
                })

    recorded_values_json = json.dumps(recorded_values)
    observable.notify_observers(recorded_values)  # Notify observers of changes
    return render(request, 'gps/interval_recording.html', {'intervals': intervals, 'selected_interval': selected_interval, 'recorded_values': recorded_values_json})





def location_history(request):
    recorded_values = RecordedValue.objects.all()
    return render(request, 'gps/location_history.html', {'recorded_values': recorded_values})

def home(request):
    return render(request, 'gps/home.html')


# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone  # Import the timezone module

@csrf_exempt
def save_recorded_value(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        date_value = datetime.datetime.now().isoformat()
        recorded_value = RecordedValue.objects.create(latitude=latitude, longitude=longitude, date=date_value)

        # Notify observers (e.g., LocationHistoryObserver)
        recorded_value.notify_observers('New recorded value added.')

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})