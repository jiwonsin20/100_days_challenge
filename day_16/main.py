from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mm = MoneyMachine()
cm = CoffeeMaker()
menu = Menu()

while True:
    coffee_choice = input(f"What would you like? ({menu.get_items()}): ")

    if coffee_choice == 'report':
        cm.report()
        mm.report()
    elif cm.is_resource_sufficient(menu.find_drink(coffee_choice)):
        print("Please insert coins.")
        if mm.make_payment(menu.find_drink(coffee_choice).cost):
            cm.make_coffee(menu.find_drink(coffee_choice))
