import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

name_bid_dict = {}
highest_bid = ""
other_bidders = 'yes'
print(logo)

def clearConsole():
  command = "clear"
  if os.name in ('nt', 'dos'):
    command = 'cls'
  os.system(command)

def add_to_dictionary(name, bid):
  name_bid_dict[name] = bid

def check_highest_bid(dictionary, best_bid):
  for key in dictionary:
    if dictionary[key] > dictionary[best_bid]:
      best_bid = key
  return best_bid

while other_bidders == 'yes':
  name_input = input('What is your name?: ')
  bid_input = input('What\'s your bid?: $')
  add_to_dictionary(name_input, bid_input)
  highest_bid = check_highest_bid(name_bid_dict, name_input)
  other_bidders = input('Are there any other bidders? Type \'yes\' or \'no\'. ')
  clearConsole()

print(f"The winner is {highest_bid} with a bid of ${name_bid_dict[highest_bid]}")




