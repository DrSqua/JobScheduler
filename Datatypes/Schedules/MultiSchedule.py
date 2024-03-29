from __future__ import annotations
from typing import Union
import datetime
from copy import deepcopy

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
                   jobVector: tuple[Job],
                   slotDates: tuple[Union[datetime.datetime, datetime.date]],
                   scheduleSlots: list[int]) -> MultiSchedule:
        return cls(personVector=personVector, jobVector=jobVector, slotDates=slotDates, scheduleSlots=scheduleSlots)

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
                       scheduleSlots=linearSchedule.slotVector)

        # Check if jobDuration is equal

        # Check if personVectors are equal
        personVectorValid = True
        if args[0].get_personVector() != args[-1].get_personVector():
            personVectorValid = False
        for first, second in zip(args, args[1:]):
            if first.get_personVector() != second.get_personVector():
                personVectorValid = False
        if not personVectorValid:
            raise ValueError("TODO: Implement summing LinearSchedules if personVectors are not equal")

        # Check if start and enddate are equal
        startEndDateValid = True
        if args[0].get_slotDateVector()[0] != args[-1].get_slotDateVector()[0]:
            startEndDateValid = False
        if args[0].get_slotDateVector()[-1] != args[-1].get_slotDateVector()[-1]:
            startEndDateValid = False
        if not startEndDateValid:
            # First we pick the start and end
            minStartDate = min(schedule.get_slotDateVector()[0] for schedule in args)
            maxEndDate = max(schedule.get_slotDateVector()[-1] for schedule in args)

            for schedule in args:
                if schedule.get_slotDateVector()[0] != minStartDate:
                    pass
                if schedule.get_slotDateVector()[-1] != maxEndDate:
                    pass


    def __str__(self):
        """
        Prints the multischedule
        :return:
        """
        dateStrLen = 19
        columnWidth: list[int] = []  # Stores how wide we can format the personName per comumn

        for jobIndex in range(len(self.jobVector)):
            slotVector = self.get_slotVector(jobIndex=jobIndex)
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
                person = self.as_person(self.__get_slot__(slotIndex=slotIndex, jobIndex=jobIndex))
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
            pass
        if isinstance(other, LinearSchedule):
            # TODO: So, so, much to check
            self.jobVector += deepcopy(tuple([other.job]))
            self.slotVector += deepcopy(other.slotVector)
        if isinstance(other, MultiSchedule):
            raise ValueError("TODO: Implement this")
        return self

    def __getitem__(self, slotIndex, jobIndex: int = None):
        return super().__getitem__(slotIndex, jobIndex)
