# Attributes are variables that belong to an object.
# sometimes, you might not know which attributes you need until your program is running. Imagine you're writing
# a script that receives attribute names from a user or a configuration file. Those are not attributes
# you can hard-code ahead of time.

# Python gives you four handy built-in functions to dynamically work with object attributes.
# They are getattr(), setattr(), hasattr(), and delattr().

# getattr()
# getattr(object, name[, default])
# Return the value of the named attribute of an object. If the named attribute does not exist,
# default is returned if given, otherwise AttributeError is raised.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Configuration:
    pass

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token # sensitive
        self.temp_counter = 0 # temporary

if __name__ == "__main__":
    person = Person("John", 30)
    print(getattr(person, "name"))
    print(getattr(person, "address", "N/A"))

    attr_name = input("Enter the attribute name: ")
    print(getattr(person,attr_name, "N/A"))

    # get a list of all attributes
    print(dir(person))

    # Loop through all attributes of the person object with dir() function
    for attr in dir(person):
        # Ignore dunder methods like __init__ or __str__ and regular methods
        if not attr.startswith('__') and not callable(getattr(person,attr)):
            value = getattr(person,attr)
            print(f"{attr} = {value}")

    # Data loaded at runtime (like from a config or env file)
    settings_data = {
        'server_url': 'https://api.example.com',
        'timeout_sec': 30,
        'max_retries': 5
    }

    config_obj = Configuration()

    # Dynamically set attributes using dictionary keys and values
    for key, value in settings_data.items():
        setattr(config_obj,key,value)

    print("server_url: ",getattr(config_obj,"server_url"))
    print("timeout_sec: ",getattr(config_obj,"timeout_sec"))

    # Dynamically check attributes
    product_a = Product('T-Shirt', 25)
    required_attributes = ['name', 'price', 'inventory_id']

    for attr in required_attributes:
        if not hasattr(product_a,attr):
            print(f"Product {product_a.name} is missing the {attr} attribute.")
        else:
            print(f"Product {product_a.name} has the {attr} attribute.")


    # Dynamically delete attributes
    session = UserSession(123, 'abc')

    # List of attributes to remove before saving the session
    attributes_to_remove = ['auth_token', 'temp_counter']

    for attr in attributes_to_remove:
        if hasattr(session, attr):
            delattr(session, attr)
            print(f"Deleted attribute: {attr}")

    print('\nFinal attributes remaining:')

    # Loop through the remaining attributes with dir()
    for attr in dir(session):
        # Ignore dunder methods like __init__ or __str__ and regular methods
        if not attr.startswith('__') and not callable(getattr(session, attr)):
            print(f' - {attr}: {getattr(session, attr)}')