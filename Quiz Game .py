print("Welcome to the game !!")
name = input("enter your name or exit ")

if (name == exit):
    print("Thanks for coming")


print("Let's start")    

score = 0
a=input("1. What is the capital of jharkhand? ")

if (a == "Ranchi" or "ranchi" ):
    print("Correct")
    score+=1

else:
    print("Incorrect")

b=int(input("2. What's the square of 25? "))

if (b==625):
    print("Correct")
    score+=1
else:
    print("Incorrect") 

c=int(input("2. What's the square root of 225? "))

if (c==15):
    print("Correct")
    score+=1
else:
    print("Incorrect") 

print("Congrats!! Your score is" , score , "out of 3") 

print("Thanks for coming !!")  