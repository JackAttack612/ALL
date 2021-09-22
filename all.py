from io import open_code
import time
import os
from playsound import playsound
import ctypes
from os import system

def projects(): 
    print("\nProjects:")
    print("rps")
    print("diceroller")
    print("calculator")
    all2 = input('\nWhat project do you want to start: ').lower()
    if all2 == 'rps':
        print('starting Rock Paper Scissors...')
        time.sleep(2)
        from Projects import rps
        projects()
    elif all2 == 'diceroller':
        print('starting Dice Roller...')
        time.sleep(2)
        from Projects import diceroller
        projects()
    elif all2 == 'calculator':
        print('starting calculator...')
        time.sleep(2)
        from Projects import calculator
        projects()
    else:
        projects()

print("\nLoading Project Menu...")
print("\nInformation:")
print("In any project type quit to go back to the project selection menu")
time.sleep(3)
print('________________________________________________________________')

directory = os.path.dirname(__file__)
dicepath = (directory + r'/Projects/diceroller.py')
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True);
kernel32.SetConsoleTitleW(u"Python Project Menu Terminal")
projects()