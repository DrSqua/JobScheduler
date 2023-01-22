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
                 job: Job,
                 slotDates: tuple[datetime.date],
                 scheduleSlots: list[int]):
        super().__init__(personVector=personVector, scheduleSlots=scheduleSlots)
        self.Job: Job = job
        self.slotDates: tuple[datetime.date] = slotDates

    def __str__(self):
        print("-"*44 + "\n           | {}\n".format(self.Job.JobName) + "-"*44)
        for slotDate, slot in zip(self.slotDates, self.scheduleSlots):
            if slot == -1:
                print("|{}| {:30}|".format(slotDate, "    "))
                continue
            print("|{}| {:30}|".format(slotDate, self.as_person(slot)))
        return ""  # TODO This is a bad way to make the function work"

    @classmethod
    def from_empty(cls, personVector: tuple[Person], job: Job,
                   slotDates: tuple[datetime.date]) -> LinearSchedule:
        return cls(personVector=personVector, job=job, slotDates=slotDates, scheduleSlots=[0]*len(slotDates))

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

        return cls(personVector=personVector, job=job, slotDates=slotDates, scheduleSlots=indexedScheduleSlots)

    def __add__(self, other):
        pass

    def is_validSlotIndex(self, slotIndex: int) -> bool:
        return slotIndex < 0 | len(self.slotDates) < slotIndex

    def get_slotCount(self) -> int:
        return len(self.scheduleSlots)

    def get_scheduleSlots(self) -> list[Union[None, Person]]:
        return [self.as_person(personIndex=personIndex) for personIndex in self.scheduleSlots]

    def set_scheduleSlots(self, scheduleSlots: list[Union[None, Person]]) -> None:
        if len(self.scheduleSlots) != len(scheduleSlots):
            raise ValueError("instance scheduleSlots and input scheduleSlots must have the same length")
        self.scheduleSlots = [self.as_personIndex(person) for person in scheduleSlots]

    def get_slot(self, slotIndex: int) -> Union[None, Person]:
        """
        Returns Person instance or None of a given slot
        :param slotIndex:
        :return:
        """
        if self.is_validSlotIndex(slotIndex):
            raise ValueError("slotIndex is required to be greater or equal to zero and smaller than size of "
                             "slotDate tuple")
        return self.as_person(self.scheduleSlots[slotIndex])

    def set_slot(self, slotValue: Union[None, Person], slotIndex: int):
        """
        Sets the value of a slot in the scheduleSlots to the personIndex of the given person (or None)
        :param slotValue:
        :param slotIndex:
        :return:
        """
        if self.is_validSlotIndex(slotIndex):
            raise ValueError("slotIndex is required to be greater or equal to zero and smaller than size of "
                             "slotDate tuple")
        self.scheduleSlots[slotIndex] = self.as_personIndex(slotValue)
