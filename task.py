def conv_num(num_str):
    pass


def my_datetime(num_sec):
    """Defines a function that takes a number of seconds and
    returns the date after 01-01-1970."""
    SECONDS_IN_DAY = 86400

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    num_days = num_sec // SECONDS_IN_DAY
    
    # Calculate year
    year = 1970
    while num_days >= 365:
        num_days -= 365
        year += 1
        
    # Calculate month
    month = 1
    while num_days >= days_in_month[month - 1]:
        num_days -= days_in_month[month - 1]
        month += 1

    day = num_days + 1 # Add 1 to get correct date format
    date = f"{month:02d}-{day:02d}-{year}"

    return date


def conv_endian(num, endian='big'):
    pass
