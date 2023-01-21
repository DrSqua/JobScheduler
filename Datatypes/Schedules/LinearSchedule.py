from __future__ import annotations
from typing import Union
import datetime

from Datatypes.Schedules.Schedule import Schedule
from Datatypes.Task import Task
from Datatypes.Person import Person


class LinearSchedule(Schedule):
    """
    A linear scheduler (one column)
    with only one task at maximum.
    """
    def __init__(self, task: Task, slotDates: tuple[datetime.date], scheduleSlots: list[Union[None, Person]]):
        self.task: Task = task
        self.slotDates: tuple[datetime.date] = slotDates
        self.scheduleSlots: list[Union[None, Person]] = scheduleSlots

    def __str__(self):
        print("-"*44 + "\n           | {}\n".format(self.task.taskName) + "-"*44)
        for slotDate, slot in zip(self.slotDates, self.scheduleSlots):
            if not slot:
                print("|{}| {:30}|".format(slotDate, "None"))
                continue
            print("|{}| {:30}|".format(slotDate, slot))
        return ""  # TODO This is a bad way to make the function work"

    @classmethod
    def from_empty(cls, task: Task, slotDates: tuple[datetime.date]) -> LinearSchedule:
        return cls(task, slotDates, [None]*len(slotDates))

    def set_scheduleSlots(self, scheduleSlots: list[Union[None, Person]]) -> None:
        if len(self.scheduleSlots) != len(scheduleSlots):
            raise AttributeError("instance scheduleSlots and input scheduleSlots must have the same length")
        self.scheduleSlots = scheduleSlots

    def get_slotCount(self) -> int:
        return len(self.scheduleSlots)
