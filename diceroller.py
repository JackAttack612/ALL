import random
import playsound
import time

def select():
    choice = input("\nHow many sides do you want (6, 12, 24, 36): ").lower()
    if choice == '6':
        side6()
    elif choice == 'quit':
        print('Loading Menu...')
        time.sleep(2)
        import all
    elif choice == '12':
        side12()
    elif choice == '24':
        side24()
    elif choice == '36':
        side36()
    elif choice == "69":
        sixnine()
    else:
        print("\nPlease Choose 6, 12, 24, or 36")
        time.sleep(3)
        select()

def side6():
    choice6 = random.choice(['1', '2', '3', '4', '5', '6'])
    print("\nYou rolled a " + choice6)
    select()

def side12():
    choice12 = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    print("\nYou rolled a " + choice12)
    select()

def side24():
    choice24 = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'])
    print("\nYou rolled a " + choice24)
    select()

def side36():
    choice36 = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'])
    print("\nYou rolled a " + choice36)
    select()

def sixnine():
    print("\nHAHAHAHAHA, Ur so funny")
    select()

select()
