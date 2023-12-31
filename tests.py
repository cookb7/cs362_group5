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
        self.assertEqual(task.my_datetime(num_sec), expected)

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
        """
        Checks my_datetime with a value of 94608000 or three years to test for
        a leap year. Should return 12-31-1972.
        """
        expected = '12-31-1972'
        num_sec = 94608000
        self.assertEqual(task.my_datetime(num_sec), expected,
                         msg="Does not account for a leap year.")

    def test_datetime_6(self):
        """Checks my_datetime with 123456789. Should return 11-29-1973."""
        expected = '11-29-1973'
        num_sec = 123456789
        self.assertEqual(task.my_datetime(num_sec), expected,
                         msg="A value of 123456789 fails to return 11-29-1973")

    def test_datetime_7(self):
        """
        Checks my_datetime with a value of 9876543210. Should return 12-22-2282
        """
        expected = '12-22-2282'
        num_sec = 9876543210
        self.assertEqual(task.my_datetime(num_sec), expected)

    def test_leapyear_1(self):
        """Checks check_leap_year with a value of 1970. Should return False"""
        self.assertFalse(task.check_leap_year(1970), msg="1970 not leap year.")

    def test_leapyear_2(self):
        """Checks check_leap_year with a value of 1971. Should return False"""
        self.assertFalse(task.check_leap_year(1971), msg="1971 not leap year")

    def test_leapyear_3(self):
        """Checks check_leap_year with a value of 1972. Should return True"""
        self.assertTrue(task.check_leap_year(1972), msg="1972 is a leap year.")

    def test_conv_num_1(self):
        """checks an empty string, should return None"""
        self.assertEqual(task.conv_num(''), None)

    def test_conv_num_2(self):
        """checks a base 10 integer of high value"""
        self.assertEqual(task.conv_num('123456789'), 123456789)

    def test_conv_num_3(self):
        """checks a base 10 integer of high value that is negative"""
        self.assertEqual(task.conv_num('-123456789'), -123456789)

    def test_conv_num_4(self):
        """checks a base 10 integer of high value with a decimal"""
        self.assertEqual(task.conv_num('123456.789'), 123456.789)

    def test_conv_num_5(self):
        """checks a base 10 integer of that is negative with a decimal"""
        self.assertEqual(task.conv_num('-12.3456789'), -12.3456789)

    def test_conv_num_6(self):
        """
        checks a base 10 integer of high value with
        an un allowed character at the beginning
        """
        self.assertEqual(task.conv_num('z123456789'), None)

    def test_conv_num_7(self):
        """
        checks a base 10 integer of high value with
        an un allowed character at the end
        """
        self.assertEqual(task.conv_num('123456789@'), None)

    def test_conv_num_8(self):
        """
        checks a base 10 integer of high value with
        an un allowed character in the middle
        """
        self.assertEqual(task.conv_num('12345y6789'), None)

    def test_conv_num_9(self):
        """
        checks a base 10 integer of high value
        with two consecutive decimal places
        """
        self.assertEqual(task.conv_num('..123456789'), None)

    def test_conv_num_10(self):
        """checks base 10 int with two separate decimal places"""
        self.assertEqual(task.conv_num('123.456789.'), None)

    def test_conv_num_11(self):
        """checks  base 10 integer with two consecutive minus signs"""
        self.assertEqual(task.conv_num('--123456789'), None)

    def test_conv_num_12(self):
        """checks a base 10 integer with two separate minus signs"""
        self.assertEqual(task.conv_num('-12345678-9'), None)

    def test_conv_num_13(self):
        """checks an integer object"""
        self.assertEqual(task.conv_num(123), None)

    def test_conv_num_14(self):
        """checks a list object"""
        self.assertEqual(task.conv_num([1, 2, 3]), None)

    def test_conv_num_15(self):
        """check a basic hexadecimal number"""
        self.assertEqual(task.conv_num('0x7B'), 123)

    def test_conv_num_16(self):
        """check a basic hexadecimal number"""
        self.assertEqual(task.conv_num('0x7B'), 123)

    def test_conv_num_17(self):
        """check a basic hexadecimal number with negative sign"""
        self.assertEqual(task.conv_num('-0x7B'), -123)

    def test_conv_num_18(self):
        """check a basic hexadecimal number without '0x' prefix"""
        self.assertEqual(task.conv_num('7B'), None)

    def test_conv_num_19(self):
        """check a basic hexadecimal number with un allowed characters"""
        self.assertEqual(task.conv_num('0x7Bs'), None)

    def test_conv_num_20(self):
        """check a basic hexadecimal number with un allowed decimal point"""
        self.assertEqual(task.conv_num('0x7B.0'), None)

    def test_conv_endian_1(self):
        """check for conversion of positive number with the big endian flag."""
        self.assertEqual(task.conv_endian(836281, 'big'), '0C C2 B9')

    def test_conv_endian_2(self):
        """check for a conversion of a number with no flag specified."""
        self.assertEqual(task.conv_endian(836281), '0C C2 B9')

    def test_conv_endian_3(self):
        """check for conversion of negative number with big endian flag."""
        self.assertEqual(task.conv_endian(-836281), '-0C C2 B9')

    def test_conv_endian_4(self):
        """check for conversion of positive number with little endian flag"""
        self.assertEqual(task.conv_endian(836281, 'little'), 'B9 C2 0C')

    def test_conv_endian_5(self):
        """check for conversion of negative number with little endian flag."""
        self.assertEqual(task.conv_endian(-836281, 'little'), '-B9 C2 0C')

    def test_conv_endian_6(self):
        """check for a conversion of an invalid endian type."""
        self.assertIsNone(task.conv_endian(-836281, 'small'))

    def test_conv_endian_7(self):
        """check for a conversion of zero with the big endian flag"""
        self.assertEqual(task.conv_endian(0, 'big'), '00')

    def test_conv_endian_8(self):
        """check for a conversion of zero with the little endian flag."""
        self.assertEqual(task.conv_endian(0, 'little'), '00')

    def test_conv_endian_9(self):
        """check conversion of a single decimal digit."""
        self.assertEqual(task.conv_endian(15), '0F')

    def test_conv_endian_10(self):
        """check conversion of a single negative decimal digit."""
        self.assertEqual(task.conv_endian(-15), '-0F')


if __name__ == '__main__':
    unittest.main()
