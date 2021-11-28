import random

mr_hangman_dead = '''
-----------
|         |
|         O
|       / | \
|        / \
|        
|
-----------
'''

mr_hangman_default = '''
-----------
|         |
|
|       
|        
|        
|
-----------
'''
# Functions required for the logical processing
def change_display(word, guess):
  """Change the display list if the user guesses the correct character

  Args:
      word (list of String): The word that is automatically selected
      guess (String): Letter the user guesses
  """
  for i in range(len(word)):
    if word[i] == guess:
      word[i] = guess
  

def check_input(word, user_letter):
  """Checks whether the user guess matches the word

  Args:
      word (list of String): The word that is automatically selected
      user_letter (String): Letter the user guesses

  Returns:
      Boolean: True if the user guess is correct, False if wrong
  """
  for letter in word:
    if letter == user_letter:
      return True
  
  return False

# Basic key global variables
word_list = ["aardvark", "baboon","camel"]
display = []
chosen_word = word_list[random.randint(0, len(word_list) -1)]
num_tries = 0

# Sets the parameters of the display
for i in range(len(chosen_word)):
  display.append("_")
print(display)

user_guess = input("Guess a letter: ").lower()  

print(chosen_word)

while num_tries <= len(chosen_word):
  guess = check_input(chosen_word, user_guess)
  if guess:
    print("Correct Guess")
    next_guess = input("What is your next guess")
    check_input(chosen_word, next_guess)
  else:
    print("Wrong, Try again!")
    num_tries+=1

# if current guess is wrong, repeat until the number of tries are expired