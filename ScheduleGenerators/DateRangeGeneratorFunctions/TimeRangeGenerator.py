import datetime


def generate_timerange(startTime: datetime.datetime, timeDelta, count):
    return [startTime + (timeDelta)*frequence for frequence in range(0, count)]