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
    def __init__(self, job: Job,
                 slotDates: tuple[datetime.date],
                 scheduleSlots: list[Union[None, Person]]):
        super().__init__(scheduleSlots)
        self.Job: Job = job
        self.slotDates: tuple[datetime.date] = slotDates

    def __str__(self):
        print("-"*44 + "\n           | {}\n".format(self.Job.JobName) + "-"*44)
        for slotDate, slot in zip(self.slotDates, self.scheduleSlots):
            if not slot:
                print("|{}| {:30}|".format(slotDate, "None"))
                continue
            print("|{}| {:30}|".format(slotDate, slot))
        return ""  # TODO This is a bad way to make the function work"

    @classmethod
    def from_empty(cls, job: Job, slotDates: tuple[datetime.date]) -> LinearSchedule:
        return cls(job, slotDates, [None]*len(slotDates))

    @classmethod
    def from_slots(cls, job: Job, slotDates: tuple[datetime.date], scheduleSlots: list[Union[None, Person]]):
        return cls(job, slotDates, scheduleSlots)

    def __add__(self, other):
        return

    def is_validSlotIndex(self, slotIndex: int, *args, **kwargs) -> bool:
        return slotIndex < 0 | len(self.slotDates) < slotIndex

    def get_slotCount(self) -> int:
        return len(self.scheduleSlots)

    def get_scheduleSlots(self) -> list[Union[None, Person]]:
        return self.scheduleSlots

    def set_scheduleSlots(self, scheduleSlots: list[Union[None, Person]]) -> None:
        if len(self.scheduleSlots) != len(scheduleSlots):
            raise ValueError("instance scheduleSlots and input scheduleSlots must have the same length")
        self.scheduleSlots = scheduleSlots

    def get_slot(self, slotIndex: int) -> Union[None, Person]:
        if self.is_validSlotIndex(slotIndex):
            raise ValueError("slotIndex is required to be greater or equal to zero and smaller than size of "
                                 "slotDate tuple")
        return self.scheduleSlots[slotIndex]

    def set_slot(self, slotValue: Union[None, Person], slotIndex: int):
        if self.is_validSlotIndex(slotIndex):
            raise ValueError("slotIndex is required to be greater or equal to zero and smaller than size of "
                                 "slotDate tuple")
        self.scheduleSlots[slotIndex] = slotValue
