import random
import time
import os
from playsound import playsound
from random import randint
from time import sleep

def play():
        
    user = input("What is your choice? 'r' for rock, 'p' for paper, and 's' for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])

    def action():
        if is_win(user, computer):
            print('\nYou win!\nYour Choice: ' + user + ". Their Choice: " + computer)
            playsound(filelocation + r'\Audio\win.wav')
            print("") #error occurs if not here (Dont know why)
            play()

        if is_win(computer, user):
            print('\nYou lost!!\nYour Choice: ' + user + ". Their Choice: " + computer)
            playsound(filelocation + r'\Audio\lose.wav')
            print("") #error occurs if not here (Dont know why)
            play()
        else:
            print("\nError!!!\nYou have to type 'r', 'p', or 's'")
            time.sleep(2)
            input("\nPress enter to continue")
            play()

    if user == computer:
        print('\nIt\'s a tie\nYour Choice: ' + user + ". Their Choice: " + computer + "\n")
        play()   
    if user == 'r':
        action()
    elif user == 'p':
        action()
    elif user == 's':
        action()
    elif user == 'quit':
        print('Loading Menu...')
        time.sleep(2)
        import all
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
play()
