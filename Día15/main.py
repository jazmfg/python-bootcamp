
MENU = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0

def report():
    """Print current resource and money report."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources.get('milk', 0)}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")

def check_resources(order_ingredients):
    """Check if there are enough ingredients to make the drink."""
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Return the total amount of money from inserted coins."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def make_coffee(drink_name, ingredients):
    """Deduct the required ingredients from the resources and serve the coffee."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        report()
    elif choice in MENU:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if payment >= drink["cost"]:
                change = round(payment - drink["cost"], 2)
                if change > 0:
                    print(f"Here is ${change:.2f} in change.")
                money += drink["cost"]
                make_coffee(choice, drink["ingredients"])
            else:
                print("Sorry, that's not enough money. Money refunded.")
    else:
        print("Invalid option. Please choose espresso, latte, or cappuccino.")