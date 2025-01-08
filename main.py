import os
import time

os.environ['TERM'] = 'xterm-256color'

print("\nWelcome to the greeting program\n")

grew_up_city = input("What city you grew up in? ")

is_continue = True
while is_continue:
    pet_existence = input("Do you have any pet? (type 'y' or 'n'):  ").lower()

    if pet_existence == "y":
        pet_name = input("What is the name of your pet? ")
        print(f"\nNice to meet you. So you grew up in {grew_up_city} and the name of your pet is {pet_name}!")
        is_continue = False

    elif pet_existence == "n":
        print(f"\nNice to meet you. So you grew up in {grew_up_city} and you do not have any pet!")
        is_continue = False

    else:
        print("\nYou have entered wrong character!")
        print("Try again")
        time.sleep(1)
        os.system("clear")