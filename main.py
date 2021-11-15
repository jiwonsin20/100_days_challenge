# Day 1 of the 100 day challenge
# print('Day 1 - Python Print Function')
# print('The function is declared like this:')
# print('print(\'what to print\')')

# Project 1
def bandNameGenerator():
    print("Hello this is name generator")
    city_input = input("Which city did you grow up in?: ")
    pet_name = input("What's the name of your pet?: ")
    print("Your band name could be " + city_input + " " + pet_name)

# Project 2 
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

tip_calculator()