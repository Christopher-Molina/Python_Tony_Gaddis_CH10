import Exercise_10_05


class CashRegister:

    # The __init__ method initializes the attributes
    def __init__(self):
        self.__items = []

    # Each time the purchase_item method is called, the RetailItem
    # object that is passed as argument is added to the list
    def purchase_item(self, retail_item):
        self.__items.append(retail_item)

    # The get_total method returns the total price of all the RetailItem
    # objects stored in the list
    def get_total(self):
        total = 0
        for item in self.__items:
            total += item.get_price() * item.get_units()
        return total

    # The show_items method displays data about the RetailItem
    # objects stored in the list
    def show_items(self):
        for item in self.__items:
            print(f'{item.get_description():14s}{item.get_units()}{item.get_price():14.2f}')

    # The clear method clears the items list
    def clear(self):
        self.__items.clear()

    # The __str__ method returns the attribute states
    def __str__(self):
        return f'{self.show_items()}\n\t\t\t\t\t---------\nTotal: {self.get_total():19.2f} ($)'


def main():
    try:
        # Allow user to enter several items to purchase
        print('-------- XYZ Company --------')

        # Sentinel value to control the loop
        choice = ''

        # Create instance of CashRegister
        register = CashRegister()

        while choice.upper().rstrip() != 'N':
            print()

            # Input item information
            item = get_retail_item()

            # Add the object to CashRegister
            register.purchase_item(item)

            # Input another choice
            choice = input_validation()

        # Display receipt
        print('\nItem\t\tQty\t\tPrice ($)\n----\t\t---\t\t---------')
        print(register)

        # Clear the register
        register.clear()
    except (TypeError, IndexError, ValueError, IOError) as e:
        print(e)


def get_retail_item():
    # Input item description
    description = input('Description: ')

    # Input number of units to purchase
    units = int(input('Units: '))

    # Input price per punit
    price = float(input('Price: '))

    # Return instance of RetailItem
    return Exercise_10_05.RetailItem(description, units, price)


# This function validates user input
def input_validation():
    choice = input('\nWould you like to purchase another item (Y = yes, N = no)? ').upper() + '\n'

    while choice.rstrip() not in {'Y', 'N', 'YES', 'NO'}:
        print('\nERROR - Enter a valid choice: ')
        choice = input('Would you like to purchase another item (Y = yes, N = no)? ').upper() + '\n'

    return choice


# Call the main function
if __name__ == '__main__':
    main()
