# Day 1 of the 100 day challenge
# print('Day 1 - Python Print Function')
# print('The function is declared like this:')
# print('print(\'what to print\')')

# Day 1
def bandNameGenerator():
    print("Hello this is name generator")
    city_input = input("Which city did you grow up in?: ")
    pet_name = input("What's the name of your pet?: ")
    print("Your band name could be " + city_input + " " + pet_name)

# Day 2 
def dataTypeInteractive():
    two_digit_number = input("Type in two digit number: ")
    print(int(two_digit_number[0]) + int(two_digit_number[1]))

def bmi_calculator():
    height = float(input("Enter your height (m): "))
    weight = float(input("Enter your weight (kg): "))
    bmi = weight/height**2
    print("Your BMI is: ", bmi)

def calculate_age_left():
    max_age = 90
    age_input = int(input("How old are you?: "))
    in_years = max_age-age_input
    in_days = (in_years)*365
    in_weeks = in_years*52
    in_months = in_years*12
    print(f"You have {in_days} days, {in_weeks} weeks and {in_months} months left")

def tip_calculator():
    print("Welcome to tip calculator")
    total_bill = float(input("What was the total bill?: "))
    tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15?: "))
    split_bill_count = int(input("How many people to split the bill?: "))
    individual_payment = round(total_bill * (1+tip_percentage/100) / split_bill_count, 2)
    print(f"Each person should pay: ${individual_payment}")

# Day 3
def odd_or_even():
    number = int(input("Which number do you want to change?: "))
    if number % 2 == 0:
        print("Even number!")
    else:
        print("Odd number")

def bmi_version_two():
    height = float(input("Enter your height in metres: "))
    weight = float(input("Enter your weight in KG: "))
    bmi_val = round(weight / height**2)
    if bmi_val < 18.5:
        print("You are UNDERWEIGHT")
    elif bmi_val < 25:
        print("You are in normal range")
    elif bmi_val < 30:
        print("You are Overweight")
    elif bmi_val < 35:
        print("You are obese")
    else:
        print("You are CLINICALLY OBESE")

def leap_year():
    year = int(input("Which year do you want to check?: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
        else:
            print("Leap year")
    else:
        print("Not leap year")

def pizza_order():
  print("Welcome to Python Pizza Deliveries")
  size = input("What size pizza do you want? S, M or L: ").lower()
  add_pepperoni = input("Do you want pepperoni? Y or N: ").lower()
  extra_cheeze = input("Do you want extra cheese? Y or N: ").lower()
  price = 0
  if size == 's':
    price += 15
  elif size == 'm':
    price += 20
  elif size == 'l':
    price += 25
  if size == 's' and add_pepperoni == 'y':
    price += 2
  elif add_pepperoni == 'y':
    price += 3
  if extra_cheeze == 'y':
    price += 1
  print(f"Your final bill is ${price}")

def love_calculator():
    first_user = input("What is your name?: ").lower()
    second_user = input("What is your partner's name?: ").lower()
    users_name = first_user+second_user
    true_count = sum((map(users_name.count, ['t','r','u','e'])))
    love_count = sum(map(users_name.count, ['l','o','v','e']))
    total_value = true_count*10 + love_count
    if total_value < 10 or total_value > 90:
        print(f"Your score is {total_value}, you go together like coke an mentos.")
    elif total_value > 40 and total_value <= 50:
        print(f"Your score is {total_value}, you are alright together.")
    else:
        print(f"Your score is {total_value}")


# Day 4 Challenge
import random
from warnings import simplefilter

rand_int = random.randint(1,10)

def heads_or_tails():
    rand_head_or_tails = random.randint(0,1)
    if rand_head_or_tails == 0:
        print("Tails")
    else:
        print("Heads")

# Select a random name from a list of names
def select_random_name():
    names_string = input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(', ')
    length_of_list = len(names)
    random_name_idx = random.randint(0,length_of_list - 1)
    print(f"Lucky winner is {names[random_name_idx]}")

# A program whcih mark a spot with an X
def x_marker():
    row1 = [" "," "," "]
    row2 = [" "," "," "]
    row3 = [" "," "," "]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = print("Where do you want to put the treasure?")
    column_num = int(input("Add Column number"))
    row_num = int(input("Add row number"))
    map[row_num-1][column_num-1] = 'X'
    print(f"{row1}\n{row2}\n{row3}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def rock_paper_scissors():
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors: "))
    computer_input = random.randint(0,2)
    list_operation = ['Rock','Paper','Scissors']
    # Relationship between rock paper ans scissors
    # 0 < 1 < 2 <0
    if user_input >2 or user_input < 0:
        print("You typed an invalid number, you lose!")

    else: 
        if user_input == 2:
            if computer_input == 1:
                print(f"User input: {list_operation[user_input]} Computer Input: {list_operation[computer_input]}")
                print("User Won!")
            elif computer_input == 0:
                print(f"User input: {list_operation[user_input]} Computer Input: {list_operation[computer_input]}")
                print("Computer Won!")
            else:
                print("Draw")
        elif computer_input == 2:
            if user_input == 1:
                print(f"User input: {list_operation[user_input]} Computer Input: {list_operation[computer_input]}")
                print("Computer Won!")
            elif user_input == 0:
                print(f"User input: {list_operation[user_input]} Computer Input: {list_operation[computer_input]}")
                print("User Won!")
            else:
                print("Draw")
        else:
            if user_input == computer_input +1:
                print(f"User input: {list_operation[user_input]} Computer Input: {list_operation[computer_input]}")
                print("User Won!")
            elif user_input == computer_input:
                print(f"User input: {list_operation[user_input]} Computer Input: {list_operation[computer_input]}")
                print("Draw")
            else:
                print(f"User input: {list_operation[user_input]} Computer Input: {list_operation[computer_input]}")
                print("Computer Won!")


def average_height_calc():
    student_list = input("Key in the list of heights of students, separated by comma : ").split()
    total_height = 0
    for students in student_list:
        total_height += int(students)
    avg_height = round(total_height/len(student_list))
    print(avg_height)

def highest_score():
    list_scores = input("List of student's scores ").split()
    high_score = 0

    if len(list_scores) > 0:
        for score in list_scores:
            if int(score) > high_score:
                high_score = int(score)
            else:
                continue
        print(high_score) 
    else:
        return

def even_sum():
    sum = 0
    for num in range(0,101):
        if num % 2 == 0:
            sum += num
    print(f"Total sum of even numbers between 0 to 100 is {sum}")

def fizz_buzz():
    for num in range(0, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num %3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Welcoming message
    print("Welcome to the Password Generator!")
    password_length = int(input("How many letters would you like in your password "))
    symbol_length = int(input("How many symbols would you like? "))
    number_length = int(input("How many numbers would you like? "))

    password_string = []

    for i in range(symbol_length):
        password_string.append(random.choice(symbols))
    for i in range(number_length):
        password_string.append(random.choice(numbers))
    for idx in range(password_length - symbol_length - number_length):
        password_string.append(random.choice(letters))
    
    print(password_string)

    random.shuffle(password_string)

    password_string = ''.join(password_string)
    print(password_string)