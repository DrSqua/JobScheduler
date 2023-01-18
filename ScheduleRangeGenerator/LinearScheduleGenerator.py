import datetime
import pandas as pd


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

    rawTimeRange: int = (endDate - startDate).days + 1  # + 1 is required to include the start date

    if rawTimeRange < actionCount:
        raise AttributeError("rawTimeRange can not be smaller than totalActions")

    fittedTimeRange = rawTimeRange - (rawTimeRange % actionCount)
    actionFrequency = fittedTimeRange // actionCount

    dateRange = pd.date_range(startDate + datetime.timedelta(days=rawTimeRange % actionCount),
                              endDate,
                              freq=f"{actionFrequency}D")
    return [date.date() for date in dateRange]
