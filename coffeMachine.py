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
    },
}
# Function to check and print resources report
def print_report(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

# Function to check if the ingredients for a selected coffe are available 
def check_resources(order, resources):
    ingredients = MENU[order]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

# Function to calculate the coins for a selected coffee
def process_coins():
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def coffee_machine():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0,
    }
    is_on = True

def make_coffee(order, resources):
    ingredients = MENU[order]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    resources["money"] += MENU[order]["cost"]
    print(f"Here is your {order}. Enjoy!")
