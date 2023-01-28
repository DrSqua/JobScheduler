import datetime
from typing import cast


def create_range(startTime: datetime.datetime,
                 actionCount: int,
                 timeUnit: datetime.timedelta = datetime.timedelta(days=1)
                 ) -> tuple[datetime.datetime]:
    """

    :param startTime:
    :param actionCount:
    :param timeUnit:
    :return:
    """
    return cast(tuple[datetime.datetime], [startTime + timeUnit * i for i in range(actionCount)])


def fit_range(startTime: datetime.datetime,
              actionCount: int,
              timeUnit: datetime.timedelta = datetime.timedelta(days=1),
              endTime: datetime.datetime = None,
              fitToEndTime: bool = True):

    if endTime is None:
        return create_range(startTime=startTime, actionCount=actionCount, timeUnit=timeUnit)

    if endTime <= startTime:
        raise ValueError("endTime must be equal to or larger than startTime")

    timeDelta = endTime - startTime
    rawTimeRange = timeDelta // timeUnit  # How many time the timeUnit fits into the interval given by startTime and endTime

    if rawTimeRange < actionCount:
        raise ValueError("rawTimeRange can not be smaller than totalActions")

    dateOffset: int = rawTimeRange % (actionCount - 1)  # Divide the time range we have in actionCount-1 parts
    fittedTimeRange: int = rawTimeRange - dateOffset  # Setting a fitting range
    actionFrequency: int = fittedTimeRange // (actionCount - 1)  # Calculating the required frequency

    if fitToEndTime:
        fittedStartTime = startTime + datetime.timedelta(days=dateOffset)
    else:
        fittedStartTime = startTime
    return create_range(startTime=fittedStartTime, actionCount=actionCount, timeUnit=timeUnit*actionFrequency)
