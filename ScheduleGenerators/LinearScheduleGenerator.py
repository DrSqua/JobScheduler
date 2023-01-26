import datetime

from Datatypes.Schedules.LinearSchedule import LinearSchedule
from Datatypes.Job import Job
from Datatypes.Person import Person
from ScheduleGenerators.ScheduleGenerator import ScheduleGenerator

from ScheduleGenerators.DateRangeGeneratorFunctions.DateRangeGeneratorFunctions import \
    generate_from_total_actions, generate_from_unbound_frequency, generate_from_bound_frequency


class LinearScheduleGenerator(ScheduleGenerator):
    """LinearScheduleGenerator"""

    def __init__(self, personVector: tuple[Person], job: Job):
        self.job = job
        self.personVector = personVector

    def generate_from_totalActions(self,
                                   endDate: datetime.datetime,
                                   actionCount: int,
                                   startDate: datetime.date = datetime.datetime.today(),
                                   fitToEndDate: bool = True) -> LinearSchedule:
        """
        Creates schedule using a range of dates, fitted to a set interval which fits in the given date range
        :param actionCount: A 'action' occurs when the job is preformed by a person
        :param endDate: proposed endDate
        :param startDate: proposed startDate
        :param fitToEndDate: The dateRange is possibly concattenated to fit the required count
               This parameter defines which of the supplied dates should always be included in the final dateRange
        :return:
        """
        return LinearSchedule.from_empty(personVector=self.personVector, job=self.job,
                                         slotDates=generate_from_total_actions(
                                             endDate, actionCount, startDate, fitToEndDate))

    def generate_from_bound_frequency(self,
                                      endDate: datetime.datetime,
                                      actionFrequency: int,
                                      startDate: datetime.datetime = datetime.datetime.today(),
                                      fitToEndDate: bool = True
                                      ):
        """
        Creates schedule using a range of dates, fitted to a set interval which fits in the given date range
        :param endDate:
        :param actionFrequency:
        :param startDate:
        :param fitToEndDate:
        :return:
        """
        return LinearSchedule.from_empty(personVector=self.personVector, job=self.job,
                                         slotDates=generate_from_bound_frequency(
                                             endDate, actionFrequency, startDate, fitToEndDate))

    def generate_from_unbound_frequency(self,
                                        beginDate: datetime.datetime,
                                        actionCount: int,
                                        actionFrequency: int,
                                        fitAsEndDate: bool = False
                                        ):
        """
        Creates schedule using a range of dates, fitted to a beginDate and endDate,
        the latter which is defined by amount of actions a frequency
        :param beginDate: Date from where the range will start/end counting
        :param actionCount: How many times the frequency will be called
        :param actionFrequency: How many days between the different actions
        :param fitAsEndDate: If 'beginDate' is to be treated as the endDate of the date range
        :return:
        """
        return LinearSchedule.from_empty(personVector=self.personVector, job=self.job,
                                         slotDates=generate_from_unbound_frequency(
                                             beginDate, actionCount, actionFrequency, fitAsEndDate))
