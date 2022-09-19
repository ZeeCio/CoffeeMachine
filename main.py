from typing import Dict

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def subtract(resources_s, menu_s):
    new_report = dict()
    for item in resources_s:
        new_report[item] = int(resources_s["key"] - menu_s["key"])
        if item not in menu_s:
            new_report += new_report[item]
    return new_report


def payment(menu_p, beverage_p):
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.01
    total += int(input("How many dimes?: ")) * 0.05
    total += int(input("How many nickles?: ")) * 0.10
    total += int(input("How many pennies?: ")) * 0.25
    return total

    if total > menu[choice[ingredients:[1]]]:
        change = total - menu[choice[ingredients:[1]]]
        print(f"Here is £{change} in change.")
    else:
        print("Amount Insufficient.")


def print_dictionary(dictionary):
    for key, value in dictionary():
        print(key, ' : ', value)




if choice == "espresso":
    espresso_report = menu[choice]
    print(espresso_report)
    print(subtract(resources_s=resources, menu_s=menu))
    payment(menu_p=menu, beverage_p=choice)
elif choice == "latte":
    latte_report = menu[choice]
    print(latte_report)
    print(subtract(resources_s=resources, menu_s=menu))
    payment(menu_p=menu, beverage_p=choice)
elif choice == "cappuccino":
    cappuccino_report = menu[choice]
    print(cappuccino_report)
    print(subtract(resources_s=resources, menu_s=menu))
    payment(menu_p=menu, beverage_p=choice)
elif choice == "report":
    print(print_dictionary(resources))
else:
    print("The coffee machine is turning off.")


# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/OFF): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "False":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Profit: £{profit}")
    else:
        drink = menu[choice]
        print(drink)
