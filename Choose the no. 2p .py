mode=int(input("Enter no. of player(1 or 2) "))
# import random
# if (mode==1):
#     target=random.randint(1,11)

#     while True:
#         choice = int(input("Choose a number between 1 to 10 = "))

#         if (choice==target):
#             print("You won \nGame Over !!")
#             break
        
#         elif(choice<target):
#             print("less than target")
        
#         else:
#             print("more than target")

# elif (mode==2):
#     player1 = input("Enter your name of player 1 ")
#     player2 = input("Enter your name of player 2 ")
#     target1 = random.randint(1,11)
#     target2 = random.randint(1,11)
    
#     while True :
        
#         choice1=int(input("Choose a number between 1 to 10 for player 1 = "))
#         choice2=int(input("Choose a number between 1 to 10 for player 2 = "))

#         if (choice1 == target1) and (choice2 == target2):
#             print("TIE !!")

#         elif  (choice1 == target1) or (choice2 == target2): 
#             if (choice1 == target1) :
#                 print("Player1 won \nGame Over !!")
#                 break

#             else:
#                 print("Player2 won \nGame Over !!")
#                 break      
        
#         elif (choice1<target1) and (choice2<target2):
#             print("Both are less than target ")

#         elif (choice1>target1) and (choice2>target2):
#             print("Both are more than target ")

#         elif (choice1<target1) and (choice2>target2) :
#             print("player 1 has guessed less than target abd player 2 has guessed more than target")

#         elif (choice1>target1) and (choice2<target2) :
#             print("player 1 has guessed more than target abd player 2 has guessed less than target")   

#         else:
#             continue 