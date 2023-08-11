import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        """Checks my_datetime for a base case of 0."""
        expected = '01-01-1970'
        self.assertEqual(task.my_datetime(0), expected,\
            "A value of 0 does not return 01-01-1970.")

    def test2(self):
        """Checks my_datetime that one day in seconds returns 01-02-1970."""
        expected = '01-02-1970'
        num_sec = 86400
        self.assertEqual(task.my_datetime(num_sec), expected,\
            msg=" A value of 86400 seconds or 1 day does not return 01-02-1970.")

    def test3(self):
        """Checks my_datetime with a value of one month."""
        expected = '02-01-1970'
        num_sec = 2678400
        self.assertEqual(task.my_datetime(num_sec), expected,\
            msg="A value of 2678400 or one month does not return 02-01-1970")


if __name__ == '__main__':
    unittest.main()
