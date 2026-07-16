# Special methods in Python, also known as "magic methods" or "dunder methods", are special
# Python methods that start and end with double underscores (__). The word "dunder" itself
# comes from double underscores (d for double, under for underscores).
# 3 + 5 is equal to 3.__add__(5)
# ex- __init__(), __len__(), __str__()

class Book:
   def __init__(self, title, pages):
       self.title = title
       self.pages = pages

class BookCorrect:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"{self.title} has {self.pages} pages."

    def __eq__(self, other):
        return self.pages == other.pages

class Cart:
   def __init__(self):
       self.items = []

   def add(self, item):
       self.items.append(item)

   def remove(self, item):
       if item in self.items:
           self.items.remove(item)
       else:
           print(f'{item} is not in cart')

   def list_items(self):
       return self.items

   def __len__(self):
       return len(self.items)

   def __getitem__(self, index):
       return self.items[index]

   def __contains__(self, item):
       return item in self.items

   def __iter__(self):
       return iter(self.items)

if __name__ == "__main__":
    book1 = Book("Built Wealth Like a Boss", 420)
    book2 = Book("Be Your Own Start", 420)

    # pyrefly: ignore [bad-argument-type]
    print(len(book1))  # TypeError: object of type 'Book' has no len()
    print(str(book1))  # <__main__.Book object at 0x102ed2900>
    print(book1 == book2)  # False even though they have the same number of pages


    book1 = BookCorrect("Built Wealth Like a Boss", 420)
    book2 = BookCorrect("Be Your Own Start", 420)

    print(len(book1))  # 420
    print(len(book2))  # 420
    print(str(book1))  # 'Built Wealth Like a Boss' has 420 pages
    print(str(book2))  # 'Be Your Own Start' has 420 pages
    print(book1 == book2)  # True

    cart = Cart()
    cart.add('Laptop')
    cart.add('Wireless mouse')
    cart.add('Ergo keyboard')
    cart.add('Monitor')
 
    for item in cart:
        print(item, end=' ')

    print(len(cart))  # 4
    print(cart[3])  # Monitor

    print('Monitor' in cart)  # True
    print('banana' in cart)  # False

    cart.remove('Ergo keyboard')

    print(cart.list_items())  # ['Laptop', 'Wireless mouse', 'Monitor']

    cart.remove('banana')  # banana is not in cart