import datetime
import unittest

from Datatypes.Schedules.LinearSchedule import LinearSchedule
from Datatypes.Schedules.MultiSchedule import MultiSchedule
from Datatypes.Person import Person
from Datatypes.Job import Job

from ScheduleGenerators.DateRangeGeneratorFunctions.TimeRangeGenerator import generate_timerange


class TestMultiSchedule(unittest.TestCase):
    def setUp(self):
        nameStrList = ["JonathanFonteyn", "WoutDeSmit", "LiesbethPoppe", "ThorClaessens", "VincentJacobs", "MichaelSchoenmakers", "BryanVanhoudt", "RobbeGevers", "WoutSaenen", "AnneMarieDeLaet", "JarneArnouts",        "MichielVercauteren",        "YorbenJoosen",        "RobbeDeHelt",        "BjornLahey",        "LiesHornikx",        "JorreBeyltiens",        "JonasVerburgh","WannesBrusselmans","CyrianneMintiens"]
        self.personList = tuple([Person(nameStr) for nameStr in nameStrList])
        self.jobList = [Job("Event delen"), Job("Winactie delen")]

    def test_constructor(self):
        startTime = datetime.datetime(2023, 1, 26, 20)
        timeDelta = datetime.timedelta(hours=1)
        timeSlots = generate_timerange(startTime, timeDelta, 10)
        linearSchedule = LinearSchedule(personVector=self.personList, job=self.jobList[0], slotDates=timeSlots, scheduleSlots=[-1 for _ in range(len(timeSlots))])
        multiSchedule = MultiSchedule.from_linear(linearSchedule)
        print(multiSchedule)
        self.assertIsNotNone(multiSchedule)


if __name__ == '__main__':
    unittest.main()
