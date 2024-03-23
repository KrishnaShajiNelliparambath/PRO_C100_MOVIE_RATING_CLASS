import random
min=1
max=6
def roledice(min,max):
    while True:
        print("Rolling dice....")
        number=random.raidint(min,max)
        print(f"Your number : "+number)
        choice=input("Do you want to role the dice again?(Yes/No)")
        if choice=="Yes":
            roledice()
        elif choice=="No":
            break
        else:
            print("Something went wrong..")
roledice()