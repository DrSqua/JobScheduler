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

    def __is_date_available(self, toCheckDate: datetime.datetime):
        """
        Returns True if a single datapoint is available
        First we identify two edge cases
            The list is empty, so the whole range is available
            The date is one of our availabilityToggles, we then return the 'self.togglesAreAvailable' variable
        Then, we aim to pinpoint where the date would be in our range,
        To make a decision, we assert if the index is even or uneven
        If even, the date is in a 'not available' zone
        If uneven, the date is in an 'available' zone
        :param toCheckDate: The date to be cheched
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
            return False  # Uneven
        else:
            return True  # Even

    def is_available(self, startDate: datetime.datetime, endDate: datetime.datetime = None) -> bool:
        """
        Returns True of both points and all date between them are available
        Will call self.is_date_available(startDate) if endDate is None
        First we identify two edge cases
            The list is empty, so the whole range is available
            Either date is not available, then the range is not available
        Then, we aim to pinpoint where the specified dateRange would be in our range,
        To make a decision, we assert if the indices are next to eachother
        If they are next to eachother, the date is in a 'available' zone
        If they are not, the date is in an 'not available' zone
        :param endDate:
        :param startDate:
        :return:
        """
        if endDate is None:
            return self.__is_date_available(startDate)

        if not self.availabilityToggleDates:
            return True

        if (not self.__is_date_available(startDate)) or (not self.__is_date_available(endDate)):
            return False

        dates: list[datetime.datetime] = self.availabilityToggleDates + [startDate, endDate]
        dates.sort()
        toCheckDateIndeces = (dates.index(startDate), dates.index(endDate))

        if toCheckDateIndeces[0] == toCheckDateIndeces[1] + 1:
            return True

    def insert_notAvailablePeriod(self, startDate: datetime.datetime, endDate: datetime.datetime):
        raise ValueError("Method not fully implemented")

    def insert_availablePeriod(self, startDate: datetime.datetime, endDate: datetime.datetime) -> None:
        if startDate >= endDate:
            raise ValueError("startdate cannot be greater than or equal to endDate")

        if not self.availabilityToggleDates:
            return  # If everything is available we cannot add an availableRange

        if startDate in self.availabilityToggleDates or endDate in self.availabilityToggleDates:
            raise ValueError("Method not fully implemented")

        dates: list[datetime.datetime] = self.availabilityToggleDates + [startDate, endDate]
        dates.sort()
        startDateIndex, endDateIndex = (dates.index(startDate), dates.index(endDate))
        # [:x] does not include x
        # [x:] does include x

        # Case 1 -> Both in not available -> [a, b]
        if (not self.is_available(startDate)) and (not self.is_available(endDate)):
            self.availabilityToggleDates = dates[:(startDateIndex+1)] + dates[endDateIndex:]
        # Case 2 -> Both available -> ]a, b[
        elif self.is_available(startDate) and self.is_available(endDate):
            self.availabilityToggleDates = dates[:startDateIndex] + dates[(endDateIndex-1):]
        # Case 3 -> A available and B not available -> ]a, b]
        elif self.is_available(startDate) and (not self.is_available(endDate)):
            self.availabilityToggleDates = dates[:startDateIndex] + dates[endDateIndex:]
        # Case 4 -> A not available and B available ->
        elif (not self.is_available(startDate)) and self.is_available(endDate):
            self.availabilityToggleDates = dates[:(startDateIndex + 1)] + dates[(endDateIndex-1):]
        else:
            raise ValueError("All options exhausted (this should never happen)")
