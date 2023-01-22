from typing import cast

from Datatypes.Person import Person


def read_person_list(filepath: str) -> tuple[Person]:
    personList: list[Person] = []
    with open(filepath) as textFile:
        for personName in textFile:
            personList.append(Person(personName.strip()))

    return cast(tuple[Person], personList)
