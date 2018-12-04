"""
Collects and returns data from .csv temperature
"""
import csv
import os
import re

from constants import FILE_PREFIX, RECORD_NOT_FOUND
from helpers import is_num


class FileContent:
    """
    Calculates result from csv file
    on the basis of certain parameters
    """
    def __init__(self, path):
        self.path = path
        self.file_names = []
        # file contains (dir_path, dir_name, filenames )
        # so by file[2] here we are getting all filenames
        for file in os.walk(path):
            self.file_names.extend(file[2])

    def __str__(self):
        return '{}'.format(self.file_names)

    def get_yearly_data(self, year):
        """
        Computes highest, lowest temperature
        and highest humidity of the given year in a
        dictionary
        """
        regex = '{}{}_[a-z]{{3}}.txt'.format(FILE_PREFIX, year)
        selected_file_names = re.findall(regex, ' '.join(self.file_names), re.IGNORECASE)

        # to skip initial whitespaces
        csv.register_dialect('myDialect', delimiter=',', skipinitialspace=True)

        temp_humid_dict = {}
        temp_humid_dict['file_found'] = bool(len(selected_file_names))
        temp_humid_dict['max_temp'] = -999
        temp_humid_dict['min_temp'] = 999
        temp_humid_dict['max_humidity'] = 0
        temp_humid_dict['min_temp_year'] = 'N/A'
        temp_humid_dict['max_temp_year'] = 'N/A'
        temp_humid_dict['max_humidity_year'] = 'N/A'
        try:
            for name in selected_file_names:
                with open('{}/{}'.format(self.path, name), 'r') as csv_file:
                    reader = csv.reader(csv_file, dialect='myDialect')
                    # to skip header
                    next(csv_file)
                    # returns tuple (index ,the complete line)
                    for index_line in enumerate(reader):
                        if is_num(index_line[1][1]):
                            if int(index_line[1][1]) > temp_humid_dict['max_temp']:
                                temp_humid_dict['max_temp'] = int(index_line[1][1])
                                temp_humid_dict['max_temp_year'] = index_line[1][0]
                        if is_num(index_line[1][3]):
                            if int(index_line[1][3]) < temp_humid_dict['min_temp']:
                                temp_humid_dict['min_temp'] = int(index_line[1][3])
                                temp_humid_dict['min_temp_year'] = index_line[1][0]
                        if is_num(index_line[1][7]):
                            if int(index_line[1][7]) > temp_humid_dict['max_humidity']:
                                temp_humid_dict['max_humidity'] = int(index_line[1][7])
                                temp_humid_dict['max_humidity_year'] = index_line[1][0]
                csv_file.close()
        except IOError:
            return None

        return temp_humid_dict

    def get_average_monthly_data(self, year, month):
        """
        Calculates the average
        highest and lowest temperature and
        average highest humidity of the given
        month of a year and returns result in a
        dictionary. Returns None in case of any
        exception
        """
        temp_humid_dict = {}
        temp_humid_dict['max_temp_sum'] = 0
        temp_humid_dict['min_temp_sum'] = 0
        temp_humid_dict['mean_humidity_sum'] = 0
        temp_humid_dict['max_temp_count'] = 0
        temp_humid_dict['min_temp_count'] = 0
        temp_humid_dict['mean_humidity_count'] = 0
        name = FILE_PREFIX + '{}_{}.txt'.format(year, month)

        # to skip initial whitespaces
        csv.register_dialect('myDialect', delimiter=',', skipinitialspace=True)
        try:
            with open('{}/{}'.format(self.path, name), 'r') as csv_file:
                reader = csv.reader(csv_file, dialect='myDialect')
                # to skip header
                next(csv_file)
                # returns tuple (index ,the complete line)
                for index_line in enumerate(reader):
                    if is_num(index_line[1][1]):
                        temp_humid_dict['max_temp_sum'] += int(index_line[1][1])
                        temp_humid_dict['max_temp_count'] += 1
                    if is_num(index_line[1][3]):
                        temp_humid_dict['min_temp_sum'] += int(index_line[1][3])
                        temp_humid_dict['min_temp_count'] += 1
                    if is_num(index_line[1][7]):
                        temp_humid_dict['mean_humidity_sum'] += int(index_line[1][8])
                        temp_humid_dict['mean_humidity_count'] += 1
            csv_file.close()
        except IOError:
            return None

        temp_humid_average = {}
        temp_humid_average['max_temp_avg'] = temp_humid_dict['max_temp_sum'] // temp_humid_dict['max_temp_count']
        temp_humid_average['min_temp_avg'] = temp_humid_dict['min_temp_sum'] // temp_humid_dict['min_temp_count']
        temp_humid_average['mean_humidity_avg'] = temp_humid_dict['mean_humidity_sum'] // temp_humid_dict[
            'mean_humidity_count']
        return temp_humid_average

    def get_daily_temps_of_month(self, year, month):
        """
        Returns the daily highest and lowest temperature of
        the given month of a year in a list of two dictionaries.
        Returns None in case of any exception.
        """
        low_temps = {}
        high_temps = {}
        name = '{}{}_{}.txt'.format(FILE_PREFIX, year, month)

        # to skip initial whitespaces
        csv.register_dialect('myDialect', delimiter=',', skipinitialspace=True)

        j = 1
        try:
            with open('{}/{}'.format(self.path, name), 'r') as csv_file:
                reader = csv.reader(csv_file, dialect='myDialect')
                # to skip header
                next(csv_file)
                # returns tuple (index ,the complete line)
                for index_line in enumerate(reader):
                    if is_num(index_line[1][1]):
                        high_temps[j] = int(index_line[1][1])
                    else:
                        high_temps[j] = RECORD_NOT_FOUND
                    if is_num(index_line[1][3]):
                        low_temps[j] = int(index_line[1][3])
                    else:
                        low_temps[j] = RECORD_NOT_FOUND
                    j += 1
            csv_file.close()
        except IOError:
            return None

        return [high_temps, low_temps]
