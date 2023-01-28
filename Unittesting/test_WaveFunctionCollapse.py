import unittest
import datetime

from Datatypes.Person import Person
from Datatypes.Job import Job
from Datatypes.Schedules.LinearSchedule import LinearSchedule

from ScheduleGenerators.LinearScheduleGenerators.LinearScheduleGenerators import fit_range

from JobScheduler.WaveFuncCollapseScheduler import WaveFuncCollapseScheduler


class MyTestCase(unittest.TestCase):
    def setUp(self):
        nameStrList = ["JonathanFonteyn", "WoutDeSmit", "LiesbethPoppe", "ThorClaessens", "VincentJacobs",
                       "MichaelSchoenmakers", "BryanVanhoudt", "RobbeGevers", "WoutSaenen", "AnneMarieDeLaet",
                       "JarneArnouts", "MichielVercauteren", "YorbenJoosen", "RobbeDeHelt", "BjornLahey", "LiesHornikx",
                       "JorreBeyltiens", "JonasVerburgh", "WannesBrusselmans", "CyrianneMintiens"]
        self.personList = tuple([Person(nameStr) for nameStr in nameStrList])

    def test_linear_WaveFunctionCollapse(self):
        startTime = datetime.datetime(2023, 1, 30, hour=12)
        endTime = datetime.datetime(2023, 3, 22, hour=12)
        job = Job("Socialmedia")
        timeRange = fit_range(startTime=startTime, endTime=endTime, actionCount=len(self.personList))
        linearSchedule = LinearSchedule.from_empty(job=job,
                                                   slotDates=timeRange,
                                                   personVector=self.personList)
        generator = WaveFuncCollapseScheduler(linearSchedule)
        fittedSchedule = generator.fill_schedule()
        print(fittedSchedule)


if __name__ == '__main__':
    unittest.main()
