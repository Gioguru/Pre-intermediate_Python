import  random
number1 = int(input("Enter your number :"))
number2 = random.randrange(20,100)
print("Your number is :",number1)
print("Rand number is :",number2)
if number1%2 != 1 and number2%2 != 1 :
    print("Numbers are Even")
elif number1%2 == 1 and number2%2 == 1:
    print("Numbers are ODD")
else:
    print("One of them is EVEN")

