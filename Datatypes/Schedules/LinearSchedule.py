from __future__ import annotations
from typing import Union
import datetime

from Datatypes.Schedules.Schedule import Schedule
from Datatypes.Job import Job
from Datatypes.Person import Person


class LinearSchedule(Schedule):
    """
    A linear scheduler (one column)
    with only one Job at maximum.
    """
    def __init__(self,
                 personVector: tuple[Person],
                 jobVector: Union[tuple[Job], Job],
                 slotDates: tuple[Union[datetime.datetime, datetime.date]],
                 scheduleSlots: list[int]):
        """

        :param personVector:
        :param jobVector:
        :param slotDates:
        :param scheduleSlots:
        """
        if isinstance(jobVector, Job):
            self.job = jobVector
        else:
            if len(jobVector) != 1:
                raise ValueError("LinearSchedule has a maximum of 1 job")
            self.job = jobVector[0]
        super().__init__(personVector=personVector, jobVector=tuple([self.job]), slotDates=slotDates, scheduleSlots=scheduleSlots)

    def __str__(self):
        print("-"*44 + "\n           | {}\n".format(self.job.JobName) + "-"*44)
        for slotDate, slot in zip(self.slotDateVector, self.scheduleSlots):
            if slot == -1:
                print("|{}| {:30}|".format(slotDate, "None"))
                continue
            if slot == -2:
                print("|{}| {:30}|".format(slotDate, "    "))
                continue
            print("|{}| {:30}|".format(slotDate, self.as_person(slot)))
        return ""  # TODO This is a bad way to make the function work"

    @classmethod
    def from_empty(cls, job: Job,
                   slotDates: tuple[datetime.date],
                   personVector: tuple[Person] = ()) -> LinearSchedule:
        return cls(personVector=personVector, jobVector=job, slotDates=slotDates, scheduleSlots=[-1]*len(slotDates))

    @classmethod
    def from_slots(cls, personVector: tuple[Person], job: Job,
                   slotDates: tuple[datetime.date], scheduleSlots: list[Union[None, Person]]):
        """

        :param personVector:
        :param job:
        :param slotDates:
        :param scheduleSlots:
        :return:
        """
        indexedScheduleSlots: list[int] = []
        for scheduleSlot in scheduleSlots:
            if not scheduleSlot:
                indexedScheduleSlots.append(0)
            elif scheduleSlot in personVector:
                indexedScheduleSlots.append(personVector.index(scheduleSlot))
            else:
                indexedScheduleSlots.append(0)

        return cls(personVector=personVector, jobVector=job, slotDates=slotDates, scheduleSlots=indexedScheduleSlots)

"""     Method which should be added, need to work around the circular import problem
        def __add__(self, other: Union[LinearSchedule, MultiSchedule]) -> MultiSchedule:
        if isinstance(other, MultiSchedule):
            return other + self
        if self.personVector != other.personVector:
            raise ValueError("TODO: Implement summation for LinearSchedule when personVectors are not equal")
        return MultiSchedule.from_linear(self, other)"""