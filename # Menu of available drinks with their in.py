# Menu of available drinks with their ingredients and cost
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


# Initial resources available in the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

"""Prints the current resources and money in the machine."""
def print_report():
    print("Current resources:")
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${resources['money']:}")

"""Checks if there are enough resources to make the selected coffee."""
def check_resources(drink):
    for ingredient in MENU[drink]:
        if ingredient != 'cost' and MENU[drink][ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

"""Prompts user to insert coins and returns total amount inserted."""
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total_money = quarters + dimes + nickels + pennies
    return total_money

"""Deducts ingredients from resources and adds money for the selected drink."""
def make_coffee(drink):
    for ingredient in MENU[drink]:
        if ingredient != 'cost':
            resources[ingredient] -= MENU[drink][ingredient]
    
    resources["money"] += MENU[drink]["cost"]
    print(f"Making your {drink}...")
    print(f"Here is your {drink}. Enjoy!")

"""Main function to run the coffee machine."""
def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        
        if choice == "off":
            print("Turning off the coffee machine.")
            break
        
        elif choice == "report":
            print_report()
        
        elif choice in MENU:
            if check_resources(choice):
                payment = process_coins()
                
                if payment >= MENU[choice]["cost"]:
                    change = round(payment - MENU[choice]["cost"], 2)
                    if change > 0:
                        print(f"Here is ${change} in change.")
                    make_coffee(choice)
                else:
                    print("Sorry, that's not enough money. Money refunded.")
        
        else:
            print("Invalid choice. Please select a valid option.")

# Start the coffee machine program
coffee_machine()
