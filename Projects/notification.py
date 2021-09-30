import datetime
import time
import instaloader

FollowerData = None

def main():
    print("Main")
    input("Enter to continue")

def check():
    try:
        covidData = requests.get("https://www.instagram.com/jackattack612/")
        main()
    except:
        print("Error: Please Check your internet connection.")

check()