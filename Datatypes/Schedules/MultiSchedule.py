from typing import Union

from Datatypes.Schedules.Schedule import Schedule
from Datatypes.Person import Person


class MultiSchedule(Schedule):
    def __init__(self, scheduleSlots: list[Union[None, Person]]):
        super().__init__(scheduleSlots)