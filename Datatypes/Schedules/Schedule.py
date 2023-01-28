import datetime
from typing import Union

from Datatypes.Person import Person
from Datatypes.Job import Job


class Schedule:
    def __init__(self,
                 personVector: tuple[Person],
                 jobVector: tuple[Job],
                 slotDates: tuple[Union[datetime.datetime, datetime.date]],
                 scheduleSlots: list[int]):
        if len(slotDates) == 0:
            raise ValueError("slotDates can not be 0")

        self.personVector: tuple[Person] = personVector  # Als person objects which can be used to fill the schedule
        self.jobVector: tuple[Job] = jobVector  # All job objects which are also the indices of the 'column's
        self.slotDateVector: tuple[datetime.datetime] = slotDates   # Rows of the schedule. Indicate the startdate for a slot
        self.scheduleSlots: list[int] = scheduleSlots  # -2 is not available, -1 is empty, 0->n is personIndex
# -----------------------------------------------------------------

    def is_valid_personIndex(self, personIndex: int) -> bool:
        return 0 <= personIndex and personIndex < len(self.personVector)

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
        """
        Translates a personIndex to the personObject
        If we get a '-1' or 'not filled' index we return None
        :param personIndex: index of person in the personVector
        :return:
        """
        if personIndex == -1:
            return None
        if personIndex < 0 or len(self.personVector) < personIndex:
            raise ValueError("personIndex must be equal or higher than 0 and smaller than personVector length")
        return self.personVector[personIndex]

    def as_personIndex(self, person: Person) -> int:
        """
        Returns the personIndex in the personVector of the input person Object
        We match with '__eq__' method
        :param person:
        :return:
        """
        if not person:
            return -1
        if person not in self.personVector:
            raise ValueError("First add a Person with add_person() before getting the ID")
        return self.personVector.index(person)

    def get_personVector(self) -> tuple[Person]:
        return self.personVector

    def set_personVector(self, personVector: tuple[Person]):
        pass

    def rebase_personVector(self, newPersonVector: tuple[Person]):
        pass
# -----------------------------------------------------------------

    def set_slot(self, slotIndex: int, slotValue: Union[int, Person]):
        if isinstance(slotValue, Person):
            slotValue = self.as_personIndex(slotValue)
        if not isinstance(slotValue, int):
            raise ValueError("slotValue has to be passed as personIndex or person instance")
        if not self.is_valid_personIndex(slotValue):
            raise ValueError("personIndex is not valid")
        if self.is_valid_slotIndex(slotIndex):
            raise ValueError("slotIndex is not valid")
        self.scheduleSlots[slotIndex] = slotValue

    def set_slotMatrix(self, scheduleSlots: Union[list[Person], list[int]]) -> None:
        if isinstance(scheduleSlots[0], Person):
            scheduleSlots = [self.as_personIndex(person) for person in scheduleSlots]

        if any(not self.is_valid_personIndex(personIndex) or personIndex == -1 or personIndex == -2 for personIndex in scheduleSlots):
            raise ValueError("all input scheduleSlots must be valid personIndices, empty or nonFill")
        if len(self.scheduleSlots) != len(scheduleSlots):
            raise ValueError("instance scheduleSlots and input scheduleSlots must have the same length")
        self.scheduleSlots = scheduleSlots

    def get_slot(self, slotIndex: int, **kwargs) -> int:
        return self.scheduleSlots[slotIndex]

    def get_slot_asPerson(self, slotIndex: int) -> Person:
        return self.as_person(self.get_slot(slotIndex=slotIndex))

    def get_slotMatrix(self, **kwargs,):
        return self.scheduleSlots

    def get_slotVector_as_person(self) -> list[Union[None, Person]]:
        """
        Returns the full slotVector but with Person objects emplaced
        :return:
        """
        return [self.as_person(personIndex=personIndex) for personIndex in self.get_slotMatrix()]

    def get_slotCount(self) -> int:
        return len(self.scheduleSlots)

    def is_valid_slotIndex(self, slotIndex: int) -> bool:
        if not (slotIndex < 0 | len(self.slotDateVector) < slotIndex):
            return False
        return self.scheduleSlots[slotIndex] != -2
# -----------------------------------------------------------------

    def get_slotDateVector(self):
        """
        Returns the slotDateVector
        :return:
        """
        return self.slotDateVector
# -----------------------------------------------------------------

    def is_filled(self) -> bool:
        """
        Checks all slots in the scheduleSlot vector for a '-1' value, which means 'to be filled'
        If there is no 'to be filled' slot then we can return True, else we return False
        :return:
        """
        return not any(value == -1 for value in self.scheduleSlots)

    def get_timespan_dates(self, slotIndex, jobIndex=0):
        # TODO
        return datetime.datetime.today(), datetime.datetime.today()
