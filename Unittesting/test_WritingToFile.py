import unittest
import datetime

from Datatypes.Person import Person
from Datatypes.Job import Job
from Datatypes.Schedules.LinearSchedule import LinearSchedule
from Datatypes.Schedules.MultiSchedule import MultiSchedule

from ImportExport.PersonImporters.read_person_list import read_person_list

from ScheduleGenerators.LinearScheduleGenerators.LinearScheduleGenerators import fit_range

from JobScheduler.WaveFuncCollapseScheduler import WaveFuncCollapseScheduler

from ImportExport.ScheduleExporters.ScheduleToTxt import ScheduleToText


class TestWritingToTXT(unittest.TestCase):
    def setUp(self):
        self.personList = read_person_list("../ImportExport/PersonImporters/PraesidiumEnEducationNamenlijst.txt")
        startTime = datetime.datetime(2023, 1, 30, hour=12)
        endTime = datetime.datetime(2023, 3, 22, hour=12)
        job = Job("Socialmedia")
        timeRange = fit_range(startTime=startTime, endTime=endTime, actionCount=len(self.personList))
        linearSchedule = LinearSchedule.from_empty(job=job,
                                                   slotDates=timeRange,
                                                   personVector=self.personList)
        generator = WaveFuncCollapseScheduler(linearSchedule)
        self.fittedLinearSchedule = generator.fill_schedule()

    def test_writeLinearToFile(self):
        ScheduleToText.schedule_to_txt(self.fittedLinearSchedule, "test_linearToTXT.txt")

    def test_writeMultiToFile(self):
        startTime = datetime.datetime(2023, 1, 30, hour=12)
        endTime = datetime.datetime(2023, 3, 22, hour=12)
        job = Job("Post op FB")
        timeRange = fit_range(startTime=startTime, endTime=endTime, actionCount=len(self.personList)//2)
        linearSchedule = LinearSchedule.from_empty(job=job,
                                                   slotDates=timeRange,
                                                   personVector=self.personList)
        multiSchedule = MultiSchedule.from_linear(linearSchedule) + linearSchedule

        generator = WaveFuncCollapseScheduler(multiSchedule)
        fittedSchedule = generator.fill_schedule()

        ScheduleToText.schedule_to_txt(fittedSchedule, "test_MultiToTXT.txt")


if __name__ == '__main__':
    unittest.main()
