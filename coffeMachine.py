resources = {"water": 2000, "milk": 1000, "coffee": 800}


recipes = {
  "espresso": {"water": 50, "milk": 0, "coffee": 18},
  "latte": {"water": 200, "milk": 150, "coffee": 24},
  "cappuccino": {"water": 250, "milk": 100, "coffee": 24}
}


while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino/report/exit): ").lower()
    
    if user_choice == "exit":
        print("Exiting the program. Goodbye!")
        break
    
    print(f"You chose: {user_choice}")

    if user_choice == espresso.lower():



