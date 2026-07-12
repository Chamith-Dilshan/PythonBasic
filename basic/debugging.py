import pdb

#  debugging techniques (print() statements, the pdb module, and IDE tools)

def divide_me(a, b):
    pdb.set_trace()
    print("a:",a, "b:",b)
    result = a / b
    return result

if __name__ == "__main__":
    print(divide_me(1,4))
    print(divide_me(13, 2))