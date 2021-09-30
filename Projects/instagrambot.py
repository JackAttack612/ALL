import requests
import time
import re

user = None

def main():
    choice = input("\nWhat do you want to do (type 'help' for a list): ").lower()
    if choice == 'help':
        print("\nFollowerCount")
        main()
    elif choice == 'followercount':
        follower_count()

def follower_count():
    try:
        user = input("Account Name: ")
        url = 'https://www.instagram.com/' + user
        r = requests.get(url).text
        followers = re.search('"edge_followed_by":{"count":([0-9]+)}',r).group(1)

        print(followers)

        main()
    except AttributeError:
        print("AttributeError")
        wrong = input("Do you want to redo? (Yes or No): ").lower()
        if wrong == 'yes':
            follower_count()
        elif wrong == 'no':
            main()
        else:
            print("I did not receive a valid answer. Sending you back.")
            time.sleep(2)
            main()



def start():
    input("Press enter to begin program")
    main()

start()

