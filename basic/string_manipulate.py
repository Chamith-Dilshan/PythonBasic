def main():
    multiline_string = """
    This is a Multiline
    sting
    example
    """
    print("MultiLine String: ",multiline_string)

    escaped_string = "This is a \"escaped\" string"
    print("Escaped String: ",escaped_string)

    len_string = len(multiline_string)
    print("Length of String: ",len_string)

    get_type = type(multiline_string)
    print("Type of String: ",get_type)

    check_type = isinstance(multiline_string, str)
    print("Check Type: ",check_type)

    check_string_contains = "multiline" in multiline_string
    print("Check String Contains: ",check_string_contains)

    get_index_char = multiline_string[-2]
    print("Get Index Char: ",get_index_char)

    get_slice = multiline_string[0:5]
    print("Get Slice: ",get_slice)

    get_slice_from_index = multiline_string[5:]
    print("Get Slice From Index: ",get_slice_from_index)

    print("\n//////////////////////// String Interpolation  ////////////////////////////")

    name = "John Doe"
    age = 30
    print(f"Hello {name}, you are {age} years old.")

    print("\n//////////////////////// String Concatenation   ////////////////////////////")

    print("Hello " + name + ", you are " + str(age) + " years old.")

    print("\n//////////////////////// String Slice   ////////////////////////////")

    print("First 5 characters: ", name[:5])
    print("Last 5 characters: ", name[-5:])
    print("Every 2nd character: ", name[::2])
    print("Reversed string: ", name[::-1])

    print("\n//////////////////////// Common String Methods  ////////////////////////////")
    print("Upper Case: ", name.upper())
    print("Lower Case: ", name.lower())
    print("Capitalize: ", name.capitalize())
    print("Replace: ", name.replace("John", "Jane"))
    print("Split: ", name.split())
    print("Count: ", name.count("o"))
    print("Find: ", name.find("o"))
    print("Index: ", name.index("o"))
    print("Strip: ", name.strip())
    print("Start with: ", name.startswith("John"))
    print("End with: ", name.endswith("Doe"))
    print("Is Alphabet: ", name.isalpha())
    print("Is Number: ", name.isnumeric())
    print("Is Alphanumeric: ", name.isalnum())
    print("Is Space: ", name.isspace())
    print("Is Title: ", name.istitle())
    print("Is Lower: ", name.islower())
    print("Is Upper: ", name.isupper())
    print("Is Decimal: ", name.isdecimal())
    print("Is Digit: ", name.isdigit())
    print("Is Identifier: ", name.isidentifier())
    print("Is Printable: ", name.isprintable())
    print("Is ASCII: ", name.isascii())
    print("Is Alphanumeric: ", name.isalnum())

if __name__ == "__main__":
    main()
