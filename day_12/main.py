# Number Guessing Game
import random as rand

correct_guess = False



def run_game(diff, num):
  global correct_guess

  if diff == 'hard':
    chances = 5
    while not correct_guess:
      if chances != 0:
        print(f"You have {chances} attempts remaining to guess the number")
        guess = int(input("   Make a guess: "))
        if guess > num:
          print("Too high.")
          print("Guess Again.")
          chances -=1
        elif guess < num:
          print("Too low.")
          print("Guess Again.")
          chances -=1
        else:
          print(f"You got it! the answer was {num}")
          correct_guess = True
    
  elif diff == 'easy':
    chances = 10
    return

print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")
random_number = rand.randint(1,100)

print(f"Randomly Generated Number: {random_number}")
difficulty_input = input("Choose a difficulty. Type 'easy' or 'hard': ")

run_game(difficulty_input, random_number)
