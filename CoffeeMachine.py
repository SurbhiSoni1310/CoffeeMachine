from data import MENU
from data import resources
from art import logo
from time import sleep
import os
continue_loop = True
money_earned = 0


def end():
    sleep(10)
    os.system("cls")


def coffee(sample_choice):
    if sample_choice == "report":
        print("The water left is : " + str(resources["water"])+"ml")
        print("The coffee left is : " + str(resources["coffee"])+"gm")
        print("The milk left is : " + str(resources["milk"])+"ml")
        print("The money earned is : " + str(money_earned)+"$")
        end()
        return True
    elif sample_choice in ["espresso", "latte", "cappuccino"]:
        return money(sample_choice)
    else:
        print("Wrong option selected. Program Terminated")
        end()
        return False


def money(option):
    global money_earned
    if check_resources(option):
        print("Please insert coins")
        quarters = int(input("How many Quarters ? "))
        dimes = int(input("How many dimes ? "))
        nickles = int(input("How many nickles ? "))
        pennies = int(input("How many pennies ? "))
        total_amount = quarters * 0.25 + nickles * 0.05 + dimes * 0.1 + pennies * 0.01
        if MENU[option]["cost"] > total_amount:
            print("Sorry that's not enough money. Money Refunded")
            end()
            return True
        elif MENU[option]["cost"] < total_amount:
            money_earned += MENU[option]["cost"]
            change = round(total_amount - MENU[option]["cost"], 2)
            resources["water"] -= MENU[option]["ingredients"]["water"]
            resources["coffee"] -= MENU[option]["ingredients"]["coffee"]
            resources["milk"] -= MENU[option]["ingredients"]["milk"]
            print(f"Here is your change {change}$")
            print(f"Here is your {option}. Enjoy!!")
            end()
            return True
        else:
            money_earned += MENU[option]["cost"]
            resources["water"] -= MENU[option]["ingredients"]["water"]
            resources["coffee"] -= MENU[option]["ingredients"]["coffee"]
            resources["milk"] -= MENU[option]["ingredients"]["milk"]
            print(f"Here is your {option}. Enjoy!!")
            end()
            return True
    else:
        return True


def check_resources(sample_option):
    if MENU[sample_option]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water")
        end()
        return False
    elif MENU[sample_option]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee")
        end()
        return False
    elif MENU[sample_option]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk")
        end()
        return False
    else:
        return True


while continue_loop:
    print("Welcome to the coffee machine")
    print(logo)
    choice = input("Do you want espresso/latte/cappuccino ? ")
    continue_loop = coffee(choice)
