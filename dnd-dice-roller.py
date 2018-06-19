import random
from colorama import init, Fore, Back, Style

init(convert=True, autoreset=True)

def roll(sides):
    return random.randint(1, int(sides))

print(Fore.GREEN + '\nYour D20 roll is: ' + str(roll(20)) +'\n')

newDieRoll = input('Did you want to roll a different sided die?\nType (y) for yes\nPress (n) for no\n>>> ').lower()

if newDieRoll == 'yes' or newDieRoll == 'y':
    sides = input('How many sides does your die have? ')
    print(Fore.GREEN + '\nYour D' + str(sides) + ' roll is ' + str(roll(sides)) + '\n')
elif newDieRoll.lower() == 'no' or newDieRoll == 'n':
    exit()