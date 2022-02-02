# Coffee Machine Code
import menu as menu

# Global Variable
RESOURCES_CAPACITY = menu.resources


def check_price(choice, v):
    price = menu.MENU[choice]["cost"]
    if price > v:
        return False
    else:
        return True


def print_report(res):
    for key, val in res.items():
        print(key, ":", val)


def check_resources(water, milk, coffee, res):
    if res["water"] >= water and res["milk"] >= milk and res["coffee"] >= coffee:
        return True
    else:
        return False


def insufficient_status(c, res):
    insufficient_lst = []
    c_water = menu.MENU[c]["water"]
    c_milk = menu.MENU[c]["milk"]
    c_coffee = menu.MENU[c]["coffee"]


def update_resources(water, milk, coffee, res):
    res["water"] -= water
    res["milk"] -= milk
    res["coffee"] -= coffee


def run():
    while True:
        coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if coffee_choice == 'report':
            print_report(RESOURCES_CAPACITY)
        elif coffee_choice != 'espresso' and coffee_choice != 'latte' and coffee_choice != 'cappuccino':
            print("Coffee type not supported. Try again.")
        else:
            water_req = menu.MENU[coffee_choice]["ingredients"]["water"]
            milk_req = menu.MENU[coffee_choice]["ingredients"]["milk"]
            coffee_req = menu.MENU[coffee_choice]["ingredients"]["coffee"]
            if check_resources(water_req, milk_req, coffee_req, RESOURCES_CAPACITY):
                print("Please insert coins.")
                while True:
                    coffee_price = menu.MENU[coffee_choice]["cost"]
                    print("Coffee Price: ", coffee_price)
                    quarter_input = int(input("    How many quarters?: "))
                    dime_input = int(input("    How many dimes: "))
                    nickles_input = int(input("    How many nickles?: "))
                    pennies_input = int(input("    How many pennies?: "))
                    coin_value = quarter_input * 0.25 + dime_input * 0.10 + nickles_input * 0.05 + pennies_input * 0.01
                    if check_price(coffee_choice, coin_value):
                        update_resources(water_req, milk_req, coffee_req, RESOURCES_CAPACITY)
                        change = round(coin_value - coffee_price, 2)
                        print(f"Here is $ {change} in change.")
                        break
                    else:
                        print("Sorry that's not enough money. Money refunded")
                        try_again_input = input("Do you want to go back to coffee selection? (y / n): ").lower()
                        if try_again_input == 'n':
                            break
                        elif try_again_input == 'y':
                            continue
                        else:
                            print("Incorrect Input, Shutting down.")
                            break
            else:
                print("Sorry there is not enough")



run()
