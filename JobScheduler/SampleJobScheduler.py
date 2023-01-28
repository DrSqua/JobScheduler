from random import sample
from copy import deepcopy

from JobScheduler.JobSchedulingAgent import JobSchedulingAgent


class SampleJobScheduler(JobSchedulingAgent):
    def __init__(self, startingSchedule):
        super().__init__(startingSchedule)

    def fill_schedule(self, checkAvailability: bool = False):
        randomPersonOrder = sample(self.personVector, self.schedule.get_slotCount())
        filledSchedule = deepcopy(self.schedule)

        filledSchedule.set_slotMatrix(randomPersonOrder)
        return filledSchedule
