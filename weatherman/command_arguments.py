"""
Validates the command line arguments
"""
import re

from constants import INVALID_ARGUMENTS, OPTION_DATE_MISMATCH


class CommandArgument:

    def __init__(self, option, date):
        self.option = option
        self.date = date

    def validate_arguments(self):
        """
        Validates command line arguments.
        Returns error message if
        validation fails otherwise None.
        """
        my_option_date = '{} {}'.format(self.option, self.date)
        regex = '(-e \d{4})|((-[acd] \d{4}\/)((1[0-2])|(0?[1-9])))'
        match_object = re.match(regex, my_option_date)
        if match_object is None or match_object.span()[1] != len(my_option_date):
            return '{}\n{}'.format(INVALID_ARGUMENTS, OPTION_DATE_MISMATCH)

        return ''

