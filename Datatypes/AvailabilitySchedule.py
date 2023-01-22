import datetime
from typing import Union


class AvailabilitySchedule:
    def __init__(self, availableToggleDates: Union[None, list[datetime.datetime]] = None, togglesAreAvailable: bool = True):
        if availableToggleDates is None or len(availableToggleDates) <= 1:
            availableToggleDates = []
        self.availabilityToggleDates: list[datetime.datetime] = sorted(availableToggleDates)
        self.togglesAreAvailable = togglesAreAvailable

    def is_available(self, toCheckDate: datetime.datetime):
        """
        Quite a lengthy algorithm
        First we identify two edge cases
            The list is empty, so the whole range is available
            The date is one of our availabilityToggles, we then return the 'self.togglesAreAvailable' variable
        Then, we aim to pinpoint where the date would be in our range,
        To make a decision, we assert if the index is even or uneven
        If even, the date is in a 'not available' zone
        If uneven, the date is in an 'available' zone
        :param toCheckDate:
        :return:
        """
        if not self.availabilityToggleDates:
            return True
        if toCheckDate in self.availabilityToggleDates:
            return self.togglesAreAvailable
        dates: list[datetime.datetime] = self.availabilityToggleDates + [toCheckDate]
        dates.sort()
        toCheckDateIndex = dates.index(toCheckDate)

        if toCheckDateIndex % 2 == 0:  # If the index is Even then the date is in a "Available" zone
            return False
        else:
            return True


