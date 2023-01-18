class Person:
    def __init__(self, name: str):
        self.personName: str = name

    def __str__(self):
        return f"{self.personName}"

    def __repr__(self):
        return self.__str__()
