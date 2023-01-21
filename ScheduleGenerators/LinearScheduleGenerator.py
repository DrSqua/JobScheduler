import datetime
import pandas as pd

from Datatypes.Schedules.LinearSchedule import LinearSchedule
from Datatypes.Task import Task
from ScheduleGenerators.ScheduleGenerator import ScheduleGenerator


class LinearScheduleGenerator(ScheduleGenerator):
    """LinearScheduleGenerator"""
    def __init__(self, task: Task):
        self.task = task

    def generate_schedule(self,
                          endDate: datetime.date,
                          actionCount: int,
                          startDate: datetime.date = datetime.date.today()) -> LinearSchedule:
        date_range = generate_calender_totalactionbase(endDate, actionCount, startDate)

        return LinearSchedule.from_empty(self.task, tuple(date_range))


def generate_calender_totalactionbase(endDate: datetime.date,
                                      actionCount: int,
                                      startDate: datetime.date = datetime.date.today()) -> list[datetime.date]:
    """
    Returns a range of dates, fitted to a set interval which fits in the given date range

    :param actionCount: A 'action' occurs when the job is preformed by a person.
    :param endDate:
    :param startDate:
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

    fittedStartDate = startDate + datetime.timedelta(days=dateOffset)
    dateRange = pd.date_range(fittedStartDate,
                              endDate,
                              freq=f"{actionFrequency}D")
    temp = [date.date() for date in dateRange]
    print(temp)
    return temp
