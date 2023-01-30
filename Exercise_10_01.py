# Starting Out With Python 5th Edition: Chapter 10 - Exercise 1

class Pet:
    # The __init__ method initializes the attributes.
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # The set_name method sets the name attribute
    def set_name(self, name):
        self.__name = name

    # The set_animal_type method sets the animal_type attribute
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # The set_age method sets the age attribute
    def set_age(self, age):
        self.__age = age

    # The get_name method returns the name attribute
    def get_name(self):
        return self.__name

    # The get_animal_type method returns the animal_type attribute
    def get_animal_type(self):
        return self.__animal_type

    # The get_age method returns the age attribute
    def get_age(self):
        return self.__age


def main():
    # Get the pet information
    name = input('Enter your pet\'s name: ')
    animal_type = input('Enter the animal type: ')
    age = int(input('Enter your pet\'s age: '))

    # Create an instance of Pet with the above information
    pet = Pet(name, animal_type, age)

    # Display the pet's information
    print(f'\nName: {pet.get_name()}')
    print(f'Animal Type: {pet.get_animal_type()}')
    print(f'Age: {pet.get_age()}')


# Call the main function
if __name__ == '__main__':
    main()
