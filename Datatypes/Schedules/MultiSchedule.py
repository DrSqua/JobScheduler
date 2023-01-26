from __future__ import annotations
from typing import Union
import datetime

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
            return cls(personVector=linearSchedule.personVector,
                       jobVector=tuple([linearSchedule.job]),
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

        dateStrLen = 19
        columnWidth: list[int] = []  # Stores how wide we can format the personName per comumn

        # Header
        print(dateStrLen*" " + " | ", end="")
        jobGen = (job.jobName for job in self.jobVector)
        for job in jobGen:
            columnWidth.append(len(job.__str__()))
            print(job, end="")
        print(" |")
        print("-" * (dateStrLen + 2))

        # Frame
        for slotIndex, slotDate in enumerate(self.slotDateVector):
            print(str(slotDate) + " | ", end="")
            for jobIndex, j in zip(range(len(self.jobVector)), columnWidth):
                person = self.get_slot_asPerson(slotIndex=slotIndex, jobIndex=jobIndex)
                if not person:
                    print(("{:"+str(j)+"}").format("None"), end="")
                    continue
                print(("{:"+str(j)+"}").format(person, end=""))
            print(" |")
        return ""  # TODO This is a bad way to make the function work"

    def __add__(self, other: Union[LinearSchedule, MultiSchedule]):
        if isinstance(other, LinearSchedule):
            raise ValueError("TODO: Implement this")

    def get_slotMatrix(self, jobIndex, **kwargs,):
        return self.scheduleSlots

    def get_slot(self, slotIndex: int, **kwargs) -> int:
        if "jobIndex" in kwargs:
            jobIndex = kwargs["jobIndex"]
            return self.scheduleSlots[jobIndex*len(self.slotDateVector) + slotIndex]
        return self.scheduleSlots[slotIndex]

    def get_slot_asPerson(self, slotIndex: int, **kwargs) -> Person:
        if "jobIndex" in kwargs:
            return self.as_person(self.get_slot(slotIndex, jobIndex=kwargs["jobIndex"]))
        return self.as_person(self.get_slot(slotIndex))
