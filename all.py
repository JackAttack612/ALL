from io import open_code
import time
import os
from playsound import playsound
import ctypes
from os import system


# Main
def projects(): 
    print("\nProjects:")
    print("rps")
    print("diceroller")
    print("calculator")
    print("twitterbot")
    all2 = input('\nWhat project do you want to start: ').lower()
    if all2 == 'rps':
        print('starting Rock Paper Scissors...')
        time.sleep(2)
        print("")
        from Projects import rps
        open(rps.py)
        projects()
    elif all2 == 'diceroller':
        print('starting Dice Roller...')
        time.sleep(2)
        from Projects import diceroller
        open(diceroller.py)
        projects()
    elif all2 == 'calculator':
        print('starting calculator...')
        time.sleep(2)
        from Projects import calculator
        open(calculator.py)
        projects()
    elif all2 == 'twitterbot':
        print('starting twitterbot...')
        time.sleep(2)
        from Projects import twitterbot
        open(twitterbot.py)
        projects()
    else:
        projects()

# Naming Terminal
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True);
kernel32.SetConsoleTitleW(u"Python Project Menu Terminal")

# Loading
print("\nLoading Project Menu...")
print("\nInformation:")
print("In any project type quit to go back to the project selection menu")
time.sleep(3)
print('________________________________________________________________')

# Directory 
directory = os.path.dirname(__file__)
dicepath = (directory + r'/Projects/diceroller.py')

# Start
projects()