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

    def test_linear_constructor(self):
        startTime = datetime.datetime(2023, 1, 26, 20)
        timeDelta = datetime.timedelta(hours=1)
        timeSlots = generate_timerange(startTime, timeDelta, 10)
        linearSchedule = LinearSchedule(personVector=self.personList, job=self.jobList[0], slotDates=timeSlots, scheduleSlots=[-1 for _ in range(len(timeSlots))])
        multiSchedule = MultiSchedule.from_linear(linearSchedule)
        self.assertIsNotNone(multiSchedule)

    def test_simple_summation(self):
        startTime = datetime.datetime(2023, 1, 30)
        job = Job("Socialmedia")
        linearSchedule = LinearSchedule.from_empty(job=job,
                                                   slotDates=generate_timerange(startTime, datetime.timedelta(days=1), 10),
                                                   personVector=self.personList)
        multiSchedule = MultiSchedule.from_linear(linearSchedule)
        multiSchedule += linearSchedule
        #print(multiSchedule)

    def test_sample_scheduler(self):
        startTime = datetime.datetime(2023, 1, 30)
        job = Job("Share on FB")
        linearSchedule = LinearSchedule.from_empty(job=job,
                                                   slotDates=generate_timerange(startTime, datetime.timedelta(days=1), 10),
                                                   personVector=self.personList)
        print(linearSchedule)

        multiSchedule = MultiSchedule.from_linear(linearSchedule)
        job2 = Job("Share on FB")
        linearSchedule.set_job(job2)
        multiSchedule += linearSchedule
        print(multiSchedule)

        jobScheduler = SampleJobScheduler(multiSchedule)
        filledSchedule = jobScheduler.fill_schedule()
        print(filledSchedule)


if __name__ == '__main__':
    unittest.main()
