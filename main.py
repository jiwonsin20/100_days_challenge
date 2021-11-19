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
        print(f"Your score is  {total_value}")


