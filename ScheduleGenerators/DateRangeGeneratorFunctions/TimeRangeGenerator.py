import datetime


def generate_timerange(startTime: datetime.datetime, timeDelta, count):
    return [startTime + (timeDelta)*frequence for frequence in range(0, count)]

def generate_timerange_byActions(startTime: datetime.datetime,
                       endTime: datetime.datetime,
                       actionCount: int,
                       fitToEndDate: bool = True,
                       timeInterval: datetime.timedelta = datetime.timedelta(days=1)) -> tuple[datetime.datetime]:
    """
    Creates dateRange fitted to a set interval which fits in the given date range
    :param actionCount: A 'action' occurs when the job is preformed by a person
    :param endTime: proposed endTime
    :param startTime: proposed startTime
    :param fitToEndDate: The dateRange is possibly concattenated to fit the required count
           This parameter defines which of the supplied dates should always be included in the final dateRange
    :return:
    """
    if endTime <= startTime:
        raise ValueError("endTime can not be smaller or equal to startTime")

    rawTimeRange: int = (endDate - startDate).days  # Excluding the endDate (is left out of equations)

    if rawTimeRange < actionCount:
        raise ValueError("rawTimeRange can not be smaller than totalActions")

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