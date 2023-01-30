# Starting Out With Python 5th Edition: Chapter 10 - Exercise 3

class Information:
    # The __init__ method initializes the attributes
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    # The set_name method sets the name attribute
    def set_name(self, name):
        self.__name = name

    # The set_address method sets the address attribute
    def set_address(self, address):
        self.__address = address

    # The set_age method sets the age attribute
    def set_age(self, age):
        self.__age = age

    # The set_phone_number method sets the phone_number attribute
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    # The get_name method returns the name attribute
    def get_name(self):
        return self.__name

    # The get_address method returns the address attribute
    def get_address(self):
        return self.__address

    # The get_age method returns the age attribute
    def get_age(self):
        return self.__age

    # The get_phone_number method returns the phone_number attribute
    def get_phone_number(self):
        return self.__phone_number

    # The __str__ method returns the attributes states
    def __str__(self):
        return f'\nName: {self.__name}' + \
               f'\nAddress: {self.__address}' + \
               f'\nAge: {self.__age}' + \
               f'\nPhone Number: {self.__phone_number}'


def main():
    # Get information
    print('Enter your name, dad, and friend\'s information, respectively: ')
    my_information, dad_information, friend_information = get_information(), get_information(), get_information()

    # Display the information
    print('\nInformation:')
    print(f'{my_information}\n{dad_information}\n{friend_information}')


def get_information():
    # Get information
    name = input('\nName: ')
    address = input('Address: ')
    age = int(input('Age: '))
    phone_number = input('Phone Number: ')

    # Return instance of Information class
    return Information(name, address, age, phone_number)


# Call the main method
if __name__ == '__main__':
    main()
