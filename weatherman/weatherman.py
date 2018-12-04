"""
Main module of the program. From here the
program initiates its execution and prints
results of temperatures according to
the given options and date
"""
import calendar
import sys

from command_arguments import CommandArgument
from constants import END_COLOR, BLUE_COLOR, RED_COLOR, IO_EXCEPTION, RECORD_NOT_FOUND, INVALID_ARGUMENTS
from csv_file_content import FileContent
from helpers import set_printing_symbol_and_temp, split_date


def __main__():
    """
    Entry point of the
    program. Manages the flow of program
    calling differnt functions
    on the basis of some checks
    """
    arguments = {}
    manage_arguments(arguments)
    file_content = FileContent(arguments['path'])
    for i in range(1, arguments['total_options'] + 1):
        if arguments['option{}'.format(i)] == '-e':
            print_yearly_data(file_content, arguments['date{}'.format(i)])
        elif arguments['option{}'.format(i)] == '-a':
            print_average_monthly_data(file_content, arguments['date{}'.format(i)])
        elif arguments['option{}'.format(i)] == '-c':
            print_monthly_bar_representation(file_content, arguments['date{}'.format(i)])
        elif arguments['option{}'.format(i)] == '-d':
            print_monthly_one_bar_representation(file_content, arguments['date{}'.format(i)])


def manage_arguments(arguments):
    """
    Manages all the validations of the input
    cmd arguments. Prints error message in case of
    worng arguments and terminate the program.
    """
    arguments['total'] = len(sys.argv)
    if arguments['total'] < 4 or arguments['total'] % 2 != 0:
        print(INVALID_ARGUMENTS)
        exit(1)
    arguments['path'] = sys.argv[1]
    i = 2
    j = 1
    while i < arguments['total']:
        arguments['option{}'.format(j)] = sys.argv[i]
        arguments['date{}'.format(j)] = sys.argv[i + 1]
        j += 1
        i += 2
    arguments['total_options'] = j - 1

    j = 1
    while j <= arguments['total_options']:
        my_arguments = CommandArgument(arguments['option{}'.format(j)], arguments['date{}'.format(j)])
        result = my_arguments.validate_arguments()
        if result != '':
            print(result)
            exit(1)
        j += 1


def print_average_monthly_data(file_content, date):
    """
    Displays the average of highest temperature,
    average of lowest temperature
    average of mean humidity of
    the given month of a year.
    Prints error message in case of
    any error.
    """
    month_abbreviation, month, year = split_date(date)
    monthly_temp_humidity_avg = file_content.get_average_monthly_data(year, month_abbreviation)
    if monthly_temp_humidity_avg is None:
        print(IO_EXCEPTION)
        return
    print('Highest Average: {:02d}C'.format(monthly_temp_humidity_avg['max_temp_avg']))
    print('Lowest Average: {:02d}C'.format(monthly_temp_humidity_avg['min_temp_avg']))
    print('Average Mean Humidity: {:02d}%\n'.format(monthly_temp_humidity_avg['mean_humidity_avg']))


def print_yearly_data(file_content, date):
    """
    Displays the yearly report of highest temperature,
    lowest temperature and highest humidity
    """
    yearly_temp_humidity = file_content.get_yearly_data(date)
    if yearly_temp_humidity is None:
        print(IO_EXCEPTION)
        return

    if not yearly_temp_humidity['file_found']:
        print(IO_EXCEPTION)
        return

    max_temp_date = yearly_temp_humidity['max_temp_year'].split('-')
    min_temp_date = yearly_temp_humidity['min_temp_year'].split('-')
    max_humidity_date = yearly_temp_humidity['max_humidity_year'].split('-')
    print('Highest: {:02d}C on {} {}'.format(
        yearly_temp_humidity['max_temp'],
        calendar.month_name[int(max_temp_date[1])],
        max_temp_date[2]
    ))
    print('Lowest: {:02d}C on {} {}'.format(
        yearly_temp_humidity['min_temp'],
        calendar.month_name[int(min_temp_date[1])],
        min_temp_date[2]
    ))
    print('Humidity: {:02d}% on {} {}\n'.format(
        yearly_temp_humidity['max_humidity'],
        calendar.month_name[int(max_humidity_date[1])],
        max_humidity_date[2]
    ))


def print_monthly_bar_representation(file_content, date):
    """
    Displays the bar chart representation of
    highest and lowest temperatures of the
    given month of the year
    on separate lines with red + for high
    and blue + for low
    """
    month_abbreviation, month_name, year = split_date(date)
    daily_temps_of_month = file_content.get_daily_temps_of_month(year, month_abbreviation)
    if daily_temps_of_month is None:
        print(IO_EXCEPTION)
        return
    print(month_name, year)
    i = 1
    while i <= len(daily_temps_of_month[0]):
        print('{}{:02d} '.format(END_COLOR, i), end='')
        if daily_temps_of_month[0][i] == RECORD_NOT_FOUND:
            print('{}missing'.format(RED_COLOR))
        else:
            temperature = daily_temps_of_month[0][i]
            symbol, temperature = set_printing_symbol_and_temp(temperature)
            print('{}{}'.format(RED_COLOR, symbol) * temperature, end='')
            print('{} {:02d}C'.format(END_COLOR, daily_temps_of_month[0][i]))
        print('{}{:02d} '.format(END_COLOR, i), end='')
        if daily_temps_of_month[1][i] == RECORD_NOT_FOUND:
            print('{}missing'.format(BLUE_COLOR))
        else:
            temperature = daily_temps_of_month[1][i]
            symbol, temperature = set_printing_symbol_and_temp(temperature)
            print('{}{}'.format(BLUE_COLOR, symbol) * temperature, end='')
            print('{} {:02d}C'.format(END_COLOR, daily_temps_of_month[1][i]))
        i += 1
    print(END_COLOR, end='')


def print_monthly_one_bar_representation(file_content, date):
    """
    Displays the bar chart
    representation of highest and lowest
    temperatures of the given month of the year
    on single line with red + for high
    and blue + for low
    """
    month_abbreviation, month_name, year = split_date(date)
    daily_temps_of_month = file_content.get_daily_temps_of_month(year, month_abbreviation)
    if daily_temps_of_month is None:
        print(IO_EXCEPTION)
        return
    print(month_name, year)
    i = 1
    while i <= len(daily_temps_of_month[0]):
        high_temp_missed = (daily_temps_of_month[0][i] == RECORD_NOT_FOUND)
        low_temp_missed = (daily_temps_of_month[1][i] == RECORD_NOT_FOUND)
        print('{}{:02d} '.format(END_COLOR, i), end='')
        if high_temp_missed:
            print('{}missing'.format(RED_COLOR), end='')
        else:
            temperature = daily_temps_of_month[0][i]
            symbol, temperature = set_printing_symbol_and_temp(temperature)
            print('{}{}'.format(RED_COLOR, symbol) * temperature, end='')
        if low_temp_missed:
            print('{}missing'.format(BLUE_COLOR), end='')
        else:
            temperature = daily_temps_of_month[1][i]
            symbol, temperature = set_printing_symbol_and_temp(temperature)
            print('{}{}'.format(BLUE_COLOR, symbol) * temperature, end='')
        if high_temp_missed:
            print('{} missing-'.format(RED_COLOR), end='')
        else:
            print('{} {:02d}C-'.format(END_COLOR, daily_temps_of_month[0][i]), end='')
        if low_temp_missed:
            print('{}missing'.format(BLUE_COLOR))
        else:
            print('{}{:02d}C'.format(END_COLOR, daily_temps_of_month[1][i]))
        i += 1
    print(END_COLOR, end='')


if __name__ == '__main__':
    __main__()
