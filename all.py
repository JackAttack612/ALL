import time
import os
from playsound import playsound


def games(): 
    print("Games to play:")
    print("rps")
    print("diceroller")
    print("calculator")
    all = input('\nWhat game do you want to play: ')
    if all == 'rps':
        print('playing Rock Paper Scissors')
        time.sleep(2)
        import rps
        execfile('rps.py')
        games()
    elif all == 'diceroller':
        print('playing Dice Roller')
        time.sleep(2)
        import diceroller
        execfile('diceroller.py')
        games()
    elif all == 'calculator':
        print('playing calculator')
        time.sleep(2)
        import calculator
        execfile('calculator.py')
        games()
    else:
        games()

games()