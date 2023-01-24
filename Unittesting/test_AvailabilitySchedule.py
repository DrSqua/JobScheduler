import datetime
import unittest

from Datatypes.AvailabilitySchedule import AvailabilitySchedule


class TestAvailabilitySchedule(unittest.TestCase):
    def setUp(self):
        self.datesToCheck = [datetime.datetime.now()]

        self.availabilitySchedule1 = AvailabilitySchedule()

        availabilityToggleDates = [datetime.datetime(2023, 1, 20), datetime.datetime(2023, 1, 28)]
        self.availabilitySchedule2 = AvailabilitySchedule(availabilityToggleDates)

        togglesAreAvailable = False
        self.availabilitySchedule3 = AvailabilitySchedule(availabilityToggleDates, togglesAreAvailable)

    def test_inputExists(self):
        """
        Tests constructors
        """
        self.assertIsNotNone(self.availabilitySchedule1)
        self.assertIsNotNone(self.availabilitySchedule2)  # With one argument
        self.assertIsNotNone(self.availabilitySchedule3)  # With two arguments

    def test_togglesAreAvailable(self):
        """
        Test if the togglesAreAvailable variable and all methods related to it are working
        """
        self.assertTrue(self.availabilitySchedule2.is_available(datetime.datetime(2023, 1, 20)))

        self.availabilitySchedule2.set_togglesAreAvailable(False)
        self.assertFalse(self.availabilitySchedule2.is_available(datetime.datetime(2023, 1, 20)))
        self.availabilitySchedule2.flip_togglesAreAvailable()

        self.assertTrue(self.availabilitySchedule2.is_available(datetime.datetime(2023, 1, 20)))

    def test_emptyAvailable(self):
        for date in self.datesToCheck:
            self.assertTrue(self.availabilitySchedule1.is_available(date))

    def test_nonAvailable(self):
        """
        Testing the nonAvailable method
        :return:
        """
        self.assertFalse(self.availabilitySchedule2.is_available(datetime.datetime(2023, 1, 22)))

    def test_inserting_available(self):
        availabilitySchedule = AvailabilitySchedule([datetime.datetime(2023, 1, 20), datetime.datetime(2023, 1, 28)])
        availabilitySchedule.insert_availablePeriod(datetime.datetime(2023, 1, 18), datetime.datetime(2023, 1, 30))
        self.assertTrue(availabilitySchedule.is_available(datetime.datetime(2023, 1, 24)))

        availabilitySchedule = AvailabilitySchedule([datetime.datetime(2023, 1, 20), datetime.datetime(2023, 1, 28)])
        availabilitySchedule.insert_availablePeriod(datetime.datetime(2023, 1, 22), datetime.datetime(2023, 1, 26))
        self.assertTrue(availabilitySchedule.is_available(datetime.datetime(2023, 1, 24)))


if __name__ == "__main__":
    unittest.main()
