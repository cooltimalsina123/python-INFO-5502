import random
def different_output(num):
    randomNum= [];
    for x in range(0,12):
        num = random.randint(1,100)
        randomNum.append(num)
        print(randomNum)
