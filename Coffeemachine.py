#AMAZING DIGITAL COFFEE MACHINE

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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def start(current_money):
    def money():
        user_money = Quarters * 0.25 + Dimes * 0.10 + Nickles * 0.05 + pennies * 0.01
        return user_money

    user_choice = input(
        "What would you like? (espresso/latte/cappuccino/report)").lower()
    if user_choice == 'latte' or user_choice == 'cappuccino':
        if resources['water'] >= MENU[user_choice]['ingredients'][
                'water'] and resources['milk'] >= MENU[user_choice][
                    'ingredients']['milk'] and resources['coffee'] >= MENU[
                        user_choice]['ingredients']['coffee']:
            pass
        elif resources['water'] < MENU[user_choice]['ingredients'][
                'water'] and resources['milk'] < MENU[user_choice][
                    'ingredients']['milk']:
            print("Sorry not enough water and milk.")
            start(current_money)
        elif resources['water'] < MENU[user_choice]['ingredients']['water']:
            print("Sorry not enough water.")
            start(current_money)
        elif resources['milk'] < MENU[user_choice]['ingredients']['milk']:
            print("Sorry not enough milk.")
            start(current_money)
        elif resources['coffee'] < MENU[user_choice]['ingredients']['coffee']:
            print("Sorry not enough coffee.")
            start(current_money)
    elif user_choice == 'espresso':
        if resources['water'] >= MENU[user_choice]['ingredients'][
                'water'] and resources['coffee'] >= MENU[user_choice][
                    'ingredients']['coffee']:
            pass
        elif resources['water'] < MENU[user_choice]['ingredients']['water']:
            print("Sorry not enough water.")
            start(current_money)
        elif resources['coffee'] < MENU[user_choice]['ingredients']['coffee']:
            print("Sorry not enough coffee.")
            start(current_money)
    elif user_choice == 'report':
        print(
            f"Water:{resources['water']}\nMilk:{resources['milk']}\nCoffee:{resources['coffee']}\nMoney:${current_money}"
        )
        start(current_money)

    if user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        print("Please enter coins.")
        Quarters = int(input("How many Quarters: "))
        Dimes = int(input("How many dimes: "))
        Nickles = int(input("How many nickles: "))
        pennies = int(input("How many pennies: "))
        user_money = money()

        if user_money >= MENU[user_choice]['cost']:
            change = user_money - MENU[user_choice]['cost']
            change = "{:.2f}".format(change)
            if change == 0.00:

                print(f"Here is your {user_choice} enjoy! ")
            else:
                print(f"Here is ${change} in change.")
                print(f"Here is your {user_choice} enjoy! ")
            if user_choice == 'latte' or user_choice == 'cappuccino':
                resources.update({
                    'water':
                    resources['water'] -
                    MENU[user_choice]['ingredients']['water']
                })
                resources.update({
                    'coffee':
                    resources['coffee'] -
                    MENU[user_choice]['ingredients']['coffee']
                })
                resources.update({
                    'milk':
                    resources['milk'] -
                    MENU[user_choice]['ingredients']['milk']
                })
            else:
                resources.update({
                    'water':
                    resources['water'] -
                    MENU[user_choice]['ingredients']['water']
                })
                resources.update({
                    'coffee':
                    resources['coffee'] -
                    MENU[user_choice]['ingredients']['coffee']
                })
            money = current_money + MENU[user_choice]['cost']
            start(money)

        else:
            print("Sorry not enough money. Money refunded.")
            start(current_money)


start(current_money=0)
