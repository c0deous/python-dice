#  Python "Dice"
#  Jesse Wallace (c0deous) (c) 2014

import os, sys, random
from optparse import OptionParser

# Define/Parse Args
parser = OptionParser()
parser.add_option('-2', '--two-dice', action='store_true', dest='two_dice', help='Rolls two dice instead of one die.')
parser.add_option('-v', '--verbose', action='store_true', dest='verbose', help='Displays more output and fancyness.')

(options, args) = parser.parse_args()

# ANSI Colors #
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def colored(text, color):
    try: 
        colorcode = getattr(bcolors, color)
        return colorcode + text + bcolors.ENDC
    except AttributeError:
        return text

# Input Method Switcher #
def inputm(textct):
    try:
        raw_input(textct)
    except NameError:
        input(textct)

# Dice ASCII Art Cache
dice_1 = colored("""
 _____
|     |
|  X  |
|     |
 -----""", 'FAIL')

dice_2 = colored(""" 
 _____
|   X |
|     |
| X   |
 -----""", 'OKBLUE')

dice_3 = colored(""" 
 _____
|   X |
|  X  |
| X   |
 ----- """, 'OKGREEN')

dice_4 = """ 
 _____
|X   X|
|     |
|X   X|
 -----"""

dice_5 = colored(""" 
 _____
|X   X|
|  X  |
|X   X|
 -----""", 'WARNING')

dice_6 = colored("""
 _____  
|X X X|
|     |
|X X X|
 ----- """, 'HEADER')

# Get ASCII Function
def get_ascii_dice(num):
        if num == 1:
                return dice_1
        elif num == 2:
                return dice_2
        elif num == 3:
                return dice_3
        elif num == 4:
                return dice_4
        elif num == 5:
                return dice_5
        elif num == 6:
                return dice_6

# Roll Functions
def roll_one_die():
    rollednum = random.randint(1, 6)
    print
    print(get_ascii_dice(rollednum))
    print
    print('Rolled a ' + str(rollednum))    

def roll_two_dice():
    rollednum1 = random.randint(1, 6)
    rollednum2 = random.randint(1, 6)
    print
    print(get_ascii_dice(rollednum1))
    print
    print(get_ascii_dice(rollednum2))
    print('Roll 1: ' + str(rollednum1))
    print('Roll 2: ' + str(rollednum2))
    print('Total: ' + str(rollednum1 + rollednum2))

def roll_one_die_verbose():
    rollednum = random.randint(1, 6)
    inputm("/:: PRESS ENTER TO ROLL ::\\")
    print(' ')
    print(colored('|-----------------------|', 'blue'))
    print(' ')
    print(get_ascii_dice(rollednum))
    print(' ')
    print('Rolled a ' + str(rollednum))
    print(colored('|-----------------------|', 'blue'))

def roll_two_dice_verbose():
        inputm("/:: PRESS ENTER TO ROLL ::\\")
        print
        print('Dice 1')
        print(colored('|-----------------------|', 'blue'))
        rollednum1 = random.randint(1, 6)
        print
        print(get_ascii_dice(rollednum1))
        print('Rolled a ' + colored(str(rollednum1), 'magenta') + ' for die 1.')
        print(colored('|-----------------------|', 'blue'))
        print
        inputm("/:: PRESS ENTER TO ROLL ::\\")
        print
        print('Dice 2')
        print(colored('|-----------------------|', 'blue'))
        rollednum2 = random.randint(1, 6)
        print
        print(get_ascii_dice(rollednum2))
        print('Rolled a ' + colored(str(rollednum2), 'magenta') + ' for die 2.')
        print(colored('|-----------------------|', 'blue'))
        print
        print('Total: ' + str(rollednum1 + rollednum2))
        print

def dicetest():
   print
   print(dice_1)
   print
   print(dice_2)
   print
   print(dice_3)
   print
   print(dice_4)
   print
   print(dice_5)
   print
   print(dice_6)
   print

# Option Directing to Function
if options.verbose == True:
        if options.two_dice == True:
                roll_two_dice_verbose()
        else:
                roll_one_die_verbose()

else:
        if options.two_dice == True:
                roll_two_dice()
        else:
                roll_one_die()








