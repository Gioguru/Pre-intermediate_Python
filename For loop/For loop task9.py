import random
from turtledemo.penrose import start

num1 = random.randrange(0,100)
num2 = random.randrange(0,100)
if num1 > num2:
    num1,num2 = num2,num1
total_sum = 0
print(num1)
print(num2)
for i in range(num1,num2):
    total_sum = total_sum + i
print("Answer",total_sum)
