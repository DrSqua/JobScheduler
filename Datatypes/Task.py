import datetime


class Task:
    def __init__(self, taskName: str, taskSlots: int = 1, jobDuration: datetime.timedelta = datetime.timedelta(1)) -> object:
        """
        Task class, holds all the data of a task which will be performed.

        :param taskName: Name of the task, trivial
        :param taskSlots: How many people can perform one instance of this task at once
        :param jobDuration: How long this job takes. This is independable from the slots
        """
        self.taskName: str = taskName
        self.taskDuration: datetime.timedelta
        self.taskSlots: int = taskSlots

    def __str__(self):
        return f"{self.taskName}"

    def __repr__(self):
        return self.__str__()

    def __format__(self, format_spec):
        return self.taskName

    def get_taskSlots(self) -> int:
        return self.taskSlots
