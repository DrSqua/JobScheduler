import time
import datetime

from Datatypes.Person import Person
from Datatypes.Task import Task

from LinearJobScheduler.LinearJobScheduler import LinearJobScheduler
from Datatypes.DistributionParemeters import LinearDistributionParameters

if __name__ == '__main__':
    """
    Basic format for using the spamcalender generator
    """
    saved_time: list = [time.time()]

    print("Setting up variables ...")
    personList: list[Person] = [Person("P1"), Person("P2"), Person("P3"), Person("P4"), Person("P5")]
    task = Task("Op Facebook delen")

    dateStart = datetime.datetime(2023, 1, 10)
    dateEnd = datetime.datetime(2023, 1, 20)

    linearParameters = LinearDistributionParameters.from_actionperperson(len(personList), 1)

    print("    Setting up generator ... ", end="")
    generator = LinearJobScheduler(personList)
    print("Done!")

    print("Finished setup!" + "\n"*2)

    print(f"Running generator ...")

    schedule = generator.schedule_single_task(endDate=dateEnd, startDate=dateStart,
                                              task=task,
                                              distParam=linearParameters)

    saved_time.append(time.time())
    print(f"Done! {saved_time[-1] - saved_time[-2]}")

    for date, person, task in schedule:
        print(f"{date} ----> {person} <--- {task}")
    print("Finished running algorithm!" + "\n" * 2)
