def main():
    # The moduler operator
    number_1 = 20.523
    number_2 = 3.90736

    output_1 = number_1 % number_2
    print("Remainder: ", output_1)

    # Floor Division
    output_2 = number_1 // number_2
    print("Floor Division: ", output_2)

    # Exponentiation
    output_3 = number_1 ** number_2
    print("Exponentiation: ", output_3)

    # Functions
    print(f"Convert to Float : {float(50)}")
    print(F"Convert to Integer : {int(50.9)}")
    print(F"Convert to Integer : {float('5.9')}")
    print("Round a number ex:1 : ", round(number_1))
    print("Round a number ex:2 : ", round(number_2,4))
    print(f"Absolute value : {abs(-50.5)}")
    print(f"power of : {pow(2,3)}")

    # increment and decrement operators (++ and  --) does not work in Python
    # Instead of x++, you can use x += 1
    # Writing ++x in Python just applies the unary plus twice, and does not increment anything:

    number_3 = 5

    print("Try 1 : ",+number_3)  # 5
    print("Try 2 : ",++number_3)  # 5
    print("Try 3 : ",+++number_3)  # 5

    number_3 += 1

    print("Try 4 : ",number_3)  # 6


if __name__ == "__main__":
    main()