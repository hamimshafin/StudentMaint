#!/usr/bin/env python3
import data_validation as dv

"""
Usage: Student_Maint.py
This program will allow you to keep a record of students. 
You will also be able to update and delete students in the list.

GitHub: https://github.com/hamimshafin/StudentMaint.git
"""

# metadata
__author__ = 'Samuel Nuno & Hamim Shafin'
__version__ = '1.0'
__date__ = '2024.02.12'
__status__ = 'Complete'


def list_students(students):

    if len(students) == 0:
        print('There are no students in the list.')
        return

    # Setup for displaying the list of students
    print("  ID First Name      Last Name")
    print('==== =============== ================')

    for student_id, student_data in students.items():
        first_name, last_name = student_data.values()
        print(f'{student_id:>4} {first_name:<15} {last_name:<15}')

    return


def add_student(students, next_student_id):

    print('Add Student')
    print('-----------')

    # Gather the input of the first and last name the user inputs
    first_name = dv.get_string(f'Please enter the Student\'s First Name').title()
    last_name = dv.get_string(f'Please enter the Student\'s Last Name').title()

    #  States that the student was added to the list
    students[next_student_id] = {'first_name': first_name, 'last_name': last_name}
    print(f"Student ID # {next_student_id} {first_name} {last_name} was added")


def update_student(students):

    if len(students) == 0:
        print('There are no students to update.')
        return

    print('Update Student')
    print('--------------')

    student_id = dv.get_num("Please enter the Student ID to be updated")

    if student_id not in students:
        print("Student ID not found.")
        return

    first_name, last_name = students[student_id].values()

    yes = dv.get_yes_no(f'Do you want to update Student ID #{student_id} {first_name} {last_name}')

    # If not confirmed, update will be cancelled
    if not yes:
        print('Update cancelled.')
        return

    # Updates the first and/or last name of the student
    new_first_name = input(f"Please enter the Student\'s new First Name or press enter to keep {first_name}: ").title()
    new_last_name = input(f"Please enter the Student\'s new Last Name or press enter to keep {last_name}: ").title()

    # States that there was no change done to the student
    if new_first_name == ' ' and new_last_name == ' ':
        print("No data changed, update cancelled")
        return

    # Updates the list for the new first name inputted
    if len(new_first_name) == 0:
        new_first_name = first_name

    # Updates the list for the new last name inputted
    if len(new_last_name) == 0:
        new_last_name = last_name

    # Holds the first and last name being replaced
    old_first_name = first_name
    old_last_name = last_name

    # States the previous name was updated to th new name
    print(f'Student ID #{student_id} {old_first_name} {old_last_name} was updated to {new_first_name} {new_last_name}')

    first_name = new_first_name
    last_name = new_last_name

    students[student_id] = {'first_name': first_name, 'last_name': last_name}
    return


def delete_student(students):

    if len(students) == 0:
        print('There are no students to delete.')
        return

    print('Delete Student')
    print('--------------')

    student_id = int(input("Please enter the Student ID to be deleted: "))

    # Throws an error if the number inputted isn't assigned to a student
    if student_id not in students:
        print(f'Student ID #{student_id} was not found. ')
        return

    first_name, last_name = students[student_id].values()

    # Lets the user confirm deleting with yes or no
    yes = dv.get_yes_no(f'Confirm deleting Student ID #{student_id} {first_name} {last_name}')

    # If not confirmed, delete will be cancelled
    if not yes:
        print('Delete cancelled.')
        return

    # Deletes student
    del students[student_id]

    # Statement saying the student was deleted
    print(f'Student ID #{student_id} {first_name} {last_name} was deleted')
    return


# if this is the module where the program started from, then display the module docstring
if __name__ == '__main__':
    help('student_maintenance')
