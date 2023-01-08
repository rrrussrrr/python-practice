import random

print("Pick a range for the randodm number:")
range = int(input())
ranNum = random.randint(1, range);
print('OK!  Now guess a number between 1 and ' + str(range))
while True:
    guess = int(input())
    if guess == ranNum:
        print ("nice!")
        break
    elif guess < ranNum:
        print("too low!")
    else:
        print("too high!")
