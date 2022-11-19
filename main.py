from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

should_continue = True

while should_continue:
    options = menu.get_items()
    coffee_type = input(f"What would you like? ({options}): ")
    if coffee_type == 'off':
        should_continue = False
    elif coffee_type == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(coffee_type)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

