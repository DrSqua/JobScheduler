from random import sample
from copy import deepcopy

from JobScheduler.JobSchedulingAgent import JobSchedulingAgent
from Datatypes.Schedules.LinearSchedule import LinearSchedule


class WaveFuncCollapseScheduler(JobSchedulingAgent):
    def __init__(self, startingSchedule):
        super().__init__(startingSchedule)

    def fill_schedule(self, checkAvailability: bool = False):
        scheduleAvailabilityList: list = []
        loopCount = 0

        while not self.schedule.is_filled():
            loopCount += 1
            print(f"Running loop {loopCount}")

            for slotIndex, slot in enumerate(self.schedule.get_slotVector()):
                if slot != -1:
                    scheduleAvailabilityList.append([])
                    continue

                # add available Persons
                slotAvailabilitList: list = []
                startDate, endDate = self.schedule.get_timespan_dates(slotIndex)
                for person in self.schedule.get_personVector():
                    if person.is_available(startDate, endDate):
                        slotAvailabilitList.append(self.schedule.as_personIndex(person))
                scheduleAvailabilityList.append(slotAvailabilitList)

            # Get smallest list
            lenOptions = [len(personList) for personList in scheduleAvailabilityList]
            lenOptions = list(map(lambda x: x if x!=0 else 9999, lenOptions))
            lowestOptions = min(lenOptions)
            slotWithLowestOptionsIndex = lenOptions.index(lowestOptions)
            listWithSmallestOptions = scheduleAvailabilityList[slotWithLowestOptionsIndex]
            choice = sample(listWithSmallestOptions, 1)[0]
            self.schedule.set_person(slotIndex=slotWithLowestOptionsIndex, personIndex=choice)
            scheduleAvailabilityList.clear()
        return self.schedule


