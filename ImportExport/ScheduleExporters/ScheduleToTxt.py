from functools import singledispatchmethod

from Datatypes.Schedules.LinearSchedule import LinearSchedule
from Datatypes.Schedules.MultiSchedule import MultiSchedule


class ScheduleToText:
    @singledispatchmethod
    @staticmethod
    def schedule_to_txt(schedule, fileName: str):
        pass

    @schedule_to_txt.register
    @staticmethod
    def linear_schedule_to_txt(schedule: LinearSchedule, fileName: str):
        print(f"Writing to {fileName}")

    @schedule_to_txt.register
    @staticmethod
    def multischedule_to_txt(schedule: MultiSchedule, fileName: str):
        pass
