name=input("Enter your name ")
print("Welcome !! To the game " , name)

score = 0  

print("This game is all about believing your instinct . If you want to win the game , score atleast 50 .")

answer = input("Are you ready? Yes(Y) or No(N) ")
y = ("yes" , "Yes" , "Y")
n =("No" , "no" , "N")
if (answer in y) :
    print("In this game you have to choose left or right or straight gate to open. \n2 out of 3 gate will be save and the remaining one will be danger . \nBelieve your instinct and choose the gate.")
    a= input("Which gate you want to choose ?")
    if (a == "left" or "right"):
        print("You are save ")
        score += 10
        b = input("Which gate you want to choose ?")
        if (b == "left" or "straight"):
            print("You are save ")
            score += 10
            c = input("Which gate you want to choose ?")
            if (c == "left" or "right"):
                print("You are save ")
                score += 10
                d = input("Which gate you want to choose ?")
                if (d == "straight" or "right"):
                    print("You are save ")
                    score += 10
                    e = input("Which gate you want to choose ?")
                    if (e == "left" or "straight"):
                        print("You are save ")
                        score += 10
                        print("Congrats !! You won the game.\nYour Score = " , score)

elif (answer in n):
    print("You quitted !!")

else:
    print("You died")