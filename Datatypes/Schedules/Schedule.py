from abc import ABC
from typing import Union

from Datatypes.Person import Person


class Schedule(ABC):
    def __init__(self, personVector: tuple[Person], scheduleSlots: list[int]):
        self.personVector: tuple[Person] = personVector
        self.scheduleSlots: list[int] = scheduleSlots

    def to_person(self, personIndex: int):
        if personIndex < 0 or personIndex < len(self.personVector):
            raise ValueError("personIndex must be equal or higher than 0 and smaller than personVector length")

    def to_personIndex(self, person: Person):
