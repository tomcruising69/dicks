import random
import time

num1 = random.randint(1,12)
num2 = random.randint(1,12)
totaldie = (num1 + num2)

input("roll it ")
time.sleep(2)
print(f"{num1} + {num2} = {totaldie}")