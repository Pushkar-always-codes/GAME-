print("Welcome !! Here you can check whether your gmail is correct or not .")
import string
a=str(string.ascii_lowercase + string.digits) +"@"+"."
email=input("Enter the Email = ")
for i in email:
    if i in a:
        if email[0].isalpha():
            if email[-10] is "@" :
                if email.count("@") == 1:
                    continue

    else:
        print("Wrong")
        quit

print("Correct") 