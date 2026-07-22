# Abstraction
# is the process of hiding the implementation details of a class or object
# ABC stands for Abstract Base Class

from abc import ABC, abstractmethod

# Example one
class Animal(ABC): # Inherits from abstract base class
   @abstractmethod # Abstract method decorator
   def make_sound(self):  # The method subclasses must override
       pass

# Concrete class that will override the abstract method
class Dog(Animal):
   def make_sound(self):
       print('Woof!')

# Another concrete class that will override the abstract method
class Cat(Animal):
   def make_sound(self):
       print('Meow!')

# Another concrete class that will override the abstract method
class Monkey(Animal):
   def make_sound(self):
       print('Ooh ooh aah aah!')


# Example two
# The blueprint for any toy that can speak
class TalkingToy(ABC):
   def __init__(self, name):
       self.name = name
   @abstractmethod
   def speak(self):
       pass

class RobotToy(TalkingToy):
   def speak(self):
       print(f'{self.name} says beep boop! I am a robot!')

class TeddyBearToy(TalkingToy):
   def speak(self):
       print(f"{self.name} says hug me! I'm cuddly!")

class DinosaurToy(TalkingToy):
   def speak(self):
       print(f'{self.name} says ROOOOAR!')


def main():
    dog = Dog()
    dog.make_sound()
    cat = Cat()
    cat.make_sound()
    monkey = Monkey()
    monkey.make_sound()

    # Create toys
    rusty = RobotToy('Rusty')
    fluffy = TeddyBearToy('Fluffy')
    rex = DinosaurToy('Rex')

    toys = [rusty, fluffy, rex]
    for toy in toys:
        toy.speak()

if __name__ == "__main__":
    main()
