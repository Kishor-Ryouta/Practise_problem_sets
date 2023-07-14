# TODO
# cash in python

#importing from CS50 library
from cs50 import get_float

#defining functions
def calculate_dollars():
     while True:
          dollars = get_float('Enter the change: ')
          if dollars > 0:
               break
          else:
               print('Please enter a valid change')
     cents = 100*dollars
     return cents

def calculate_quarters(cents):
     quarters = 0
     while cents >= 25:
          cents = cents - 25
          quarters+= 1
     return quarters

def calculate_dimes(cents):
     dimes = 0
     while cents >= 10:
          cents = cents - 10
          dimes+= 1
     return dimes

def calculate_nickel(cents):
     nickel = 0
     while cents >=5:
          cents = cents - 5
          nickel+= 1
     return nickel

def calculate_pennies(cents):
     pennies = 0
     while cents>=1:
          cents = cents - 1
          pennies+= 1
     return pennies

#main program
cents = calculate_dollars()

quarters = calculate_quarters(cents)
cents = cents - quarters*25

dimes = calculate_dimes(cents)
cents = cents - dimes*10

nickel = calculate_nickel(cents)
cents = cents - nickel*5

pennies = calculate_pennies(cents)
cents = cents - pennies*1

total_coins = quarters + dimes + nickel + pennies

print(total_coins)








