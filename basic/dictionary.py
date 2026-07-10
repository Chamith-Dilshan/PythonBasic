def main():
    picture: dict[str, str | int] = {"name": "Johnny", "age": 20, "age": 20}
    print(picture)

    print(picture["name"])
    print(picture["age"])

    print(picture.get("name", "No Name"))
    print(picture.get("gender", "No Gender"))

    print(picture.setdefault("gender", "No Gender"))

    print(picture.pop("name"))
    print(picture.pop("name", None))

    print(picture.keys())
    print(picture.values())
    print(picture.items())

    print(picture.update({"gender": "Male", "name": "Johnny"}))

    print(picture.popitem())
    print(len(picture))

    print(picture.clear())
    print(picture)

    ##################### Loop Over Dictionary #####################
    products = {
        'Laptop': 990,
        'Smartphone': 600,
        'Tablet': 250,
        'Headphones': 70,
    }

    for key,value in products.items():
        print(f'{key} costs {value}')
        products[key] = round(value * 0.9)
        print(f'New price of {key} is {products[key]}')

    for product in enumerate(products):
        print(product)
    print(products)

    for index,product in enumerate(products.items(),1):
        print(index,product)
    print(products)

if __name__ == "__main__":
    main()