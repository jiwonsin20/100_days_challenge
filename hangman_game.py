import random

word_list = ["aardvark", "baboon","camel"]
display = []
chosen_word = word_list[random.randint(0, len(word_list) -1)]
for i in range(len(chosen_word)):
  display.append("_")
print(display)

user_guess = input("Guess a letter: ").lower()

def show_word(word, user_letter):
  

def check_input(word, user_letter):
  for letter in word:
    if letter == user_letter:
      return True
  
  return False

print(chosen_word)

guess = check_input(chosen_word, user_guess)
if guess:
  print("Correct Guess")
else:
  print("Wrong")