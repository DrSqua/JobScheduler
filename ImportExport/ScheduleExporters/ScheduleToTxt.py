class ScheduleToText:
    @staticmethod
    def schedule_to_txt(schedule, fileName: str):
        print(f"Writing to {fileName}")
        with open(fileName, "w") as file:
            file.write(schedule.__str__())
