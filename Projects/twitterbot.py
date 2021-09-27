import tweepy
import time
import pwinput

auth = tweepy.OAuthHandler("QjT3WQnlSIsO4dexw9C0TaIP4", "CeqHI2EcKnAJkbWU3IcCiEArqG8xWZphzXKJIc1WoT5piuUnJj")
auth.set_access_token("1156848387163119616-h87w8HtypPHyvTRYUZGyz6jT3EP4EZ", "QnhxN5pDZ01YFaTR94lVpPI1vSKDsje2CDLCMvJQ9INKU")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")

except:
    print("Error during authentication")

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

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
        import all
    else:
        print("\nDid not receive a valid input")
        main()

def guest():
    print("type help to get a list of things you can do")
    start = input("\nWhat do you want to do: ").lower()
    if start == 'help':
        print('quit\nread\nuserinfo')
    elif start == 'read':
        gread()
    elif start == 'userinfo':
        guser_info()
    elif start == 'quit':
        import all
    else:
        guest()

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
        guest()
    elif Username or Password == 'quit':
        import all
    else:
        print("Username or Password is incorrect")
        Login()
print("Guest Login:\nUsername: Guest\nPassword: Guest123")
Login()