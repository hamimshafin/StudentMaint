#!/usr/bin/env python3


# the following are module level dunders (metadata) for the authorship information
__author__ = 'Debbie Johnson'
__version__ = '1.0'
__date__ = '2024.02.12'
__status__ = 'Development'


def get_string(prompt):

    while True:
        user_input = input(f'{prompt}: ')
        user_input = user_input.strip()

        if user_input > '':
            return user_input

        print('Invalid Input: Please enter a value!')


def get_num(prompt, data_type='int'):

    while True:
        user_input = input(f'{prompt}: ')

        try:
            if data_type == 'int':
                number = int(user_input)
            else:
                number = float(user_input)

            return number

        except ValueError:
            print('Invalid Input: Please enter a number')


def get_positive_num(prompt, data_type='int'):

    while True:
        user_input = input(f'{prompt}: ')

        try:
            if data_type == 'int':
                number = int(user_input)
            else:
                number = float(user_input)

            if number > 0:
                return number
            else:
                print(f'Invalid Input: Please enter a positive number')

        except ValueError:
            print('Invalid Input: Please enter a number')


def get_range(prompt, low, high, data_type='int'):

    while True:
        user_input = input(f'{prompt} (Valid {low}-{high}): ')

        try:
            if data_type == 'int':
                number = int(user_input)
            else:
                number = float(user_input)

            if low <= number <= high:
                return number
            else:
                print(f'Invalid Input: Please enter a number greater or equal to {low} '
                      f'and less than or equal to {high}')

        except ValueError:
            print('Invalid Input: Please enter a number')


def get_yes_no(prompt='(y=Yes, n=No):'):

    while True:
        user_input = input(f'{prompt} (y=Yes, n=No): ').lower()

        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print('Invalid Input: Please enter a y=yes, or n=no')


# if this is the module where the program started from, then display the module docstring
if __name__ == '__main__':
    help('data_validation')
