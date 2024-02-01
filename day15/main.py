from data import MENU

is_continue = True
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
        else:
            return True


def calculate_value():
    total_value = int(input("How many quarters: ")) * coins["quarters"]
    total_value += int(input("How many dimes: ")) * coins["dimes"]
    total_value += int(input("How many nickles: ")) * coins["nickles"]
    total_value += int(input("How many pennies: ")) * coins["pennies"]
    return total_value


def coffee_make(order_ingredients, total_value):
    for item in order_ingredients:
        resources[item] = resources[item] - order_ingredients[item]
    if total_value > MENU[user_choice]["cost"]:
        return total_value - MENU[user_choice]["cost"]
    else:
        return 0


while is_continue:
    change = 0
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'off':
        is_continue = False
        print("Coffee machine turn offed")
    elif user_choice == 'report':
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ")
    else:
        order_ingredients = MENU[user_choice]["ingredients"]
        if is_resource_sufficient(order_ingredients):
            total_value = calculate_value()
            if MENU[user_choice]["cost"] <= total_value:
                change = coffee_make(order_ingredients, total_value)
                if change == 0:
                    print(f"Here is your {user_choice}. Enjoy!")
                else:
                    change = round(change, 2)
                    print(f"Here is your {user_choice}. Enjoy!")
                    print(f"Here is ${change} dollars in change.")
            else:
                print(f"Sorry that's not enough money. Money refunded. ${total_value}")
