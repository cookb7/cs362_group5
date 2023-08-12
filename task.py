def conv_num(num_str):
    pass


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
    """This function converts to a hexadecimal value and determines whether
    the endianness of the value is big or small"""
    check = ''
    if num < 0:
        check = '-'
        num = -num

    # Listing of hex digits
    hex_digits = '0123456789ABCDEF'
    hex_store = []
    while num:
        hex_store.append(hex_digits[num % 16])
        num //= 16
    if not hex_store:
        hex_store.append('0')

    hex_string = ''.join(reversed(hex_store))

    if len(hex_string) % 2 == 1:
        hex_string = '0' + hex_string

    # Splicing the list
    sol_list = [hex_string[i:i + 2] for i in range(0, len(hex_string), 2)]

    if endian == 'little':
        sol_list = reversed(sol_list)
    elif endian != 'big':
        return None

    return check + ' '.join(sol_list)