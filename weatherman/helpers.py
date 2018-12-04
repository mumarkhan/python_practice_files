"""
Contains the helper
functions which will be used
by other functions or classes
"""
import calendar
import re


def is_num(value):
    """
    Checks either string contains a number or not
    """
    regex = '-?[\d]*'
    if value == '' or re.match(regex, value) is None:
        return False

    return True


def split_date(date):
    """
    Gets date in string and returns
    month abbreviation, month name and year
    """
    date_tokens = date.split('/')
    year = date_tokens[0]
    month_abbreviation = calendar.month_abbr[int(date_tokens[1])]
    month_name = calendar.month_name[int(date_tokens[1])]
    return month_abbreviation, month_name, year


def set_printing_symbol_and_temp(temperature):
    """
    Sets and returns printing symbol and temperature
    according to positive or negative value
    """
    temperature = int(temperature)
    symbol = '+'
    if temperature < 0:
        symbol = '-'
        temperature *= -1

    return symbol, temperature
