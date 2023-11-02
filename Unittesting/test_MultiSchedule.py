import datetime
import unittest

from Datatypes.Schedules.LinearSchedule import LinearSchedule
from Datatypes.Schedules.MultiSchedule import MultiSchedule

from Datatypes.Person import Person
from Datatypes.Job import Job
from ImportExport.PersonImporters.read_person_list import read_person_list

from JobScheduler.SampleJobScheduler import SampleJobScheduler
from JobScheduler.WaveFuncCollapseScheduler import WaveFuncCollapseScheduler

from ScheduleGenerators.DateRangeGeneratorFunctions.TimeRangeGenerator import generate_timerange
from ScheduleGenerators.MultiScheduleGenerator import MultiScheduleGenerator


class TestMultiSchedule(unittest.TestCase):
    def setUp(self):
        job = Job("AJob", datetime.timedelta(hours=1))

        timeRangeOne = generate_timerange(datetime.datetime(2023, 2, 1, 13), datetime.timedelta(hours=1), 8)
        timeRangeTwo = generate_timerange(datetime.datetime(2023, 2, 1, 14), datetime.timedelta(hours=1), 8)
        timeRangeThree = generate_timerange(datetime.datetime(2023, 2, 1, 15), datetime.timedelta(hours=1), 8)

        self.personVector = read_person_list("../ImportExport/PersonImporters/PraesidiumNamenlijst.txt")
        self.linearOne = LinearSchedule.from_empty(job=job, slotDates=timeRangeOne, personVector=self.personVector)
        self.linearTwo = LinearSchedule.from_empty(job=job, slotDates=timeRangeTwo, personVector=self.personVector)
        self.linearThree = LinearSchedule.from_empty(job=job, slotDates=timeRangeThree, personVector=self.personVector)

    def test_constructor(self):
        emptyMultiSchedule = MultiSchedule.from_linear(self.linearOne, self.linearTwo, self.linearThree)
        print(emptyMultiSchedule)

if __name__ == '__main__':
    unittest.main()
