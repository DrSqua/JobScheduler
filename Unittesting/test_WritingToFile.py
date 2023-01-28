import unittest
import datetime

from Datatypes.Person import Person
from Datatypes.Job import Job
from Datatypes.Schedules.LinearSchedule import LinearSchedule

from ScheduleGenerators.LinearScheduleGenerators.LinearScheduleGenerators import fit_range

from JobScheduler.WaveFuncCollapseScheduler import WaveFuncCollapseScheduler

from ImportExport.ScheduleExporters.ScheduleToTxt import ScheduleToText

class TestWritingToTXT(unittest.TestCase):
    def setUp(self):
        nameStrList = ["JonathanFonteyn", "WoutDeSmit", "LiesbethPoppe", "ThorClaessens", "VincentJacobs",
                       "MichaelSchoenmakers", "BryanVanhoudt", "RobbeGevers", "WoutSaenen", "AnneMarieDeLaet",
                       "JarneArnouts", "MichielVercauteren", "YorbenJoosen", "RobbeDeHelt", "BjornLahey", "LiesHornikx",
                       "JorreBeyltiens", "JonasVerburgh", "WannesBrusselmans", "CyrianneMintiens"]
        self.personList = tuple([Person(nameStr) for nameStr in nameStrList])
        startTime = datetime.datetime(2023, 1, 30, hour=12)
        endTime = datetime.datetime(2023, 3, 22, hour=12)
        job = Job("Socialmedia")
        timeRange = fit_range(startTime=startTime, endTime=endTime, actionCount=len(self.personList))
        linearSchedule = LinearSchedule.from_empty(job=job,
                                                   slotDates=timeRange,
                                                   personVector=self.personList)
        generator = WaveFuncCollapseScheduler(linearSchedule)
        self.fittedLinearSchedule = generator.fill_schedule()

    def test_writeToFile(self):
        ScheduleToText.schedule_to_txt(self.fittedLinearSchedule, "test_linearToTXT.txt")



if __name__ == '__main__':
    unittest.main()
