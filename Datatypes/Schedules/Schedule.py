from typing import Union

from Datatypes.Person import Person


class Schedule:
    def __init__(self, scheduleSlots: list[Union[None, Person]]):
        self.scheduleSlots: list[Union[None, Person]] = scheduleSlots
