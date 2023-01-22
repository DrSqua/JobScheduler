from __future__ import annotations


class Person:
    def __init__(self, name: str):
        self.personName: str = name

    def __str__(self):
        return f"{self.personName}"

    def __repr__(self):
        return self.__str__()

    def __format__(self, format_spec):
        diff: int = int(format_spec)-len(self.personName)
        if diff < 0:
            return self.personName[:len(self.personName)-diff]
        return self.personName + ' '*diff

    def __eq__(self, other: Person):
        if self.personName == other.personName:
            return True
        return False
