''' Python Modules and Data Handling Assignment
Objective:
 The aim of this assignment is to assess your understanding and ability to implement Python modules, both built-in and custom, and to apply
 data handling techniques using Python's data structures and error handling. This assignment will help solidify your grasp on creating 
 and using modules, as well as manipulating and processing data effectively in Python.

Task 1: Your Mood Today:
Problem Statement:
 Create a Python program using a custom module that asks the user how they are feeling today and responds with a custom message based on the mnood entered.


'''

import mood_responses
mood = input("How are you feeling today? (happy, sad, excited): ").lower()
mood_responses.mood_response(mood)

''' Question 2
Objective: 
 The aim of this assignment is to deepen your understanding of Python modules, both built in and custom, and to enhance your skills in working
 with various Python data structures like lists, dictionaries, and sets.  This assignment focuses on practical applications of these concepts in real-world
 scenarios.

Task 1: Contact list manager
Problem Statement:
 Create a Python script using a custom module to manage a contact list. The script should allow adding, removing, and displaying contacts stored in a list.

Expected Outcome:
 Your script should be able to add new contacts, remove existing contacts, and display all contacts. Each contact can be a dictionary with a name and phone number

'''
import contact_manager

def contact_program():
    contacts = {}
    while True:
        print("\nWelcome to Kai's Contact Manager")
        print("\n1. Add New Contacts\n2. Remove a contact\n3. Display Contacts\n4. Exit")
        selection = input("Enter your selection: ")

        if selection == '1':
            contact_manager.add_contact(contacts)
        elif selection == '2':
            contact_manager.delete_contact(contacts)
        elif selection == '3':
            contact_manager.view_contacts(contacts)
        elif selection == '4':
            break
        else:
            print("That's not a proper entry")
        
contact_program()
print()
'''
Task 2: Date Extractor
Problem Statement:
 Write a Python program that uses the datetime module to extract and display the current month and year. Additionally, allow the user to input a date string and parse it
 into a date time object

Expected Outcomes:
 - The program should accurately display the current month and year and successfully convert a user-input date string
 - e.g. 2023-03-15 into datetime object, handling any invalid inputs gracefully.

'''
import datetime

def display_current_month_and_year():
    now = datetime.datetime.now()
    print(f"Current Month: {now.strftime('%B')}")
    print(f"Current Year: {now.year}")

def parse_user_input_date():
    date_input = input("Enter a date in YYYY-MM-DD format: ")
    try:
        parsed_date = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        print(f"The date you entered is: {parsed_date}")
    except ValueError:
        print("Invalid date format. Please ensure your date is in YYYY-MM-DD format.")

def date_time_prog():
    display_current_month_and_year()
    parse_user_input_date()

date_time_prog()
print()

''' 3. Mastering Python Modules and Aliases
Objective:
The aim of this assignment is to enhance your proficiency in using Python modules, both standard and custom, with a specific focus on importing with aliases. 
This will develop your skills in organizing code, simplifying access to module components, and effectively managing namespace in Python programs.

Task 1: Custom Module with Aliases

Problem Statement: 
 Create a custom module named text_utils.py with functions for string manipulation (e.g., reversing a string, capitalizing). 
 In your main script, import this module using an alias and utilize its functions.

Expected Outcome: 
 Your main script should be able to use the functions from text_utils.py via an alias, demonstrating an understanding of custom module creation and aliasing.

'''
import text_utils as tu

def string_manipulator():
    input_string = input("Please enter a string: ")
    
    reversed_string = tu.reverse_string(input_string)
    capitalized_string = tu.capitalize_string(input_string)

    print(f"Original: {input_string}")
    print(f"Reversed: {reversed_string}")
    print(f"Capitalized: {capitalized_string}")

string_manipulator()