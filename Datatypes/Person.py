from __future__ import annotations
import datetime
from Datatypes.AvailabilitySchedule import AvailabilitySchedule


class Person:
    def __init__(self, name: str, availabilitySchedule: AvailabilitySchedule = AvailabilitySchedule()):
        self.personName: str = name
        self.availabilitySchedule: availabilitySchedule

    def __str__(self):
        return f"{self.personName}"

    def __repr__(self):
        return self.__str__()

    def __format__(self, format_spec):
        diff: int = int(format_spec)-len(self.personName)
        if diff < 0:
            return self.personName[:len(self.personName)-diff]
        return self.personName + ' '*diff

    def __eq__(self, other: Person):
        if self.personName == other.personName:
            return True
        return False

    def is_available(self, startDate: datetime.datetime, endDate: datetime.datetime = None) -> bool:
        return True
