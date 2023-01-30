# Starting Out With Python 5th Edition: Chapter 10 - Exercise 2

class Car:
    # The __init__ method initializes the attributes.
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # The accelerate method adds 5 to the speed data attribute each time it's called
    def accelerate(self):
        self.__speed += 5

    # The brake method subtracts 5 from the speed data attribute each time it's called
    def brake(self):
        self.__speed -= 5

    # The get_speed method returns the speed attribute
    def get_speed(self):
        return self.__speed


def main():
    # Get information from the user
    year_model = int(input('Enter the car\'s year model: '))
    make = input('Enter the car\'s make: ')

    # Create a Car object
    car = Car(year_model, make)

    # Call the accelerate method five times
    print('\nAccelerating...')
    for i in range(4):
        # Accelerate the car
        car.accelerate()

        # Display the current speed
        print(f'Current Speed: {car.get_speed()}')

    # Call the brake method five times
    print('\nBraking...')
    for i in range(4):
        # Brake the car
        car.brake()

        # Display the current speed
        print(f'Current Speed: {car.get_speed()}')


# Call the main function
if __name__ == '__main__':
    main()
