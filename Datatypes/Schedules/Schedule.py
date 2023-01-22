from abc import ABC
from typing import Union

from Datatypes.Person import Person


class Schedule(ABC):
    def __init__(self, personVector: tuple[Person], scheduleSlots: list[int]):
        self.personVector: tuple[Person] = personVector
        self.scheduleSlots: list[int] = scheduleSlots

    def add_person(self, person) -> None:
        """
        Adds a new person to the personVector
        Method to be avoided as it reinitializes the tuple
        :param person:
        :return: None
        """
        if person not in self.personVector:
            self.personVector += person

    def as_person(self, personIndex: int) -> Union[None, Person]:
        if personIndex == -1:
            return None
        if personIndex < 0 or len(self.personVector) < personIndex:
            raise ValueError("personIndex must be equal or higher than 0 and smaller than personVector length")
        return self.personVector[personIndex]

    def as_personIndex(self, person: Person) -> int:
        if not person:
            return -1
        if person not in self.personVector:
            raise ValueError("First add a Person with add_person() before getting the ID")
        return self.personVector.index(person)

    def get_personVector(self) -> tuple[Person]:
        return self.personVector
