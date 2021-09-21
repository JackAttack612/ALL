import time
import os
from playsound import playsound


def games(): 
    print("\nProjects:")
    print("rps")
    print("diceroller")
    print("calculator")
    all = input('\nWhat project do you want to start: ').lower()
    if all == 'rps':
        print('starting Rock Paper Scissors...')
        time.sleep(2)
        import rps
        games()
    elif all == 'diceroller':
        print('starting Dice Roller...')
        time.sleep(2)
        import diceroller
        games()
    elif all == 'calculator':
        print('starting calculator...')
        time.sleep(2)
        import calculator
        games()
    else:
        games()

print("\nLoading Project Menu...")
print("\nInformation:")
print("In any project type quit to go back to the project selection menu")
time.sleep(3)
print('________________________________________________________________')

games()