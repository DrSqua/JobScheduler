import datetime


class Task:
    def __init__(self, taskName: str, jobDuration: datetime.timedelta = datetime.timedelta(1)):
        """
        Task class, holds all the data of a task which will be performed.

        :param taskName: Name of the task, trivial
        :param jobDuration: How long this job takes. This is independable from the slots
        """
        self.taskName: str = taskName
        self.taskDuration: datetime.timedelta

    def __str__(self):
        return f"{self.taskName}"

    def __repr__(self):
        return self.__str__()

    def __format__(self, format_spec):
        return self.taskName
