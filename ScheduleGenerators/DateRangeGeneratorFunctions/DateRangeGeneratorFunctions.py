import datetime
import pandas as pd
from typing import cast


def generate_from_total_actions(endDate: datetime.date,
                                actionCount: int,
                                startDate: datetime.date = datetime.datetime.today().date(),
                                fitToEndDate: bool = True) -> tuple[datetime.date]:
    """
    Creates dateRange fitted to a set interval which fits in the given date range
    :param actionCount: A 'action' occurs when the job is preformed by a person
    :param endDate: proposed endDate
    :param startDate: proposed startDate
    :param fitToEndDate: The dateRange is possibly concattenated to fit the required count
           This parameter defines which of the supplied dates should always be included in the final dateRange
    :return:
    """
    if endDate <= startDate:
        raise AttributeError("endDate can not be smaller or equal to startDate")

    rawTimeRange: int = (endDate - startDate).days  # Excluding the endDate (is left out of equations)

    if rawTimeRange < actionCount:
        raise AttributeError("rawTimeRange can not be smaller than totalActions")

    dateOffset: int = rawTimeRange % (actionCount - 1)  # Divide the time range we have in actionCount-1 parts
    fittedTimeRange: int = rawTimeRange - dateOffset  # Setting a fitting range
    actionFrequency: int = fittedTimeRange // (actionCount - 1)  # Calculating the required frequency

    if fitToEndDate:
        fittedStartDate = startDate + datetime.timedelta(days=dateOffset)
        fittedEndDate = endDate
    else:
        fittedStartDate = startDate
        fittedEndDate = endDate - datetime.timedelta(days=dateOffset)

    dateRange = pd.date_range(fittedStartDate,
                              fittedEndDate,
                              freq=f"{actionFrequency}D")
    return cast(tuple[datetime.date], list[datetime.date]([date.date() for date in dateRange]))


def generate_from_bound_frequency(endDate: datetime.date,
                                  actionFrequency: int,
                                  startDate: datetime.date = datetime.datetime.today().date(),
                                  fitToEndDate: bool = True
                                  ) -> tuple[datetime.date]:
    """
    Creates a dateRange fitted to a set interval which fits in the given date range
    :param endDate:
    :param actionFrequency:
    :param startDate:
    :param fitToEndDate:
    :return:
    """
    if endDate <= startDate:
        raise AttributeError("endDate can not be smaller or equal to startDate")

    rawTimeRange: int = (endDate - startDate).days  # Excluding the endDate (is left out of equations)
    dateOffset: int = rawTimeRange - (rawTimeRange % actionFrequency)

    if fitToEndDate:
        fittedStartDate = startDate + datetime.timedelta(days=dateOffset)
        fittedEndDate = endDate
    else:
        fittedStartDate = startDate
        fittedEndDate = endDate - datetime.timedelta(days=dateOffset)

    dateRange = pd.date_range(fittedStartDate,
                              fittedEndDate,
                              freq=f"{actionFrequency}D")
    return cast(tuple[datetime.date], list[datetime.date]([date.date() for date in dateRange]))


def generate_from_unbound_frequency(beginDate: datetime.date,
                                    actionCount: int,
                                    actionFrequency: int,
                                    fitAsEndDate: bool = False
                                    ):
    """
    Creates a dateRange fitted to a beginDate and endDate,
    the latter which is defined by amount of actions a frequency
    :param beginDate: Date from where the range will start/end counting
    :param actionCount: How many times the frequency will be called
    :param actionFrequency: How many days between the different actions
    :param fitAsEndDate: If 'beginDate' is to be treated as the endDate of the date range
    :return:
    """
    timeRange: int = (actionCount - 1) * actionFrequency

    if fitAsEndDate:
        fittedStartDate = beginDate - datetime.timedelta(days=timeRange)
        fittedEndDate = beginDate
    else:
        fittedStartDate = beginDate
        fittedEndDate = beginDate + datetime.timedelta(days=timeRange)

    dateRange = pd.date_range(fittedStartDate,
                              fittedEndDate,
                              freq=f"{actionFrequency}D")
    return cast(tuple[datetime.date], list[datetime.date]([date.date() for date in dateRange]))
