from playsound import playsound
import time



def alarm(secounds):
    timepassed=0
    while timepassed < secounds:
        time.sleep(1)
        timeleft= secounds-timepassed
        timepassed+=1
        print(timeleft)

    playsound("you phone lnging.mp3")
        
sec= int(input("Enter the sec left for the time you want the alarm to rang = "))
alarm(sec)