import datetime
from typing import Union, Callable
from functools import singledispatch
import abc
from collections import abc

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
        self.slotDateVector: tuple[
            datetime.datetime] = slotDates  # Rows of the schedule. Indicate the startdate for a slot
        self.slotRowCount = len(self.slotDateVector)
        self.slotVector: list[int] = scheduleSlots  # -2 is not available, -1 is empty, 0->n is personIndex

    @singledispatch
    def __getitem__(self, argument: Union[int, Callable[[int], bool]], jobIndex: int = None) -> Union[int, list[int]]:
        """
        Returns either the filled personIndex, not filled or non valid
        :param slotIndex:
        :param jobIndex:
        :return:
        """

    def __get_slot__(self, slotIndex: int, jobIndex: int = None) -> int:
        """
        Returns the value of a given slotIndex
        If supplied, jobIndex
        :param slotIndex:
        :param jobIndex:
        :return:
        """
        if jobIndex is None:
            if not self.is_valid_slotIndex(slotIndex):
                raise ValueError("slotIndex must be valid")
            return self.slotVector[slotIndex]
        if not self.is_valid_slotIndex(slotIndex=slotIndex, jobIndex=jobIndex):
            raise ValueError(f"slotIndex {slotIndex} is not valid")
        return self.slotVector[slotIndex + jobIndex * self.slotRowCount]

    @__getitem__.register
    def _(self, argument: int, jobIndex: int = None) -> int:
        slotIndex = argument
        if not self.is_valid_slotIndex(slotIndex):
            raise ValueError("slotIndex must be valid")
        if jobIndex is None:
            return self.__get_slot__(slotIndex=slotIndex)
        return self.__get_slot__(slotIndex=slotIndex, jobIndex=jobIndex)

    def __get__selection(self, operator: Callable[[int], bool], jobIndex: int = None) -> list:
        unfiltered = self.get_slotVector(jobIndex=jobIndex)
        return [personIndex for personIndex in unfiltered if operator(personIndex)]

    @__getitem__.register
    def _(self, argument: abc.Callable, jobIndex: int = None) -> list[int]:
        return self.__get__selection(operator=argument, jobIndex=jobIndex)

    # person and personIndex methods----------------------------------------------------------------
    def is_existing_personIndex(self, personIndex: int) -> bool:
        """
        Returns True if the personIndex is of a person in the personVector
        :param personIndex:
        :return:
        """
        return 0 <= personIndex < len(self.personVector)

    def is_valid_personIndex(self, personIndex: int) -> bool:
        """
        If the personIndex is a valid index. Either it exists, is not filled (-1) or is not to be filled (-2)
        :param personIndex:
        :return:
        """
        if personIndex == -2 or personIndex == -1:
            return True
        if self.is_existing_personIndex(personIndex):
            return True
        return False

    def add_person(self, person: Person) -> None:
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
        if self.is_existing_personIndex(personIndex):
            return self.personVector[personIndex]
        if self.is_valid_personIndex(personIndex):
            return None
        raise ValueError("personIndex must either be valid and not existing")

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

    # personVector-----------------------------------------------------------------
    def get_personVector(self) -> tuple[Person]:
        return self.personVector

    def set_personVector(self, personVector: tuple[Person]):
        self.personVector = personVector

    # job and jobIndex-----------------------------------------------------------------
    def is_valid_jobIndex(self, jobIndex: int) -> bool:
        return 0 <= jobIndex < len(self.jobVector)

    def as_job(self, jobIndex: int) -> Job:
        if not self.is_valid_jobIndex(jobIndex=jobIndex):
            raise ValueError("jobIndex has to be 0 and jobVector length")
        return self.jobVector[jobIndex]

    def as_jobIndex(self, job: Job) -> int:
        if job not in self.jobVector:
            raise ValueError("first add a job to the schedule before requesting the jobIndex")
        return self.jobVector.index(job)

    # slot-----------------------------------------------------------------
    def set_slot(self, slotIndex: int, slotValue: Union[int, Person]):
        if isinstance(slotValue, Person):
            slotValue = self.as_personIndex(slotValue)
        if not isinstance(slotValue, int):
            raise ValueError("slotValue has to be passed as personIndex or person instance")
        if not self.is_existing_personIndex(slotValue):
            raise ValueError("personIndex is not valid")
        if not self.is_valid_slotIndex(slotIndex):
            raise ValueError("slotIndex is not valid")
        self.slotVector[slotIndex] = slotValue

    def get_slot(self, slotIndex: int, jobIndex: int = None) -> Person:
        """
        Passes slotIndex and jobIndex to get_slot and then as_person functions
        :param slotIndex:
        :param jobIndex:
        :return:
        """
        return self.as_person(self.__get_slot__(slotIndex, jobIndex))

    # slotMatrix and vector-----------------------------------------------------------------
    def is_valid_slotIndex(self, slotIndex: int, jobIndex: int = None) -> bool:
        if jobIndex is None:
            return 0 <= slotIndex < self.slotRowCount * len(self.jobVector)
        return 0 <= slotIndex < self.slotRowCount

    def get_slotCount(self) -> int:
        return len(self.slotVector)

    def get_slotVector(self, jobIndex: int = None):
        """
        Returns slots
        :param jobIndex:
        :return:
        """
        if not jobIndex:
            return self.slotVector
        if not self.is_valid_jobIndex(jobIndex=jobIndex):
            raise ValueError("jobIndex is invalid")
        return self.slotVector[self.slotRowCount:(self.slotRowCount * jobIndex)]

    def get_slotVector_as_person(self) -> list[Union[None, Person]]:
        """
        Returns the full slotVector but with Person objects emplaced
        :return:
        """
        return [self.as_person(personIndex=personIndex) for personIndex in self.get_slotVector()]

    def set_slotVector(self, scheduleSlots: Union[list[Person], list[int]]) -> None:
        """

        :param scheduleSlots:
        :return:
        """
        if isinstance(scheduleSlots[0], Person):
            scheduleSlots = [self.as_personIndex(person) for person in scheduleSlots]

        if any(not self.is_valid_personIndex(personIndex) for personIndex in scheduleSlots):
            raise ValueError("all input scheduleSlots must be valid personIndices, empty or nonFill")
        if len(self.slotVector) != len(scheduleSlots):
            raise ValueError("instance scheduleSlots and input scheduleSlots must have the same length")
        self.slotVector = scheduleSlots

    # slotDateVector-----------------------------------------------------------------
    def get_slotDateVector(self):
        """
        Returns the slotDateVector
        :return:
        """
        return self.slotDateVector

    # extra operations-----------------------------------------------------------------
    def swap_slots(self, slotIndexA, slotIndexB):
        if not (self.is_valid_slotIndex(slotIndexA) and self.is_valid_slotIndex(slotIndexB)):
            raise ValueError("Two valid slotindices are required")
        self.slotVector[slotIndexA], self.slotVector[slotIndexB] = self.slotVector[slotIndexB], \
                                                                   self.slotVector[slotIndexA]

    def is_filled(self) -> bool:
        """
        Checks all slots in the scheduleSlot vector for a '-1' value, which means 'to be filled'
        If there is no 'to be filled' slot then we can return True, else we return False
        :return:
        """
        return not any(value == -1 for value in self.slotVector)

    def get_timespan_dates(self, slotIndex, jobIndex=0):
        # TODO
        return datetime.datetime.today(), datetime.datetime.today()
