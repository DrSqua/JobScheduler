import datetime
from random import sample
from copy import deepcopy

from Datatypes.Person import Person
from Datatypes.Schedules.LinearSchedule import LinearSchedule


class LinearJobScheduler:
    def __init__(self, personList: list[Person], startingSchedule):
        self.personList = personList
        self.schedule: LinearSchedule = startingSchedule

    def fill_schedule(self):
        randomPersonOrder = sample(self.personList, self.schedule.get_slotCount())
        filledSchedule: LinearSchedule = deepcopy(self.schedule)

        filledSchedule.set_scheduleSlots(randomPersonOrder)
        return filledSchedule
