# This file defines the computer moves
import main as m


def probability_check(cards, lst):
  upper_limit = 21
  lose_chance = 0
  win_chance = 0
  
  if 11 in cards:
    max_diff = upper_limit - m.add_list_elements(cards)
    min_diff = upper_limit - m.add_list_elements(cards) - 10
  max_diff = upper_limit - m.add_list_elements(cards)
  print(difference)
  for i in lst:
    if i > difference:
      lose_chance += 1
    else:
      win_chance += 1

