# import random
# a=( "rock", "paper" , "sci" )
# p=0
# c=0
# while (p<3) and (c<3) :
#     r=random.choice(a)
#     s=input("Choose from rock , paper or sci ")

#     if (r == "rock" and s == "paper" ) or (r == "paper" and s == "sci") or (r == "sci" and s == "rock"):
#         print("You won") 
#         p+=1
#         print("Your score = " , p , "Bot Score = " , c)
#     elif (r == s):
#         print("Same")
#         continue

#     elif (s not in a):
#         print("Invalid")
#         continue

#     else :
#         print("You lose")
#         c+=1 
#         print("Your score = " , p , "Bot Score = " , c)
    
# if(p ==3)or (c == 3):
#     if (p==3):
#         print("You won the game" , "Your score = " , p , " Bot Score = " , c)

#     else:
        # print ("You lose the game" , "Your score = " , p , " Bot Score = " , c)  