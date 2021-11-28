import random
import hangman_art
import hangman_words as h_words

# Basic key global variables
word_list = h_words.word_list
display = []
chosen_word = word_list[random.randint(0, len(word_list) -1)]
num_tries = 0
print(hangman_art.logo)

# Sets the parameters of the display
for i in range(len(chosen_word)):
  display.append("_")

# Functions required for the logical processing
def update_display(word, char):
  """Change the display list if the user guesses the correct character

  Args:
      word (list of String): The word that is automatically selected
      guess (String): Letter the user guesses
  """
  for i in range(len(word)):
    if word[i] == char:
      display[i] = char
  

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

print(chosen_word)

while num_tries <= 6:
  user_guess = input("Guess a letter: ").lower()  
  guess = check_input(chosen_word, user_guess)
  if guess:
    if user_guess in display:
      print("Repeated Guess: You guessed it already!\n"," ".join(display))
      continue
    print("Correct Guess")
    update_display(chosen_word, user_guess)
    print(" ".join(display))
    print("\n")
    if "_" not in display:
      print(f"End of Game! You won!\nThe word was: {chosen_word}")
      break
  else:
    print("Wrong, Try again!")
    print(hangman_art.mr_hangman[num_tries])
    num_tries+=1

print("Game Over")