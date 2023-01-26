from __future__ import annotations
from typing import Union
import datetime
from functools import singledispatchmethod

from Datatypes.Schedules.Schedule import Schedule
from Datatypes.Schedules.LinearSchedule import LinearSchedule
from Datatypes.Person import Person
from Datatypes.Job import Job


class MultiSchedule(Schedule):
    def __init__(self,
                 personVector: tuple[Person],
                 jobVector: tuple[Job],
                 slotDates: tuple[Union[datetime.datetime, datetime.date]],
                 scheduleSlots: list[int]):
        super().__init__(personVector=personVector, jobVector=jobVector, slotDates=slotDates, scheduleSlots=scheduleSlots)
        self.scheduleJobs: tuple[Job] = jobVector

    @classmethod
    def from_empty(cls,
                   personVector: tuple[Person],
                   scheduleSlots: list[int],
                   scheduleJobs: tuple[Job]) -> MultiSchedule:
        pass

    @classmethod
    def from_linear(cls, *args: LinearSchedule):
        """

        :param args: n number of LinearSchedules
        :return:
        """
        if len(args) == 1:
            linearSchedule = args[0]
            cls(personVector=linearSchedule.personVector,
                jobVector=tuple(linearSchedule.job),
                slotDates=linearSchedule.get_slotDateVector(),
                scheduleSlots=linearSchedule.scheduleSlots)

        personVectorValid = True
        if args[0] != args[-1]:
            personVectorValid = False
        for first, second in zip(args, args[1:]):
            if first != second:
                personVectorValid = False
        if not personVectorValid:
            raise ValueError("TODO: Implement summing LinearSchedules if personVectors are not equal")

    def __str__(self):
        print("-"*44 + "\n           | {}\n".format(self.job.JobName) + "-"*44)
        for slotDate, slot in zip(self.slotDateVector, self.scheduleSlots):
            if slot == -1:
                print("|{}| {:30}|".format(slotDate, "    "))
                continue
            print("|{}| {:30}|".format(slotDate, self.as_person(slot)))
        return ""  # TODO This is a bad way to make the function work"

    def __add__(self, other: Union[LinearSchedule, MultiSchedule]):
        if isinstance(other, LinearSchedule):
            raise ValueError("TODO: Implement this")


    def get_slotMatrix(self, jobIndex, **kwargs,):
        return self.scheduleSlots