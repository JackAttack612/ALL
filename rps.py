import random
import time
import os
from playsound import playsound
from random import randint
from time import sleep

def play():
        
    user = input("\nWhat is your choice? 'r' for rock, 'p' for paper, and 's' for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print('\nIt\'s a tie\nYour Choice: ' + user + ". Their Choice: " + computer)
        play()
    
    elif user == 'quit':
        import all.py
        execfile(all.py)

    if is_win(user, computer):
        print('\nYou win!\nYour Choice: ' + user + ". Their Choice: " + computer)
        playsound(filelocation + r'\Sound\win.wav')
        input("\nPress enter to play again")
        play()

    if is_win(computer, user):
        print('\nYou lost!!\nYour Choice: ' + user + ". Their Choice: " + computer)
        playsound(filelocation + r'\Sound\lose.wav')
        input("\nPress enter to play again")
        play()
    
    else:
        print("\nError!!!\nYou have to type 'r', 'p', or 's'")
        time.sleep(2)
        input("\nPress enter to continue")
        play()


def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') \
    or (user == 'p' and computer == 'r'):
        return True

filelocation = os.path.dirname(__file__)
input("Press enter to play")
play()