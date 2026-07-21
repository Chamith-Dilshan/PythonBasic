# Inheritance
# is a mechanism for creating a new class from an existing class.
# With inheritance, a subclass (or child class) can use the attributes
# and methods of a base class (or parent class). This allows you to reuse
# code, create clear class hierarchies, and customize behavior without
# rewriting everything. You can customize by extending existing methods
# or overriding them in the child class.

# single inheritance
# override the method in the child class
# extends the functionality of the parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound.'

class Dog(Animal):
    # override the method in the child class
    def sound(self):
        return f'{self.name} barks.'

    # extends the functionality of the parent class
    # use super() to call the parent class's method and extend it
    def bark(self):
        base = super().sound()
        return f'{base} Also, {self.name} is a good boy.'


# multiple inheritance
class Walker:
    def walker(self):
        return 'I can walk on land'

class Swimmer:
    def swimmer(self):
        return 'I can swim in water'

# Amphibian inherits from both Walker and Swimmer
class Amphibian(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I'm {self.name} the frog. {self.walker()} and {self.swimmer()}"

def main():
    animal = Animal('Frog')
    print(animal.sound())
    dog = Dog('Rex')
    print(dog.sound())
    print(dog.bark())
    amphibian = Amphibian('Froggy')
    print(amphibian.introduce())

if __name__ == "__main__":
    main()