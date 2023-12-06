from typing import List
from .models import RecordedValue
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

class Observer:
    def update(self, message):
        pass

class LocationHistoryObserver(Observer):
    def update(self, recorded_values):
        from .models import RecordedValue
        for value in recorded_values:
            RecordedValue.objects.create(
                latitude=value['latitude'],
                longitude=value['longitude'],
                date=value['date']
            )