def main():
    """
    A tuple is an immutable, ordered collection that cannot be changed after creation,
    while a list is a mutable, ordered collection that can be modified by adding,
    removing, or changing elements
    """
    cities = ['Los Angeles', 'London', 'Tokyo']
    print('First index value of the list:',cities[0])

    name = 'Chamith Dilshan'

    # Converting to list and tuple
    print('Convert to a list:',list(name))
    print('Convert to a tuple:',tuple(name))

    # Length
    name_list = list(name)
    print('Length of name:',len(name_list))

    # delete and check
    del cities[1]
    print('Is London in the list:','London' in cities)

    # append
    cities.append('New York')
    cities.append('Colombo')

    # Unpacking
    city_1, city_2, *rest = cities
    print('First City:',city_1)
    print('Second City:',city_2)
    print('Rest of the cities:',rest)

    # Slicing
    print('Cities:',cities[1:3:2])

    # Add multiple elements from one list to another
    cities_2 = ['Delhi', 'Mumbai']
    cities.extend(cities_2)
    print('Cities:',cities)

    #  Insert an element at a specific index in a list
    cities.insert(2, 'Paris')
    print('Cities:',cities)

    # Remove first occurrence element from a list
    cities.remove('Paris')
    print('Cities:',cities)

    # Reverse a list
    cities.reverse()
    print('Reversed Cities:',cities)

    # Sort a list
    cities.sort()
    print('Sorted Cities:',cities)

    # Returns a new sorted list instead of modifying the original list
    print('Sorted Cities:',sorted(cities))

    # Remove an element at a specific index
    cities.pop(2)
    print('Cities:',cities)

    # Count the number of occurrences of an element in a list
    print('Number of occurrences of "Tokyo" in the list:', cities.count('Tokyo'))

    # Index of an element in a list
    print('Index of "Tokyo" in the list:', cities.index('Tokyo'))

    # Empty the list
    cities.clear()
    print('Cities:',cities)

    # Sorting a tuple
    numbers = (1, 2, 3, 4, 5)
    print('Sorted Numbers:', sorted(numbers,key=lambda x: x, reverse=True))


if __name__ == "__main__":
    main()