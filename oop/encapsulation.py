# Encapsulation
# is the process of hiding the implementation
# details of a class or module from the outside world.

# Note that this does not prevent the attribute from being accessed or
# modified outside the class. Also, in Python there's always a way to
# access private attributes (prefixed with a double underscore) as well.

#  a single underscore is a convention that means the attribute is meant
#  for internal use in the class and should not be directly accessed from
#  outside the class. Double underscore, on the other hand, prevents that
#  attribute from being accessed directly from outside the class.

class Wallet:
    def __init__(self, balance):
       self._balance = balance # For internal use by convention
       self.__private_data = "This is a private attribute"

    def __validate(self, amount): # Private method to validate the amount
        if amount < 0:
            raise ValueError('Amount must be positive')

    def deposit(self, amount):
        self.__validate(amount)
        self._balance += amount # Add to the balance safely

    def withdraw(self, amount):
        self.__validate(amount)
        if amount > self._balance:
            raise ValueError('Insufficient funds')
        self._balance -= amount

    def get_private_data(self):
        return self.__private_data

def main():
    wallet = Wallet(100)
    wallet.deposit(50)
    wallet.withdraw(30)
    print(wallet._balance) # can access the private attribute
    #print(wallet.__private_data) # AttributeError: 'Wallet' object has no attribute '__private_data'
    print(wallet.get_private_data()) # can access the private method

if __name__ == "__main__":
    main()