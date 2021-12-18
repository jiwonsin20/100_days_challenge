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
highest_bid = 0
other_bidders = 'yes'

def clearConsole():
  command = "clear"
  if os.name in ('nt', 'dos'):
    command = 'cls'
  os.system(command)

def add_to_dictionary(name, bid):
  name_bid_dict['Name'] = name
  name_bid_dict['Bid Amount'] = bid

def check_highest_bid(dictionary):
  for key in dictionary:
    if key['Bid Amount'] > highest_bid:
      highest_bid = key['Bid Amount']
  return highest_bid

while other_bidders == 'yes':
  name_input = input('What is your name?: ')
  bid_input = int(input('What\'s your bid?: '))
  add_to_dictionary(name_input, bid_input)
  highest_bid = check_highest_bid(name_bid_dict)
  other_bidders = input('Are there any other bidders? Type \'yes\' or \'no\'. ')






