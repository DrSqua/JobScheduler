from abc import ABC


class DistributionParameters(ABC):
    def __init__(self, personCount):
        self.personCount = personCount

    def get_actions_per_person(self):
        pass

    def get_total_actions(self):
        pass


class LinearDistributionParameters(DistributionParameters):
    def __init__(self, personCount, totalActions, actionsPerPerson):
        super(LinearDistributionParameters, self).__init__(personCount=personCount)
        self.totalActions = totalActions
        self.actionsPerPerson = actionsPerPerson

    @classmethod
    def from_totalactions(cls, personCount, totalActions):
        actionsPerPerson = totalActions//personCount
        return cls(personCount, totalActions, actionsPerPerson)

    @classmethod
    def from_actionperperson(cls, personCount, actionsPerPerson):
        totalActions = personCount*actionsPerPerson
        return cls(personCount, totalActions, actionsPerPerson)

    def get_actions_per_person(self):
        return self.actionsPerPerson

    def get_total_actions(self):
        return self.totalActions
