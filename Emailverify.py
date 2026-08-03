print("Welcome !! Here you can check whether your gmail is correct or not .")
import string
a=str(string.ascii_lowercase + string.digits) +"@"
Email=input("Enter the Email = ")
for i in Email:
    if i == a:
        continue
    else:
        print("Wrong")
        break