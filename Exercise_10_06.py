# Starting Out With Python 5th Edition: Chapter 10 - Exercise 6

class Patient:

    # The __init__ method initializes the data attributes
    def __init__(self, first_name, middle_name, last_name, address, city,
                 state, zip_code, phone_number, emergency_name, emergency_number):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone_number = phone_number
        self.__emergency_name = emergency_name
        self.__emergency_number = emergency_number

    # The set_first_name method sets the first_name attribute
    def set_first_name(self, first_name):
        self.__first_name = first_name

    # The set_middle_name method sets the middle_name attribute
    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    # The set_last_name method sets the last_name attribute
    def set_last_name(self, last_name):
        self.__last_name = last_name

    # The set_address method sets the address attribute
    def set_address(self, address):
        self.__address = address

    # The set_city method sets the address attribute
    def set_city(self, city):
        self.__city = city

    # The set_state method sets the state attribute
    def set_state(self, state):
        self.__state = state

    # The set_zip_code method sets the zip_code attribute
    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

    # The set_phone_number method sets the phone_number attribute
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    # The set_emergency_name method sets the emergency_name attribute
    def set_emergency_name(self, emergency_name):
        self.__emergency_name = emergency_name

    # The set_emergency_number method sets the emergency_number attribute
    def set_emergency_number(self, emergency_number):
        self.__emergency_number = emergency_number

    # The get_first_name method returns the first_name attribute
    def get_first_name(self):
        return self.__first_name

    # The get_middle_name method returns the middle_name attribute
    def get_middle_name(self):
        return self.__middle_name

    # The get_last_name method returns the last_name attribute
    def get_last_name(self):
        return self.__last_name

    # The get_address method returns the address attribute
    def get_address(self):
        return self.__address

    # The get_city method returns the address attribute
    def get_city(self):
        return self.__city

    # The get_state method returns the state attribute
    def get_state(self):
        return self.__state

    # The get_zip_code method returns the zip_code attribute
    def get_zip_code(self):
        return self.__zip_code

    # The get_phone_number method returns the phone_number attribute
    def get_phone_number(self):
        return self.__phone_number

    # The get_emergency_name method sets the emergency_name attribute
    def get_emergency_name(self):
        return self.__emergency_name

    # The get_emergency_number method sets the emergency_number attribute
    def get_emergency_number(self):
        return self.__emergency_number

    # The __str__ method returns the attribute states
    def __str__(self):
        return f'Patient: {self.__first_name} {self.__middle_name} {self.__last_name}\n' \
               f'Address: {self.__address}\n' \
               f'City, State, and ZIP Code: {self.__city}, {self.__state}, {self.__zip_code}\n' \
               f'Phone Number: {self.__phone_number}\n' \
               f'Emergency Contact: {self.__emergency_name} - {self.__emergency_number}'


class Procedure:

    # The __init__ method initializes the data attributes
    def __init__(self, procedure, date, practitioner, charges):
        self.__procedure = procedure
        self.__date = date
        self.__practitioner = practitioner
        self.__charges = charges

    # Mutator methods
    def set_procedure(self, procedure):
        self.__procedure = procedure

    def set_date(self, date):
        self.__date = date

    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner

    def set_charges(self, charges):
        self.__charges = charges

    # Accessor methods
    def get_procedure(self):
        return self.__procedure

    def get_date(self):
        return self.__date

    def get_practitioner(self):
        return self.__practitioner

    def get_charges(self):
        return self.__charges

    def __str__(self):
        return f'\nProcedure Name: {self.__procedure}\n' \
               f'Date: {self.__date}\nPractitioner: {self.__practitioner}\n' \
               f'Charges: {self.__charges}\n'


def main():
    # Create instance of Patient class initialized with sample data
    patient0 = Patient('Christopher', 'Dave', 'Franco',
                       '7720 McCallum Blvd.', 'Dallas', 'TX', 75252, 940_299_3483,
                       'Genesis Martin', 940_516_5656)

    # Create three instances of the procedure class
    procedure1 = Procedure('Physical Exam', '10-02-2022', 'Dr. Irvine', 250.00)
    procedure2 = Procedure('X-Ray', '10-02-2022', 'Dr. Jamison', 500.00)
    procedure3 = Procedure('Blood Test', '10-02-2022', 'Dr. Smith', 200.00)

    # Display patient information
    print('Patient Information:\n')
    print(patient0)

    # Display procedures and total charges
    print('\nProcedures:')
    print(procedure1, procedure2, procedure3, sep='')
    print(f'Total Charges: ${procedure1.get_charges() + procedure2.get_charges() + procedure3.get_charges():,.2f}')


# Call the main function
if __name__ == '__main__':
    main()
