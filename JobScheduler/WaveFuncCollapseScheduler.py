from random import sample
from copy import deepcopy

from JobScheduler.JobSchedulingAgent import JobSchedulingAgent


class WaveFuncCollapseScheduler(JobSchedulingAgent):
    def __init__(self, startingSchedule):
        super().__init__(startingSchedule)

    def get_options(self, checkSchedule=False) -> list[int]:
        usedValues = []
        if checkSchedule:
            usedValues = list(filter(lambda n: n not in {-1, -2}, self.schedule.get_slotVector()))
        data = [self.schedule.as_personIndex(person) for person in self.schedule.get_personVector() if self.schedule.as_personIndex(person) not in usedValues]
        return data

    def fill_schedule(self):
        scheduleAvailabilityList: list = []
        schedule = deepcopy(self.schedule)

        unusedOptions: list[int] = self.get_options(checkSchedule=True)

        while not schedule.is_filled():
            if not unusedOptions:
                unusedOptions = self.get_options()

            for slotIndex, slot in enumerate(schedule.get_slotVector()):
                # Check if slot has to be filled
                if slot != -1:
                    scheduleAvailabilityList.append([])
                    continue

                # add available Persons for slot
                slotAvailabilitList: list = []
                startDate, endDate = schedule.get_timespan_dates(slotIndex)
                for person in schedule.get_personVector():
                    personIndex = self.schedule.as_personIndex(person)
                    if person.is_available(startDate, endDate) and personIndex in unusedOptions:
                        slotAvailabilitList.append(personIndex)
                scheduleAvailabilityList.append(slotAvailabilitList)

            # Get smallest list
            lenOptions = [len(personList) for personList in scheduleAvailabilityList]
            lenOptions = list(map(lambda x: x if x != 0 else len(self.personVector) + 1, lenOptions))
            lowestOptions = min(lenOptions)
            slotWithLowestOptionsIndex = lenOptions.index(lowestOptions)
            listWithSmallestOptions = scheduleAvailabilityList[slotWithLowestOptionsIndex]

            # Here we choose a random person of the options
            choice: int = sample(listWithSmallestOptions, 1)[0]  # personIndex of the chosen Person
            unusedOptions.pop(unusedOptions.index(choice))
            schedule[slotWithLowestOptionsIndex] = choice
            scheduleAvailabilityList.clear()
        return schedule
