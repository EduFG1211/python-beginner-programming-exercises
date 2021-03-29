import random

# your code here
def generate_random():
    num = random.randint(0, 9)
    num2 = random.randrange(0,9)
    print(num)
    print(num2)
    return num
generate_random()