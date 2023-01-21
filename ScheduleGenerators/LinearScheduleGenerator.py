import datetime
import pandas as pd

from Datatypes.Schedules.LinearSchedule import LinearSchedule
from Datatypes.Task import Task
from ScheduleGenerators.ScheduleGenerator import ScheduleGenerator


class LinearScheduleGenerator(ScheduleGenerator):
    """LinearScheduleGenerator"""
    def __init__(self, task: Task):
        self.task = task

    def generate_from_totalActions(self,
                                   endDate: datetime.date,
                                   actionCount: int,
                                   startDate: datetime.date = datetime.datetime.today().date(),
                                   fitToEnd: bool = True) -> LinearSchedule:
        dateRange = generate_calender_totalactionbase(endDate, actionCount, startDate, fitToEnd)

        return LinearSchedule.from_empty(self.task, tuple(dateRange))


def generate_calender_totalactionbase(endDate: datetime.date,
                                      actionCount: int,
                                      startDate: datetime.date = datetime.date.today(),
                                      fitToEndDate: bool = True) -> list[datetime.date]:
    """
    Returns a range of dates, fitted to a set interval which fits in the given date range

    :param actionCount: A 'action' occurs when the job is preformed by a person.
    :param endDate:
    :param startDate:
    :param fitToEndDate:
    :return:
    """
    if endDate <= startDate:
        raise AttributeError("endDate can not be smaller or equal to startDate")

    rawTimeRange: int = (endDate - startDate).days  # Excluding the endDate (is left out of equations)

    if rawTimeRange < actionCount:
        raise AttributeError("rawTimeRange can not be smaller than totalActions")

    dateOffset = rawTimeRange % (actionCount-1)  # We must divide the time range we have in actionCount-1 parts
    fittedTimeRange = rawTimeRange - dateOffset  # Setting a fitting range
    actionFrequency = fittedTimeRange // (actionCount-1)  # Calculating the required frequency

    if fitToEndDate:
        fittedStartDate = startDate + datetime.timedelta(days=dateOffset)
        fittedEndDate = endDate
    else:
        fittedStartDate = startDate
        fittedEndDate = endDate - datetime.timedelta(days=dateOffset)

    dateRange = pd.date_range(fittedStartDate,
                              fittedEndDate,
                              freq=f"{actionFrequency}D")
    return [date.date() for date in dateRange]
