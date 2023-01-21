import datetime


class Job:
    def __init__(self, JobName: str, jobDuration: datetime.timedelta = datetime.timedelta(1)):
        """
        Job class, holds all the data of a Job which will be performed.

        :param JobName: Name of the Job, trivial
        :param jobDuration: How long this job takes. This is independable from the slots
        """
        self.JobName: str = JobName
        self.JobDuration: datetime.timedelta

    def __str__(self):
        return f"{self.JobName}"

    def __repr__(self):
        return self.__str__()

    def __format__(self, format_spec):
        return self.JobName
