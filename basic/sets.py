# don't store duplicate values.
# Sets are mutable and unordered, which means that their elements are not stored in
# any specific order, so you cannot use indices or keys to access them
# support mathematical set operations, including union, intersection, difference,
# and symmetric difference.

def main():
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    numbers.add(10)

    print(numbers)
    # Remove will give error if the value is not present in the set
    numbers.remove(10)
    print(numbers)
    # discard will not give error if the value is not present in the set
    numbers.discard(11)
    print(numbers)

    set_1 = {1, 2, 3}
    set_2 = {3, 4, 5}
    print('union: ',set_1.union(set_2))
    print('union: ',set_1 | set_2)
    print('intersection: ',set_1.intersection(set_2))
    print('intersection: ',set_1 & set_2)
    print('difference: ',set_1.difference(set_2))
    print('difference: ',set_1 - set_2)
    print('symmetric_difference: ',set_1.symmetric_difference(set_2))
    print('symmetric_difference: ',set_1 ^ set_2)
    print('issubset: ',set_1.issubset(set_2))
    print('issuperset: ',set_1.issuperset(set_2))
    print('isdisjoint: ',set_1.isdisjoint(set_2))

if __name__ == "__main__":
    main()
