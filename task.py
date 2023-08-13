def conv_num(num_str):
    """
    Author: Sam Miller GitHub: samuelcoding97
    Changes made: 13 August 2023
    Accepts a string and converts into a base-10 int type and returns it. This
    method can handle hexadecimal numbers, signed numbers, integers and floats.
    If the input is not a valid number, the method returns the None object.
    """
    # if input is not a string return None
    if isinstance(num_str, str) is False or len(num_str) == 0:
        return None

    # initialize integer that will return at end of method
    num_int = 0
    # make a list of the string
    num_str_lower = num_str.lower()
    num_list = list(num_str_lower)

    # get the sign
    num_sign = get_sign(num_list)
    num_list = update_num_list(num_list, num_sign)

    # check for multiple .'s and multiple x's and -'s
    if num_list.count(".") > 1 or num_list.count("x") > 1 or num_list.count("-") > 1:
        return None

    # iterate through each character, returning None if char is not 0-9, a-f, x, ".", or -
    valid_input = check_str(num_list)
    if valid_input is False:
        return None

    # if the number is hexadecimal
    if ord(num_list[1]) == 120:
        num_int = hex_conversion(num_list, num_int)

    # if the number is decimal
    else:
        num_int = dec_conversion(num_list, num_int)
        num_int = dec_point_conversion(num_list, num_int)

    if num_int is None:
        return None

    # apply the number sign
    num_int *= num_sign

    # return final value
    return num_int

def get_sign(num_list):
    num_sign = 1
    if num_list[0] == "-":
        num_sign = -1
    return num_sign

def update_num_list(num_list, num_sign):
    if num_sign == -1:
        num_list = num_list[1:]
    return num_list

def check_str(num_list):
    for char in range(len(num_list)):
        # if it is a digit 0-9
        if 47 < ord(num_list[char]) < 58:
            continue
        # it is a letter a-f
        elif 96 < ord(num_list[char]) < 103:
            continue
        # it is a decimal point
        elif ord(num_list[char]) == 46:
            continue
        # it is letter x to clarify hexadecimal input
        elif ord(num_list[char]) == 120:
            if char == 1:
                continue
            else:
                return False
        else:
            return False
    return True

def hex_conversion(num_list, num_int):
    if ord(num_list[0]) == 48:
        num_list = num_list[2:]
        for char in range(len(num_list)):
            # if hex character convert to int
            if 96 < ord(num_list[char]) < 103:
                digit_val = ord(num_list[char]) - 87
                num_int = num_int * 16 + digit_val
            # decimal point not allowed in hexadecimal
            elif ord(num_list[char]) == 46:
                return None
            else:
                # convert digits to int
                digit_val = ord(num_list[char]) - 48
                num_int = num_int * 16 + digit_val
    else:
        return None
    return num_int

def dec_conversion(num_list, num_int):
    for char in range(len(num_list)):
        # un allowed characters for base 10 conversions
        if ord(num_list[char]) < 46 or ord(num_list[char]) > 57 or ord(num_list[char]) == 47:
            return None
        elif ord(num_list[char]) == 46:
            continue
        else:
            # convert each number to ordinal subtract 48 to get int and add to num_int
            digit_val = ord(num_list[char]) - 48
            num_int = num_int * 10 + digit_val
    return num_int

def dec_point_conversion(num_list, num_int):
    dec_point = -1
    for char in range(len(num_list)):
        if ord(num_list[char]) == 46:
            dec_point = len(num_list) - char - 1

    # apply the decimal point
    if dec_point > -1:
        ratio = 10 ** dec_point
        num_int /= ratio

    return num_int


def my_datetime(num_sec):
    """Defines a function that takes a number of seconds and
    returns the date after 01-01-1970."""
    SECONDS_IN_DAY = 86400
    START_YEAR = 1970

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num_days = num_sec // SECONDS_IN_DAY

    # Calculate year
    year = START_YEAR
    while True:
        days_in_year = 366 if check_leap_year(year) else 365
        if num_days < days_in_year:
            break
        num_days -= days_in_year
        year += 1

    # If leap year then change Febuary to 29 days
    if check_leap_year(year):
        days_in_month[1] = 29

    # Calculate month
    month = 1
    while num_days >= days_in_month[month - 1]:
        num_days -= days_in_month[month - 1]
        month += 1

    day = num_days + 1  # Add 1 to get correct date format
    date = f"{month:02d}-{day:02d}-{year}"

    return date


def check_leap_year(year):
    """Defines a function that takes a year and checks if it is a leap year.
    Returns True if it is a leap year and False if not."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def conv_endian(num, endian='big'):
    pass
