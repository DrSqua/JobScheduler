import datetime


class Task:
    def __init__(self, taskName: str, jobDuration: datetime.timedelta = datetime.timedelta(1)):
        self.taskName: str = taskName
        self.taskDuration: datetime.timedelta
