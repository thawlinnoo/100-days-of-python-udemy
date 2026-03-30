# from coffee_machine import MENU
# from coffee_machine import resources

# water = resources["water"]
# milk = resources["milk"]
# coffee = resources["coffee"]

# money = 0

# required_water_espresso = MENU["espresso"]["ingredients"]["water"]
# required_coffee_espresso = MENU["espresso"]["ingredients"]["coffee"]

# required_water_latte = MENU["latte"]["ingredients"]["water"]
# required_milk_latte = MENU["latte"]["ingredients"]["milk"]
# required_coffee_latte = MENU["latte"]["ingredients"]["coffee"]

# required_water_cappuccino = MENU["cappuccino"]["ingredients"]["water"]
# required_milk_cappuccino = MENU["cappuccino"]["ingredients"]["milk"]
# required_coffee_cappuccino = MENU["cappuccino"]["ingredients"]["coffee"]

# required_coin_espresso = MENU["espresso"]["cost"]
# required_coin_latte = MENU["latte"]["cost"]
# required_coin_cappuccino = MENU["cappuccino"]["cost"]

# def check_resources(user_choice):
#     if user_choice == "espresso":
#         if water>=required_water_espresso and coffee>=required_coffee_espresso:
#             return True
           
#         else:
#             if water<required_water_espresso:
#                 print("Not enough water")
#             if coffee<required_coffee_espresso:
#                 print("Not enough coffee")
            
#     elif user_choice == "latte":
#         if water>=required_water_latte and milk>=required_milk_latte and coffee>=required_coffee_latte:
#             return True

            
#         else:
#             if water<required_water_latte:
#                 print("Not enough water")
#             if milk<required_milk_latte:
#                 print("Not enough milk")
#             if coffee<required_coffee_latte:
#                 print("Not enough coffee")
            
#     elif user_choice == "cappuccino":
#         if water>=required_water_cappuccino and milk>=required_milk_cappuccino and coffee>=required_coffee_cappuccino:
#             return True

            
#         else:
#             if water<required_water_cappuccino:
#                 print("Not enough water")
#             if milk<required_milk_cappuccino:
#                 print("Not enough milk")
#             if coffee<required_coffee_cappuccino:
#                 print("Not enough coffee")



# def check_coin(user_choice):
#     global money
#     print("Please insert coins")
#     quarter_quantity = int(input("How many quarters: "))
#     dime_quantity = int(input("How many dimes: "))
#     nickel_quantity = int(input("How many nickels: "))
#     penny_quantity = int(input("How many pennies: "))
#     user_inserted_value = (quarter_quantity*0.25) + (dime_quantity*0.10) + (nickel_quantity*0.05) + (penny_quantity*0.01)
#     if user_choice == "espresso":
#         if user_inserted_value<required_coin_espresso:
#             print("sorry, not enough money, money refunded")
#         else:
#             money += required_coin_espresso
#             if user_inserted_value>required_coin_espresso:
#                 print(f"here is {round(user_inserted_value-required_coin_espresso,2)} in change")
#                 return True
#             elif user_inserted_value==required_coin_espresso:
#                 return True
#     elif user_choice == "latte":
#         if user_inserted_value<required_coin_latte:
#             print("sorry, not enough money, money refunded")
#         else:
#             money += required_coin_latte
#             if user_inserted_value>required_coin_latte:
#                 print(f"here is {round(user_inserted_value-required_coin_latte,2)} in change")
#                 return True
#             elif user_inserted_value==required_coin_latte:
#                 return True
#     elif user_choice == "cappuccino":
#         if user_inserted_value<required_coin_cappuccino:
#             print("sorry, not enough money, money refunded")
#         else:
#             money += required_coin_cappuccino
#             if user_inserted_value>required_coin_cappuccino:
#                 print(f"here is {round(user_inserted_value-required_coin_cappuccino,2)} in change")
#                 return True
#             elif user_inserted_value==required_coin_cappuccino:
#                 return True

# def make_coffee(user_choice):
#     global water, milk, coffee
#     if user_choice == "espresso":
#             water -= required_water_espresso
#             coffee -= required_coffee_espresso
#             print("here is ur espresso")
#     elif user_choice == "latte":
#             water -= required_water_latte
#             milk -= required_milk_latte
#             coffee -= required_coffee_latte
#             print("here is ur latte")
#     elif user_choice == "cappuccino":
#             water -= required_water_cappuccino
#             milk -= required_milk_cappuccino
#             coffee -= required_coffee_cappuccino
#             print("here is ur cappuccino")
    

# def coffee_machine():
#     power_off = False
#     while not power_off :
#         user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
#         if user_input == "report":
#             print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: ${money}")
#         elif user_input == "off":
#             power_off = True
#         else:
#             if check_resources(user_input):
#                 if check_coin(user_input):
#                     make_coffee(user_input)   

            
# coffee_machine()
        

#better version (use "in" to check)

from coffee_machine import MENU, resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0


def check_resources(user_choice):
    required_ingredients = MENU[user_choice]["ingredients"]
    enough = True
    if "water" in required_ingredients and water<required_ingredients["water"]:
        print("Not enough water")
        enough = False
    if "milk" in required_ingredients and milk<required_ingredients["milk"]:
        print("Not enough milk")
        enough = False
    if "coffee" in required_ingredients and coffee<required_ingredients["coffee"]:
        print("Not enough coffee")
        enough = False
    return enough


def check_coin(user_choice):
    global money
    print("Please insert coins")
    quarter_quantity = int(input("How many quarters: "))
    dime_quantity = int(input("How many dimes: "))
    nickel_quantity = int(input("How many nickels: "))
    penny_quantity = int(input("How many pennies: "))
    user_inserted_value = (quarter_quantity*0.25) + (dime_quantity*0.10) + (nickel_quantity*0.05) + (penny_quantity*0.01)
    required_coin = MENU[user_choice]["cost"]
    if user_inserted_value<required_coin:
        print("sorry, not enough money, money refunded")
        return False
    else:
        money += required_coin
        if user_inserted_value>required_coin:
            print(f"here is {round(user_inserted_value-required_coin,2)} in change")
            return True
        elif user_inserted_value==required_coin:
            return True
        
def make_coffee(user_choice):
    global water, milk, coffee
    required_ingredients = MENU[user_choice]["ingredients"]
    if "water" in required_ingredients:
        water -= required_ingredients["water"]
    if "milk" in required_ingredients:
        milk -= required_ingredients["milk"]
    if "coffee" in required_ingredients:
        coffee -= required_ingredients["coffee"]

    print(f"Here.. enjoy your {user_choice}")


def coffee_machine():
    power_off = False
    while not power_off :
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == "report":
            print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: ${money}")
        elif user_input == "off":
            power_off = True
        else:
            if check_resources(user_input):
                if check_coin(user_input):
                    make_coffee(user_input) 



coffee_machine()

