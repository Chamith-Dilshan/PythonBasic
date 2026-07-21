# Mangling
# A process in which Python changes __attribute into _ClassName__attribute
# to avoid accidental overriding in subclasses.

# Prefixing an attribute with a double underscore triggers Python's name mangling process,
# in which Python internally renames the attribute by adding an underscore and
# the class name as a prefix, turning __attribute into _ClassName__attribute.

# A single underscore is just a convention, while a double underscore triggers name mangling.
# if you're working with a class that will be inherited, you should use a double underscore
# so the attribute from the parent doesn't get overridden.
# otherwise, The child class completely overrides the parent class attribute, and the parent's data is lost.

class Example:
    def __init__(self, internal, private):
        self._internal = internal
        self.__private = private

def main():
    example1 = Example(
        'I can be accessed from outside the class, but should not',
        'I cannot be accessed directly from outside the class'
    )

    print(example1.__dict__)
    print(example1._Example__private) # you can access the private attribute

if __name__ == "__main__":
    main()