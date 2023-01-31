import datetime
import unittest

from Datatypes.Schedules.LinearSchedule import LinearSchedule
from Datatypes.Schedules.MultiSchedule import MultiSchedule
from Datatypes.Person import Person
from Datatypes.Job import Job

from JobScheduler.SampleJobScheduler import SampleJobScheduler

from ScheduleGenerators.DateRangeGeneratorFunctions.TimeRangeGenerator import generate_timerange
from ScheduleGenerators.MultiScheduleGenerator import MultiScheduleGenerator


class TestMultiSchedule(unittest.TestCase):
    def setUp(self):
        nameStrList = ["JonathanFonteyn", "WoutDeSmit", "LiesbethPoppe", "ThorClaessens", "VincentJacobs", "MichaelSchoenmakers", "BryanVanhoudt", "RobbeGevers", "WoutSaenen", "AnneMarieDeLaet", "JarneArnouts",        "MichielVercauteren",        "YorbenJoosen",        "RobbeDeHelt",        "BjornLahey",        "LiesHornikx",        "JorreBeyltiens",        "JonasVerburgh","WannesBrusselmans","CyrianneMintiens"]
        charList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                         "t", "u", "v", "w", "x", "y", "z"]
        self.personList = tuple([Person(nameStr) for nameStr in nameStrList])
        self.charList = tuple([Person(char) for char in charList])
        self.jobList = tuple([
            Job("Event delen", datetime.timedelta(hours=1)),
            Job("Winactie delen", datetime.timedelta(minutes=30))])

    def test_from_empty(self):
        timeRange = generate_timerange(datetime.datetime(2023, 2, 1, 12), datetime.timedelta(hours=1), 10)
        emptyMulti = MultiSchedule.from_empty(personVector=self.personList,
                                              scheduleSlots=[-1]*len(self.personList)*len(self.jobList),
                                              slotDates=timeRange,
                                              jobVector=self.jobList)
        self.assertIsNotNone(emptyMulti)

    def test_setSlot(self):
        timeRange = generate_timerange(datetime.datetime(2023, 2, 1, 12), datetime.timedelta(hours=1), 10)
        emptyMulti = MultiSchedule.from_empty(personVector=self.personList,
                                              scheduleSlots=[-1] * len(self.personList) * len(self.jobList),
                                              slotDates=timeRange,
                                              jobVector=self.jobList)
        namen = "RobbeDeHelt", "JorreBeyltiens"
        index1, index2 = [person.personName for person in self.personList].index(namen[0]), [person.personName for person in self.personList].index(namen[1])

        emptyMulti[0, 0] = index1
        emptyMulti[0, 1] = index2
        print(emptyMulti)

    def test_getitem(self):
        pass


if __name__ == '__main__':
    unittest.main()
