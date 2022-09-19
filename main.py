# global variables ( if any)

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

bank = 0

# function definitions


def report():
    print(
        f"Water: {resources['water']} ml \nMilk: {resources['milk']} ml \nCoffee: {resources['coffee']} ml \nProfit: {bank}")


def calculate(choice):
    quarter_amount = int(input("how many quarters?: "))
    dime_amount = int(input("how many dimes?: "))
    nickle_amount = int(input("how many nickels?: "))
    penny_amount = int(input("how many pennies?: "))

    quarter_amount = float(quarter_amount) * 0.25
    dime_amount = float(dime_amount) * 0.10
    nickle_amount = float(nickle_amount) * 0.05
    penny_amount = float(penny_amount) * 0.01

    sum = quarter_amount + dime_amount + nickle_amount + penny_amount
    if sum >= MENU[choice]['cost']:
        difference = round(sum - MENU[choice]['cost'], 3)
        print(f"here is your change: $ {difference}")
        return sum
    else:
        print("sorry that's not enough money. money refunded.")
        start()


def new_resources(choice):
    global resources
    for ingredient in resources:
        if choice == "espresso":
            if ingredient == "milk":
                print("no milk")
            else:
                resources[ingredient] -= MENU[choice]['ingredients'][ingredient]
        else:
            resources[ingredient] -= MENU[choice]['ingredients'][ingredient]


def give_coffee(choice):
    print(f"here is your {choice} ☕️. enjoy!")


def enough_resources():
    for ingredient in resources:
        if resources[ingredient] <= 0:
            print(f"I apologize, the coffee machine is out of {ingredient}.")
            return False
    return True


def start():
    global bank
    global resources
    coffee_choice_true = False
    while coffee_choice_true != True:
        coffee_lover_choice = input(
            "Welcome to coffee machine. \nWhat would you like? (espresso/latte/cappuccino/report): ").lower()
        if coffee_lover_choice != "espresso" and coffee_lover_choice != "latte" and coffee_lover_choice != "cappuccino" and coffee_lover_choice != "report":
            print("incorrect input: only input espresso, latte, cappuccino or report")
        else:
            coffee_choice_true = True

    if coffee_lover_choice == "report":
        report()
        start()
    else:
        bank = bank + calculate(coffee_lover_choice)
        new_resources(coffee_lover_choice)
        can_make = enough_resources()
        if can_make == False:
            print("turning off for refill process.")
            exit()
        give_coffee(coffee_lover_choice)
        start()


# timeline


start()
