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

def proj_rps():
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
            projects()
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

def proj_diceroller():
    def select():
        try:
            choice = input("\nHow many sides do you want: ").lower()
            if choice == 'quit':
                projects()
            else:
                roll = random.randint(1, int(choice))
                print("You rolled: " + str(roll))
                select()
        except ValueError:
            print("\n⚠")
            print("ValueError: You have to input a number")
            print("⚠")
            time.sleep(2)
            select()


    select()

def proj_twitterbot():
    auth = tweepy.OAuthHandler("QjT3WQnlSIsO4dexw9C0TaIP4", "CeqHI2EcKnAJkbWU3IcCiEArqG8xWZphzXKJIc1WoT5piuUnJj")
    auth.set_access_token("1156848387163119616-h87w8HtypPHyvTRYUZGyz6jT3EP4EZ", "QnhxN5pDZ01YFaTR94lVpPI1vSKDsje2CDLCMvJQ9INKU")

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("\nAuthentication OK")

    except:
        print("Error during authentication")

    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

    # Things to do
    def read():
        timeline = api.home_timeline()
        for tweet in timeline:
            print(f"{tweet.user.name} said {tweet.text}")
            time.sleep(3)
            main()

    def gread():
        timeline = api.home_timeline()
        for tweet in timeline:
            print(f"{tweet.user.name} said {tweet.text}")
            time.sleep(3)
            guest()

    def Tweet():
        tweet_input = input("\nWhat do you want to tweet: ")
        api.update_status(tweet_input)
        print("You tweeted: " + tweet_input)
        main()

    def user_info():
        try:
            user_info_name = input("\nWhat user do you want to find: ")
            user = api.get_user(user_info_name)
            followers_count = user.followers_count
    
            print("User details:")
            print('Username: ' + user.name)
            print('User Description: ' + user.description)
            print('User Location: ' + user.location)
            print("Followers: " + str(followers_count))

            print("\nLast 20 Followers:")
            for follower in user.followers():
                print(follower.name)
            main()
        except:
            print("\nCould not find user")
            main()

    def guser_info():
        try:
            user_info_name = input("\nWhat user do you want to find: ")
            user = api.get_user(user_info_name)
            followers_count = user.followers_count
    
            print("User details:")
            print('Username: ' + user.name)
            print('User Description: ' + user.description)
            print('User Location: ' + user.location)
            print("Followers: " + str(followers_count))

            print("\nLast 20 Followers:")
            for follower in user.followers():
                print(follower.name)
            guest()
        except:
            print("\nCould not find user")
            guest()

    def like_mentioned():
        tweets = api.mentions_timeline()
        for tweet in tweets:
            tweet.favorite()
        main()

    def mentioned():
        tweets = api.mentions_timeline()
        for tweet in tweets:
            print(f"\n{tweet.user.name} said {tweet.text}")
        time.sleep(3)
        main()
            
    # Function Menu
    def main():
        start = input("\nWhat do you want to do: ").lower()
        if start == 'help':
            print("quit\ntweet\nread\nuserinfo\nlikementioned\nmentioned")
            main()
        elif start == 'tweet':
            confirmation = input("\nAre you sure you want to send a tweet (Yes or No): ").lower()
            if confirmation == 'yes':
                Tweet()
            elif confirmation == 'no':
                main()
            else:
                print("\nDid not receive a valid input")
                main()
        elif start == 'read':
            read()
        elif start == 'userinfo':
            user_info()
        elif start == 'likementioned':
            like_mentioned()
        elif start == 'mentioned':
            mentioned()
        elif start == 'quit':
            projects()
        else:
            print("\nDid not receive a valid input")
            main()

    # Guest Functions
    def guest():
        start = input("\nWhat do you want to do: ").lower()
        if start == 'help':
            print('quit\nread\nuserinfo')
            guest()
        elif start == 'read':
            gread()
        elif start == 'userinfo':
            guser_info()
        elif start == 'quit':
            projects()
        else:
            guest()

    # Login
    def Login():
        Username = input("\nUsername: ")
        Password = pwinput.pwinput()
        if Username == 'JackAttack612' and Password == 'Madjack612!':
            print("\nLogin Sucessful")
            time.sleep(2)
            main()
        elif Username == 'Guest' and Password == 'Guest123':
            print("Login Sucessful")
            print("Guest Mode: Limited Abilities")
            time.sleep(3)
            print("type help to get a list of things you can do")
            guest()
        elif Username or Password == 'quit':
            projects()
        else:
            print("Username or Password is incorrect")
            Login()
    print("\nGuest Login:\nUsername: Guest\nPassword: Guest123")
    Login()

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
    elif all2 == 'diceroller':
        print('starting Dice Roller...')
        time.sleep(2)
        proj_diceroller()
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