import blackjack_art as art
import random as rand
from os import system, name

card_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]

statement = ""

def clear():
  if name=='nt':
    _ = system('cls')
  else:
    _ = system('clear')

def player_cards(cards):
  player_starting_cards = rand.choices(cards, weights=None, k=2)
  player_starting_cards.sort()
  return player_starting_cards
  
def computer_cards(cards):
  comp_cards = rand.choices(cards, weights=None, k=1)
  comp_cards.sort()  
  return comp_cards

def add_list_elements(lst):
  sum = 0
  for i in lst:
    sum+=i
  return sum

def play_game(p, c, s):
  print("   Your cards: ", p, "current score: ", add_list_elements(p))
  print("   Computer's first card: ", c, " current score: ", add_list_elements(c))
  
  # Loop this section until the winning conditions are met
  while(True):

    choice = input("Type 'y' to get another card, type 'n' to pass: ")

    # Check whether player got a BlackJack
    if add_list_elements(p) == 21:
      print("You win by BlackJack!!!")
      break

    # Player chose to get cards
    if choice == 'y':
      p_random_card = card_list[rand.randint(-1, len(card_list) -1)]
      p.append(p_random_card)
      print("   Your cards: ", p, "current score:", add_list_elements(p))

      # After choosing a card and it goes beyond 21, player lose
      if add_list_elements(p) > 21:
        if 11 in p:
          p = [1 if i == 11 else i for i in p]
          continue
        else:
          print("You went over. You lose 😤")
          break
      
    
    # If player chose not to get cards then computer will choose their cards
    else:
      while (True):
        if add_list_elements(c) > 21:
          if 11 in c:
            p = [1 if i == 11 else i for i in p]
            continue
          else:
            break
        elif add_list_elements(c) == 21:
          break
        else:
          c_random_card = card_list[rand.randint(-1, len(card_list) -1)]
          c.append(c_random_card)

          # Print out the cards we have
          print("   Your final cards: ", p, "final score:", add_list_elements(p))
          print("   Computer's hand: ", c, "Current Score: ",add_list_elements(c))
        
      if add_list_elements(p) < add_list_elements(c) and add_list_elements(c) <= 21:
        print("You Lose")
        break

      elif add_list_elements(p) == add_list_elements(c):
        print("Draw")
        break

      else:
        if add_list_elements(c) > 21:
          statement = "Opponenet went over. "
        
        print(statement, "You Won! 😁")
        break
    

def play_again():
  play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if play_again == 'n':
    return play_again


# Game starts from here
start_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
clear()
print(art.logo)

while start_input == 'y':
  p_cards = player_cards(card_list)
  c_cards = computer_cards(card_list)
  play_game(p_cards, c_cards, start_input)
  choice = play_again()
  start_input = choice
