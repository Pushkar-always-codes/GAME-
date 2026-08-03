import random

def deposit(invest,mode):
    if (invest >= 10):
        a= random.randrange(mode)
        b= random.randrange(mode)
        c= random.randrange(mode)
        if (a==b==c):
            print("Jackpot")
            return invest*5
            

        elif(a==b!=c) or (a!=b==c) or (a==c!=b):
            print("Major")
            return invest*2
            

        else:
            print("You are stupid to invest here")
            return invest*0   

    else:
        ("Insufficient Amount") 




name=input("Enter your name ")

print("Welcome !! To the Faith Fortune " , name)

paisa=int(input("Enter your property value "))

level=str(input("Select your level (easy ,medium , hard)"))

if (level=="easy"):
    mode=3

elif (level=="medium"):
    mode=5

else:
    mode=7

a=deposit(paisa,mode)
print("Your property value" , a) 