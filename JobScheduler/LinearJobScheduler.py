from random import sample
from copy import deepcopy

from Datatypes.Schedules.LinearSchedule import LinearSchedule


class LinearJobScheduler:
    def __init__(self, startingSchedule: LinearSchedule):
        self.personVector = startingSchedule.get_personVector()
        self.schedule: LinearSchedule = startingSchedule

    def fill_schedule(self):
        randomPersonOrder = sample(self.personVector, self.schedule.get_slotCount())
        filledSchedule: LinearSchedule = deepcopy(self.schedule)

        filledSchedule.set_scheduleSlots(randomPersonOrder)
        return filledSchedule
