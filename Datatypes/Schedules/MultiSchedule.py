from typing import Union

from Datatypes.Schedules.Schedule import Schedule
from Datatypes.Person import Person
from Datatypes.Job import Job


class MultiSchedule(Schedule):
    def __init__(self, scheduleSlots: list[Union[None, Person]], scheduleJobs: tuple[Job]):
        super().__init__(scheduleSlots)
        self.scheduleJobs: tuple[Job] = scheduleJobs
