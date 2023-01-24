import datetime
from typing import Union


class AvailabilitySchedule:
    def __init__(self,
                 availabilityToggleDates: Union[None, list[datetime.datetime]] = None,
                 togglesAreAvailable: bool = True):
        """
        Initializer can be called with no arguments
        availableToggleDates
        :param availabilityToggleDates:
        :param togglesAreAvailable:
        """
        if availabilityToggleDates is None or len(availabilityToggleDates) <= 1:
            availabilityToggleDates = []
        self.availabilityToggleDates: list[datetime.datetime] = sorted(availabilityToggleDates)
        self.togglesAreAvailable = togglesAreAvailable

    def is_toggleAreAvailable(self) -> bool:
        return self.togglesAreAvailable

    def set_togglesAreAvailable(self, togglesAreAvailable: bool) -> None:
        self.togglesAreAvailable = togglesAreAvailable

    def flip_togglesAreAvailable(self) -> None:
        self.togglesAreAvailable = not self.togglesAreAvailable

    def is_available(self, toCheckDate: datetime.datetime) -> bool:
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

        if toCheckDateIndex % 2 == 1:  # If the index is Uneven then the date is in an "Available" zone
            return False
        else:
            return True

    def insert_availablePeriod(self, startDate: datetime.datetime, endDate: datetime.datetime) -> None:
        if startDate >= endDate:
            raise ValueError("startdate cannot be greater than or equal to endDate")

        if startDate in self.availabilityToggleDates or endDate in self.availabilityToggleDates:
            raise ValueError("Method not fully implemented")

        if self.is_available(startDate) and self.is_available(endDate):
            # TODO Then insert both and create new list from begin->startDate + endDate -> end
            pass
        else:
            raise ValueError("Method not fully implemented")
