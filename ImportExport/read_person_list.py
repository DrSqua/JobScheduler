from Datatypes.Person import Person


def read_person_list(filepath: str) -> list[Person]:
    personList: list[Person] = []
    with open(filepath) as textFile:
        for personName in textFile:
            personList.append(Person(personName.strip()))

    return personList
