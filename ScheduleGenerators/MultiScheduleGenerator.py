import datetime

from Datatypes.Person import Person
from Datatypes.Job import Job


class MultiScheduleGenerator:
    def __init__(self, personVector: tuple[Person], jobVector: tuple[Job]):
        self.personVector = personVector
        self.jobVector = jobVector

    def fill_full_schedule(self, startTime: datetime.datetime, endTime: datetime.datetime):
        durations = [job.jobDuration for job in self.jobVector]
        smallestDuration = min(durations)
        indexOfSmallest = durations.index(smallestDuration)
        print(durations[0] // durations[1])
