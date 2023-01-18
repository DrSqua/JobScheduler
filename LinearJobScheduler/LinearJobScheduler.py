import datetime
from random import sample

from Datatypes.Task import Task
from Datatypes.Person import Person
from Datatypes.DistributionParemeters import LinearDistributionParameters
from ScheduleRangeGenerator.LinearScheduleGenerator import generate_calender_totalactionbase


class LinearJobScheduler:
    def __init__(self, personList: list[Person]):
        self.personList = personList

    def schedule_single_task(self, endDate: datetime.date,
                             task: Task,
                             distParam: LinearDistributionParameters,
                             startDate: datetime.date = datetime.date.today()):

        actionCount = distParam.get_total_actions()
        linearEmptySchedule = generate_calender_totalactionbase(endDate=endDate, actionCount=actionCount, startDate=startDate)

        return zip(linearEmptySchedule, sample(self.personList, len(self.personList)))
