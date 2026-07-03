def main():
    """"
    How to work with loops in Python.
    For, While, Range
    """

    # For Loop
    numbers = range(0,11)
    print(numbers)
    for number in numbers:
        print(number)

    # Nested Loop
    categories = ['Fruit', 'Vegetable']
    foods = ['Apple', 'Carrot', 'Banana']

    for category in categories:
        for food in foods:
            print(category, food)

    # While loop
    count_1 = 0
    while count_1 < 10:
        if count_1 == 3:
            count_1 += 1
            continue
        if count_1 == 5:
            break
        print('count_1:',count_1)
        count_1 += 1

    for i in range(11):
        if i == 3:
            i += 1
            continue
        if i == 5:
            break
        print('count_2:',i)
        i += 1

    numbers = list(range(2, 11, 2))
    print(numbers)

    languages = ['Spanish', 'English', 'Russian', 'Chinese']
    for index,language in enumerate(languages,1):
        print(f'Index {index} and language {language}')

    id_numbers = [1, 2, 3, 4]
    developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
    for id_number, developer in zip(id_numbers, developers):
        print(f'ID: {id_number} and Developer: {developer}')

    # List Comprehension
    numbers = [1, 2, 3, 4, 5]
    squares = [number * number for number in numbers]
    print(squares)

    even_number = [number for number in range(11) if number % 2 == 0]
    print(even_number)

    odd_even_numbers = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in range(11)]
    print(odd_even_numbers)

    # Filter
    words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

    def is_long_word(word):
        return len(word) > 5

    ling_words = list(filter(is_long_word, words))
    print(ling_words)

    # Map
    celsius = [0, 10, 20, 30, 40]

    def to_fahrenheit(temp):
        return  temp * 9/5 + 32

    fahrenheit = list(map(to_fahrenheit, celsius))
    print(fahrenheit)

    print('Total:', sum(fahrenheit,start=60))

if __name__ == "__main__":
    main()