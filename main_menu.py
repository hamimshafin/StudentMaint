#!/usr/bin/env python3


# Import built-in modules first
# followed by third-party modules
# followed by any changes to the path
# your own modules.
import student_maintenance as sm    # student add, update, delete, list
import data_validation as dv  # user input data validation

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Debbie Johnson'
__version__ = '1.0'
__date__ = '2024.02.12'
__status__ = 'Development'


def display_menu():

    print('Student Records Menu')
    print('======================')
    print('1 - List all students')
    print('2 - Add a student')
    print('3 - Update a student')
    print('4 - Delete a student')
    print('0 - Exit program')
    print()

    return


def main():

    students = {}  # students 2D dictionary {id: {'first_name': value}, {'last_name': value}}
    next_student_id = 1

    while True:
        display_menu()

        menu_num = dv.get_range('Please enter a Menu #', 0, 4)
        print()
        if menu_num == 1:
            sm.list_students(students)
        elif menu_num == 2:
            sm.add_student(students, next_student_id)
            next_student_id += 1
        elif menu_num == 3:
            sm.update_student(students)
        elif menu_num == 4:
            sm.delete_student(students)
        elif menu_num == 0:
            break
        else:
            print('Not a valid menu option.')

        input('Press Enter to continue...')
        print()

    print('Bye!')

    return


# if this is the module where the program started running from, then run the main function
if __name__ == '__main__':
    # help('main_menu')  # used to display the script's docstring
    main()
