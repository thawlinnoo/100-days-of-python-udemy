from menu import Menu 
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

power_on = True
menu = Menu() 
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while power_on:
    user_choice = input(f"What do you wanna drink? {menu.get_items()}: ").lower()
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        power_on = False
    else:
        drink = menu.find_drink(user_choice)
        if not coffee_maker.is_resource_sufficient(drink):
            continue
        else:
            if not money_machine.make_payment(drink.cost):
                continue
            else:
                coffee_maker.make_coffee(drink)
            
        
    
    



