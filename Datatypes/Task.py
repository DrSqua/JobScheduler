import datetime


class Task:
    def __init__(self, taskName: str, jobDuration: datetime.timedelta = datetime.timedelta(1)):
        self.taskName: str = taskName
        self.taskDuration: datetime.timedelta

    def __str__(self):
        return f"{self.taskName}"

    def __repr__(self):
        return self.__str__()
