import time
import random

print("Welcome to the game !!")
name = input("Enter your name = ")
print("Let's start \n-----------------")    
time_start=time.time()
score =0

while score <10:
    operators=("+" , "-" , "*")
    start = random.randrange(10)
    end = random.randrange(10)
    choosedoperator= random.choice(operators)
    Guess = input("#Problem " + str(start) + " " + choosedoperator + " " + str(end) + " = ")
    Answer = str(eval(Guess))

    if Guess == Answer:
        print ("Correct ")
        score +=1

    else:
        print("Incorrect")
        continue    

time_end=time.time()
Totaltime=time_end-time_start
print("----------------------\n" , "total time taken = " , Totaltime) 

print("Thanks for coming !!") 