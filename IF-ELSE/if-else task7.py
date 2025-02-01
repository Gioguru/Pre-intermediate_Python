Login = input("Enter your username :")
Password = input("Enter your password :")
Login1 = "user"
Password1 = "admin"
if  Login == Login1 and Password == Password1 :
    print("well done")
elif Login == Login1 or Password == Password1 :
    print("try again")
else:
    print("You are hacker")