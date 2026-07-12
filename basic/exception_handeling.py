# Python provides the try, except, else, and finally blocks to gracefully handle errors.
# raise enabling you to create custom error conditions and enforce specific program behavior.

def divide_me(a, b):
    try:
        result = a / b
        return result
    except ValueError as e:
        print('That was not a valid number.', e)
    except ZeroDivisionError as e:
        print(f"Cannot divide by zero! {e}")
    except (ValueError, ZeroDivisionError) as e:
        print(f'Error occurred: {e}')
    else:
        print("No errors!")
    finally:
        print("This will always execute! Useful for clean-up tasks like closing files or releasing resources.")
    return None

def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging: Invalid data received')
        raise  # Re-raises the same ValueError

#  create and raise custom exceptions by defining your own exception classes
class InsufficientFunds(Exception):
    def __init__(self, balance,amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds! Balance: {balance}, Amount: {amount}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFunds(balance, amount)
    return balance - amount

def parse_config(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        # raise ... from None suppresses the original exception context:
        raise ValueError(f"Config file not found: {file_name}") from None
    except ValueError as e:
        # raise ... from e chains the new exception to the original one, preserving the error trail
        raise ValueError(f"Invalid config format: {e}") from e

def calculate_square_root(number):
    # assert statements, which are essentially shorthand for raise with AssertionError
    assert number >= 0, 'Cannot calculate square root of negative number'
    return number ** 0.5

if __name__ == "__main__":
    print(divide_me(10,0))

    try:
        check_age(-10)
    except ValueError as e:
        print(e)

    try:
        process_data('abc')
    except ValueError:
        print('Handled at higher level')

    print('#####################################')
    try:
        new_balance = withdraw(100, 150)
    except InsufficientFunds as e:
        print(f'Transaction failed: {e}')

    print('#####################################')
    config = parse_config('config.txt')
    print(config)

    print('#####################################')
    try:
        square_root = calculate_square_root(-1)
    except AssertionError as e:
        print(f'Error: {e}')
