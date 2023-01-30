# Starting Out With Python 5th Edition: Chapter 10 - Exercise 5

class RetailItem:
    # The __init__ method initializes the data attributes
    def __init__(self, description, units, price):
        self.__description = description
        self.__units = units
        self.__price = price

    # The set_description method sets the description attribute
    def set_description(self, description):
        self.__description = description

    # The set_units method sets the units attribute
    def set_units(self, units):
        self.__units = units

    # The set_price method sets the price attribute
    def set_price(self, price):
        self.__price = price

    # The get_description methods returns the description attribute
    def get_description(self):
        return self.__description

    # The get_units method returns the units attribute
    def get_units(self):
        return self.__units

    # The get_price method returns the price attribute
    def get_price(self):
        return self.__price

    # The __str__ method returns the attribute states
    def __str__(self):
        return f'Description: {self.__description}\nUnits: {self.__units}' + \
               f'\nPrice: {self.__price}'


def main():
    # Create three instances of RetailItem
    item1 = RetailItem('Jacket', 12, 59.95)
    item2 = RetailItem('Designer Jeans', 40, 34.95)
    item3 = RetailItem('Shirt', 20, 24.95)

    # Display the objects
    print(item1, '\n')
    print(item2, '\n')
    print(item3)


# Call the main function
if __name__ == '__main__':
    main()
