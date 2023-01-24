from random import sample
from copy import deepcopy

from JobScheduler.JobSchedulingAgent import JobSchedulingAgent
from Datatypes.Schedules.LinearSchedule import LinearSchedule


class LinearRandomJobScheduler(JobSchedulingAgent):
    def __init__(self, startingSchedule: LinearSchedule):
        super().__init__(startingSchedule)

    def fill_schedule(self, checkAvailability: bool = False):
        randomPersonOrder = sample(self.personVector, self.schedule.get_slotCount())
        filledSchedule: LinearSchedule = deepcopy(self.schedule)

        filledSchedule.set_scheduleSlots(randomPersonOrder)
        return filledSchedule
