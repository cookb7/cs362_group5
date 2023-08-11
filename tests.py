import unittest
import task


class TestCase(unittest.TestCase):

    def test_datetime_1(self):
        """Checks my_datetime for a base case of 0."""
        expected = '01-01-1970'
        self.assertEqual(task.my_datetime(0), expected,
                         msg="A value of 0 does not return 01-01-1970.")

    def test_datetime_2(self):
        """Checks my_datetime that one day in seconds returns 01-02-1970."""
        expected = '01-02-1970'
        num_sec = 86400
        self.assertEqual(task.my_datetime(num_sec), expected,
                         msg="""A value of 86400 seconds or 1 day does not return
                         01-02-1970.""")

    def test_datetime_3(self):
        """Checks my_datetime with a value of one month."""
        expected = '02-01-1970'
        num_sec = 2678400
        self.assertEqual(task.my_datetime(num_sec), expected,
                         msg="""A value of 2678400 or one month does not return
                           02-01-1970.""")

    def test_datetime_4(self):
        """Checks my_datetime with a value of one year."""
        expected = '01-01-1971'
        num_sec = 31536000
        self.assertEqual(task.my_datetime(num_sec), expected,
                         msg="""A value of 31536000 or one year does not return
                           01-01-1971""")

    def test_datetime_5(self):
        """Checks my_datetime with a value of 94608000 or three years to test for
        a leap year. Should return 12-31-1972."""
        expected = '12-31-1972'
        num_sec = 94608000
        self.assertEqual(task.my_datetime(num_sec), expected,
                         msg="Does not account for a leap year.")    

    def test_datetime_6(self):
        """Checks my_datetime with a value of 123456789. Should return 11-29-1973."""
        expected = '11-29-1973'
        num_sec = 123456789
        self.assertEqual(task.my_datetime(num_sec), expected,
                         msg="A value of 123456789 fails to return 11-29-1973")

    def test_datetime_7(self):
        """Checks my_datetime with a value of 9876543210. Should return 12-22-2282."""
        expected = '12-22-2282'
        num_sec = 9876543210
        self.assertEqual(task.my_datetime(num_sec), expected,
                         msg="A value of 9876543210 fails to return 12-22-2282")

    def test_leapyear_1(self):
        """Checks check_leap_year with a value of 1970. Should return False"""
        self.assertFalse(task.check_leap_year(1970), msg="1970 is not a leap year.")

    def test_leapyear_2(self):
        """Checks check_leap_year with a value of 1971. Should return False"""
        self.assertFalse(task.check_leap_year(1971), msg="1971 is not a leap year.")

    def test_leapyear_3(self):
        """Checks check_leap_year with a value of 1972. Should return True"""
        self.assertTrue(task.check_leap_year(1972), msg="1972 is a leap year.")


if __name__ == '__main__':
    unittest.main()
