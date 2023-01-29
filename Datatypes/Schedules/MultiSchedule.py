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
        super().__init__(personVector=personVector, jobVector=jobVector, slotDates=slotDates,
                         scheduleSlots=scheduleSlots)
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
        """
        Prints the multischedule
        :return:
        """
        dateStrLen = 19
        columnWidth: list[int] = []  # Stores how wide we can format the personName per comumn

        for jobIndex in range(len(self.jobVector)):
            slotVector = self.get_slotVector(jobIndex)
            personVector = map(self.as_person, slotVector)
            personNameLengthList = list(map(lambda x: len(x.personName) if x else 0, personVector)) + [
                len(self.as_job(jobIndex).jobName)]
            columnWidth.append(max(personNameLengthList))

        # Header
        result: str = dateStrLen * " " + " |"
        result += "".join([(" {:" + str(j) + "} |").format(job.jobName) for job, j in zip(self.jobVector, columnWidth)])

        # Horizontal dotted line
        result += "\n" + "-" * (dateStrLen + 2 + sum(columnWidth) + 2 * len(columnWidth))

        # Frame
        for slotIndex, slotDate in enumerate(self.slotDateVector):
            result += "\n" + str(slotDate) + " |"
            for jobIndex, j in zip(range(len(self.jobVector)), columnWidth):
                person = self.get_slot_asPerson(slotIndex=slotIndex, jobIndex=jobIndex)
                if not person:
                    result += (" {:" + str(j) + "} |").format("None")
                    continue
                result += (" {:" + str(j) + "} |").format(person)
        return result

    def __add__(self, other: Union[LinearSchedule, MultiSchedule]):
        """
        Adds two schedules together
        :param other:
        :return:
        """
        if self.personVector != other.personVector:
            self.rebase_personVector(tuple(set(self.personVector).union(other.personVector)))
        if isinstance(other, LinearSchedule):
            # TODO: So, so, much to check
            self.jobVector += tuple([other.job])
            self.scheduleSlots += other.scheduleSlots
        if isinstance(other, MultiSchedule):
            raise ValueError("TODO: Implement this")
        return self

    def get_slotVector(self, jobIndex=None):
        if jobIndex is None:
            return super().get_slotVector()
        return self.scheduleSlots[jobIndex * self.slotRowCount:(jobIndex + 1) * self.slotRowCount]

    def is_valid_slotIndex(self, slotIndex: int, jobIndex=None) -> bool:
        if not jobIndex:
            return super().is_valid_slotIndex(slotIndex)
        if 0 <= slotIndex < self.slotRowCount:
            return True
        return False

    def get_slot(self, slotIndex: int, jobIndex=None) -> int:
        if not jobIndex:
            return super().get_slot(slotIndex)
        if not self.is_valid_slotIndex(slotIndex, jobIndex):
            raise ValueError("slotIndex must be valid")
        return self.scheduleSlots[jobIndex * self.slotRowCount + slotIndex]

    def set_slot(self, slotIndex: int, slotValue, jobIndex=None):
        if not jobIndex:
            super().set_slot(slotIndex=slotIndex, slotValue=slotValue)
            return
        if not self.is_valid_slotIndex(slotIndex=slotIndex, jobIndex=jobIndex):
            raise ValueError("slotIndex must be valid")
        super().set_slot(slotIndex=slotIndex + jobIndex * self.slotRowCount, slotValue=slotValue)

    def get_slot_asPerson(self, slotIndex: int, jobIndex: int = None) -> Person:
        if not jobIndex:
            return self.as_person(self.get_slot(slotIndex))
        return super().get_slot_asPerson(slotIndex=slotIndex+jobIndex*self.slotRowCount)
