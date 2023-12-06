# new_observable.py
from typing import List



class Observer:
    def update(self, message):
        pass

class Observable:
    def __init__(self):
        self._observers: List[Observer] = []

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


# observable.py

class LocationHistoryObserver(Observer):
    def update(self, message):
        from .models import RecordedValue
        # Check if the change has already been detected
        if isinstance(message, dict):
            # Check if the change has already been detected
            if not message.get('changeDetected'):
                RecordedValue.objects.create(
                    latitude=message['latitude'],
                    longitude=message['longitude'],
                    date=message['date']
                )
                # Update the message to indicate the change has been detected
                message['changeDetected'] = f"Change detected in latitude: {message['latitude']}, longitude: {message['longitude']}"
        return message
