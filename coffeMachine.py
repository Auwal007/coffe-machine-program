# TOtal amount of resources ingredient present in the coffe machine
resources = {"water": 2000, "milk": 1000, "coffee": 800}
# Amount of ingredients needed to produce each resources
recipes = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18},
    "latte": {"water": 200, "milk": 150, "coffee": 24},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24}
}

# Cost of each coffee
costs = {"espresso": 2.5, "latte": 3.0, "cappuccino": 3.5}

# Whilee loop for the whole coffee processing
while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino/report/exit): ").lower()
    
    if user_choice == "exit":
        print("Exiting the program. Goodbye!")
        break
    
    elif user_choice == "report":
        print("\nResources Report:")
        for resource, amount in resources.items():
            print(f"{resource.capitalize()}: {amount}ml")
        print()
        continue

    elif user_choice in recipes:
        recipe = recipes[user_choice]
        cost = costs[user_choice]
        
        # Check if resources are sufficient
        if resources["water"] < recipe["water"]:
            print("Sorry, there is not enough water.")
            continue
        if resources["milk"] < recipe["milk"]:
            print("Sorry, there is not enough milk.")
            continue
        if resources["coffee"] < recipe["coffee"]:
            print("Sorry, there is not enough coffee.")
            continue
        
        
