from abc import ABC

from Datatypes.Person import Person


class JobSchedulingAgent(ABC):
    def __init__(self, schedule):
        self.schedule = schedule
        self.personVector: tuple[Person] = schedule.get_personVector()

    def fill_schedule(self):
        pass
