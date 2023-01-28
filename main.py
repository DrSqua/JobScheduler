import time
import datetime

from Datatypes.Person import Person
from Datatypes.Job import Job
from ImportExport.read_person_list import read_person_list

from ScheduleGenerators.LinearScheduleGenerator import LinearScheduleGenerator
from JobScheduler.WaveFuncCollapseScheduler import WaveFuncCollapseScheduler
from JobScheduler.RandomJobScheduler import RandomJobScheduler

from ImportExport.ScheduleExporters.ScheduleToTxt import ScheduleToText

if __name__ == '__main__':
    """
    Basic format for using the spamcalender generator
    """
    saved_time: list = [time.time()]

    print("Setting up variables ...")
    personList: tuple[Person] = read_person_list("ImportExport/PraesidiumNamenlijst.txt")
    job = Job("Delen op socials")

    dateStart = datetime.datetime(2023, 1, 30)
    dateEnd = datetime.datetime(2023, 3, 23)

    print("    Setting up generator ... ", end="")
    generator = LinearScheduleGenerator(personVector=personList, job=job)

    print("Done!")
    print("Finished setup!" + "\n"*2)

    print(f"Running generator ...")
    emptySchedule = generator.generate_from_totalActions(dateEnd, len(personList), dateStart)
    saved_time.append(time.time())
    print(f"Done! {saved_time[-1] - saved_time[-2]}")
    print(emptySchedule)

    print(f"Setting up and running scheduler ...")
    scheduler = RandomJobScheduler(emptySchedule)
    filledSchedule = scheduler.fill_schedule()
    saved_time.append(time.time())
    print(f"Done! {saved_time[-1] - saved_time[-2]}")

    print("Finished running algorithm!" + "\n" * 2)

    print("Ran generator with paramaters:")
    print("Personlist: " + str(personList))
    print("Job: " + str(job))

    print("\n" + "Resulted in this return")
    print(filledSchedule)

    ScheduleToText.schedule_to_txt(filledSchedule, "scheduleOutput.txt")
