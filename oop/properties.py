# Properties
# act like attributes but behave like methods.
# it lets us run logic behind the scenes while getting, setting or deleting an attribute's value
# why use properties for that instead of methods? It's mostly about readability and convention.
# They make your code cleaner and easier to read.
# We use it for getters, setters and deleters.

# Keynotes:
# 1. Properties are functions that behave like methods.
# 2. They are defined using the @property decorator.
# 3. They are accessed using the dot notation.
# 4. They are used to define getters, setters, and deleters.
# 5. They are used to encapsulate and manage the state of an object.
# 6. Getters let you retrieve a value or even compute a value on the fly.
# 7. Setters let you modify the values safely by running checks before assignment.
# 8. Properties are what tie these getters and setters together so you can write logic while still using dot notation.
# 9. Deleters let you define what happens when an attribute is deleted.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):  # A getter to get the radius
        return self._radius

    # To Create a Setter, you have to define another method with the same name
    # and use @<property_name>.setter above it
    @radius.setter
    def radius(self, value):  # A setter to set the radius
        if value <= 0:
            raise ValueError('Radius must be positive')
        self._radius = value

    # Note that inside the setter, you cannot use the same name of the property when assigning a new value.
    # That's because self.radius = value will call the setter within the setter method itself,
    # leading to infinite recursion and a RecursionError. So you must always use the underscore-prefixed
    # form self._radius = value.

    @radius.deleter
    def radius(self):
        print('Radius deleted!')
        del self._radius

    @property
    def area(self):  # A getter to calculate area
        return 3.14 * (self._radius ** 2)


def main():
    my_circle = Circle(3)

    print('Initial radius:', my_circle.radius) # Initial radius: 3
    my_circle.radius = 8
    print('Updated radius:', my_circle.radius)
    print('Area:', my_circle.area)

    # Delete the radius
    # This calls the deleter
    del my_circle.radius  # Deleting radius...

    # Try to access radius after deletion
    try:
        print(my_circle.radius)
    except AttributeError as e:
        print("Error:", e)  # Error: 'Circle' object has no attribute '_radius'

if __name__ == "__main__":
    main()