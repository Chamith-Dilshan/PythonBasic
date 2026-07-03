def main():
    numbers = [1, 2, 3, 4, 5]

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)

    # Don't use lambda if it gets complex
    result = (lambda x: (x ** 2 + 2 * x - 1) if x > 0 else (x ** 3 - x + 4))(3)
    print(result)

    def calculate_expression(x):
        if x > 0:
            return x ** 2 + 2 * x - 1
        else:
            return x ** 3 - x + 4

    print(calculate_expression(3))


if __name__ == "__main__":
    main()