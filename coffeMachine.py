# Menu of available drinks with their ingredients and cost
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

# Initial resources available in the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# Prints the current resources and money in the machine.
# I assume that wate and milk are measured in millimeter while coffee in gram.
def print_report():
    print("Current resources report:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")

#Checks if there are enough resources to make the selected coffee
def check_resources(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if amount > resources.get(ingredient, 0):
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

# Prompts user to insert coins and returns total amount inserted
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total_money = quarters + dimes + nickels + pennies
    return total_money

# Deducts ingredients from resources and adds money for the selected drink.
def make_coffee(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        resources[ingredient] -= amount
    resources["money"] += MENU[drink]["cost"]
    print(f"Making your {drink}...")
    print(f"Here is your {drink}. Enjoy!")

# the main function to run the coffee machine.
def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        print(f"You choose {choice}..")
        
        if choice == "off":
            print("Turning off the coffee machine.")
            break
        
        elif choice == "report":
            print(print_report())
        
        elif choice in MENU:
            if check_resources(choice):
                payment = process_coins()
                # Processing payment and change if applicable
                if payment >= MENU[choice]["cost"]:
                    change = round(payment - MENU[choice]["cost"], 2)
                    if change > 0:
                        print(f"Here is ${change} in change.")
                    make_coffee(choice)
                else:
                    print("Sorry, that's not enough money. Money refunded..")
        
        else:
            print("Invalid coffe choice. Please select a valid option.")

# Start the coffee machine program
coffee_machine()
