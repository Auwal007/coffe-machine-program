# Menu of available drinks
MENU = {
    "espresso": {"water": 50, "coffee": 18, "cost": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0},
}

# Initial resources available in the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def print_report():
    """Prints the current resources and money in the machine."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")

def check_resources(order):
    """Checks if there are enough resources to make the ordered drink."""
    for item, amount in MENU[order].items():
        if item != 'cost' and amount > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Processes the coins inserted by the user and returns the total amount."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return quarters + dimes + nickels + pennies

def make_coffee(order):
    """Deducts ingredients from resources and adds money for the ordered drink."""
    for item, amount in MENU[order].items():
        if item != 'cost':
            resources[item] -= amount
    resources["money"] += MENU[order]["cost"]
    print(f"Here is your {order}. Enjoy!")

def coffee_machine():
    """Main function to run the coffee machine."""
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
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
