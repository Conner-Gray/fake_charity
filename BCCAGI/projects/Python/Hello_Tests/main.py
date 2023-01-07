def say_hello():
    return "Hello World!"


def hey_you(name):
    return f"Hello, {name}!"


def age_in_2050(age):
    age = 2050 - age
    return f"You will be {age} in 2050!"


def can_i_take_your_order(burgers, fries, drinks):

    burgerPrice = float(burgers) * 4.5
    friesPrice = float(fries) * 1.5
    drinkPrice = float(drinks) * 1.0
    totalPrice = burgerPrice + friesPrice + drinkPrice
    return (burgerPrice, friesPrice, drinkPrice, totalPrice)


if __name__ == "__main__":
    print(
        """Welcome to Good Burger.
Home of the Good Burger.
Can I take your order?"""
    )

    burgers = input("Good Burgers ($4.5): ")
    while burgers.isdigit() == False:
        burgers = input("Quantity must be a positive number. ")

    fries = input("\nFrench Fries ($1.5): ")
    while fries.isdigit() == False:
        fries = input("Quantity must be a positive number. ")

    drinks = input("\nDrinks       ($1.0): ")
    while drinks.isdigit() == False:
        drinks = input("Quantity must be a positive number. ")
    burgerPrice, friesPrice, drinkPrice, totalPrice = can_i_take_your_order(
        burgers, fries, drinks
    )

    print("Here is your receipt:")
    print("- Good Burgers $4.5 x", burgers, "= $" + str(burgerPrice))
    print("- French Fries $1.5 x", fries, "= $" + str(friesPrice))
    print("- Drinks       $1.0 x", drinks, "= $" + str(drinkPrice))
    print("TOTAL = ${:.2f}".format(totalPrice))
