from io import open_code
import time
import os
from playsound import playsound
import ctypes
from os import system
import pwinput
import random
import tweepy
from random import randint
import random


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
        proj_rps()
        projects()
    elif all2 == 'diceroller':
        print('starting Dice Roller...')
        time.sleep(2)
        proj_diceroller()
        projects()
    elif all2 == 'calculator':
        print('starting calculator...')
        time.sleep(2)
        proj_calculator()
    elif all2 == 'twitterbot':
        print('starting twitterbot...')
        time.sleep(2)
        proj_twitterbot()
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

# Start
projects()

def proj_calculator():
    # Eastereggs -------

    def audrey():
        print('\nAvailable songs:\nloverboy\nbored')
        time.sleep(3)
        music = input("What song do you want to play (Title Only): ").lower()
        if music == 'quit':
            calculator()
        elif music == 'loverboy' or 'bored':
            print("\nPlaying " + music)
            playsound(location + r'\Audio\\' + music + r'.mp3')
            calculator()

    def admin_panel():
        name = input("Enter Input:").lower()
        if name == 'nuke':
            print("Okay, nuking")
            playsound(location + r'\Audio\nuke.mp3')
            quit()
        elif name == 'audrey':
            audrey()
        else:
            print("That input does not exist")
            print("Your input: " + name)
            calculator()

    # Exit -------

    def quit1():
        projects()

    # Main -------

    def calculator():
        try:
            calc = input("\nType calculation or type quit: ").lower()

            if calc == 'quit':
                print('Loading Menu...')
                time.sleep(2)
                quit1()
            elif calc == 'operations':
                print("\nOperations/Operators:")
                print("+ = addition")
                print("- = subtracion")
                print("/ = division")
                print("* = multiply")
                print("** = exponent")
                print("// = floor division")
                print("% = modulus")
                print("< = less than")
                print("> = greater than")
                print("_______________________")
                calculator()
            elif calc == 'admin':
                admin1 = pwinput.pwinput()
                if admin1 == 'Madjack612!':
                    admin_panel()
                else:
                    print("Password Incorrect")
                    calculator()
            elif calc == "audrey":
                    audrey()
            else:
                print("Answer: " + str(eval(calc)))
                calculator()

        except ZeroDivisionError:
            print("\n!!!")
            print("Error: Divided by zero")
            print("Error type: ZeroDivisionError")
            print("!!!")
            time.sleep(3)
            calculator()
        except ValueError:
            print("\n!!!")
            print("Error: Invalid input")
            print("Error type: ValueError")
            print("!!!")
            time.sleep(3)
            calculator()
        except NameError:
            print("\n!!!")
            print("Error: Your calculation has to be numbers")
            print("Error type: NameError")
            print("!!!")
            time.sleep(3)
            calculator()
        except TypeError:
            print("\n!!!")
            print("Error: You tried to use parentheses")
            print("Error type: TypeError")
            print("!!!")
            time.sleep(3)
            calculator()
        except SyntaxError:
            print("\n!!!")
            print("Error: Could not complete calculation.\nMost likely due to an invalid operation; Refer to the top of the page to see all valid operations\nor type \"Operations\"")
            print("Error type: SyntaxError")
            print("!!!")
            time.sleep(3)
            calculator()

    # Program start -------

    print("\nVersion 4.4")
    print("To see latest version visit https://github.com/JackAttack612/Calculator")
    print("Loading Calculator...")
    time.sleep(2)
    print("\nOperations/Info:")
    print("+ = addition")
    print("- = subtracion")
    print("/ = division")
    print("* = multiply")
    print("** = exponent")
    print("// = floor division")
    print("% = modulus")
    print("< = less than")
    print("> = greater than")
    print("This calculator uses order of operation")
    print("To get the list of Operators later type \"Operations\" ")
    print("_______________________")

    location = os.path.dirname(__file__)

    calculator()