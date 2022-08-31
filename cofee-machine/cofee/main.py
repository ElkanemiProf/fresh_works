from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    drink = menu.get_items()
    choice = input(f"kindly choose the option that best suits you: ({drink})")
    if choice == "report":
        coffe_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        drinks = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drinks):
            money_machine.make_payment(drinks.cost)
            coffe_maker.make_coffee(drinks)

