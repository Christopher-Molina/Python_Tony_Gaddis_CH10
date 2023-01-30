import Exercise_10_04
import pickle

# Global constants for menu choice
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constant for the filename
FILENAME = 'employees.dat'


def main():
    # Load the employees dictionary
    employees = load_employees()

    # Initialize a variable for the user's choice
    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()

        if choice == 1:
            look_up(employees)
        elif choice == 2:
            add(employees)
        elif choice == 3:
            change(employees)
        elif choice == 4:
            delete(employees)

    # Save the employees dictionary to a file
    save_employees(employees)


def load_employees():
    try:
        # Open the employees.dat file
        infile = open(FILENAME, 'rb')

        # Unpickle the dictionary
        employees = pickle.load(infile)

        # Close the file
        infile.close()
    except IOError:
        # Could not open the file, so create an empty dictionary
        employees = {}

    # Return the dictionary
    return employees


# Function returns the menu choice chosen by the user
def get_menu_choice():
    print('Menu')
    print('---------------------')
    print('1. Look up an employee.\n2. Add a new employee.\n3. Change an existing employee.')
    print('4. Delete an employee.\n5. Quit the program.')

    choice = int(input('\nEnter your choice: '))

    # Input validation
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('ERROR - Enter a valid choice: '))

    # Return the user choice
    return choice


def look_up(employees):
    # Get a name to look up
    name = input('Enter a name: ')

    # Look it up in the dictionary
    print(employees.get(name, 'That name is not found.'))


def add(employees):
    # Get a name to add to the employees dictionary
    name = input('Name: ')
    id_number = int(input('ID Number: '))
    department = input('Department: ')
    job_title = input('Job Title: ')

    # Create a contact object named employee
    entry = Exercise_10_04.Employee(name, id_number, department, job_title)

    # Store the employee object into a dictionary
    if name not in employees:
        employees[name] = entry
        print('The entry has been added.')
    else:
        print('That name already exists.')


def change(employees):
    # Get a name to look up
    name = input('Enter a name: ')

    if name in employees:
        # Get a new id_number
        id_number = int(input('Enter the new ID number: '))

        # Get a new department
        department = input('Enter the new department: ')

        # Get a new job title
        job_title = input('Enter the new job title: ')

        # Update the entry
        entry = Exercise_10_04.Employee(name, id_number, department, job_title)
        employees[name] = entry
        print('Information updated.')
    else:
        print('That name is not found.')


def delete(employees):
    name = input('Enter a name: ')
    if name in employees:
        del employees[name]
        print('Entry deleted.')
    else:
        print('That name is not found.')


def save_employees(employees):
    # Open the file for writing
    outfile = open(FILENAME, 'wb')

    # Pickle the dictionary and save it
    pickle.dump(employees, outfile)

    # Close the file
    outfile.close()


# Call the main function
if __name__ == '__main__':
    main()
