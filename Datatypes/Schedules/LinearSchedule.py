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
                 job: Union[Job],
                 slotDates: tuple[datetime.datetime],
                 scheduleSlots: list[int]):
        """
        :param personVector:
        :param slotDates:
        :param scheduleSlots:
        """
        super().__init__(personVector=personVector, jobVector=tuple([job]), slotDates=slotDates, scheduleSlots=scheduleSlots)
        self.job = job

    def __str__(self):
        dateStrLen = 19

        personVector = map(self.as_person, self.slotVector)
        personNameLengthList = list(map(lambda x: len(x.personName) if x else 0, personVector)) + [len(self.jobVector[0].jobName)]
        columnWidth = max(personNameLengthList)  # Stores how wide we can format the personName per comumn

        # Header
        result: str = dateStrLen*" " + " |"
        result += (" {:" + str(columnWidth) + "} |").format(self.jobVector[0].jobName)

        # Horizontal dotted line
        result += "\n" + "-" * (dateStrLen + 2 + columnWidth + 2)

        # Frame
        for slotIndex, slotDate in enumerate(self.slotDateVector):
            result += "\n" + str(slotDate) + " |"
            person = self.get_slot(slotIndex=slotIndex)
            if not person:
                result += (" {:"+str(columnWidth)+"} |").format("None")
                continue
            result += (" {:"+str(columnWidth)+"} |").format(person)
        return result

    @classmethod
    def from_empty(cls,
                   job: Job,
                   slotDates: tuple[datetime.datetime],
                   personVector: tuple[Person]) -> LinearSchedule:
        return cls(personVector=personVector, job=job, slotDates=slotDates, scheduleSlots=[-1]*len(slotDates))

    @classmethod
    def from_slots(cls, personVector: tuple[Person], job: Job,
                   slotDates: tuple[datetime.datetime], scheduleSlots: list[Union[None, Person]]):
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
