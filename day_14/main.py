from click import option
import game_data as gd
import logo as logo
import random as rand
from os import system, name

# Setting up imported files
data = gd.data
main_logo = logo.logo
vs_logo = logo.vs

# Setting up global variables
FINAL_SCORE = 0


## List of functions

# Function 1: Clear the terminal

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Function 2: print the random element from the dictionary list
def choose_element(d):
    element = rand.choice(d)
    return element


# Game Start

# choice = input(print("Play game? Type 'y' or 'n': "))
# while choice == 'y':
def basic_game_run(op_a, op_b):
    clear()
    print(main_logo)

    print(f"Compare A: {op_a['name']}, a {op_a['description']}, from {op_a['country']}.")

    print(vs_logo)

    print(f"Against B: {op_b['name']}, a {op_b['description']}, from {op_b['country']}.")


def compare_followers(op_a, op_b):
    if op_a['follower_count'] > op_b['follower_count']:
        return 'a'
    else:
        return 'b'


# Records user input
def inital_load():
    global FINAL_SCORE

    option_a = choose_element(data)
    option_b = choose_element(data)

    basic_game_run(option_a, option_b)

    # Debug line
    print(
        f"Option A Follower Count: {option_a['follower_count']}, Option B Follower Count: {option_b['follower_count']}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ")

    # Check whether the user chose correct answer
    result = compare_followers(option_a, option_b)
    if user_choice.lower() == result:
        FINAL_SCORE += 1
        loop_sequence(option_a, option_b)


def loop_sequence(op_a, op_b):
    global FINAL_SCORE

    while True:
        op_a = op_b
        op_b = choose_element(data)
        if op_a == op_b:
            op_b = choose_element(data)

        basic_game_run(op_a, op_b)

        choice = input("Who has more followers? Type 'A' or 'B': ")

        print(f"Option A Follower Count: {op_a['follower_count']}, Option B Follower Count: {op_b['follower_count']}")

        if choice.lower() != compare_followers(op_a, op_b):
            print(f"Sorry, that's wrong. Final score: {FINAL_SCORE}")
            break
        else:
            FINAL_SCORE += 1


print("Out")

inital_load()
