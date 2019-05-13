import random
secret = random.randint(1,11)

guess = input("type a number in the interval from 1-10: ")
number = str(secret)
if guess == number:
    print("your guess is correct")
elif guess > number:
    guess = input("the secret number is less than " + guess + ", try again: ")
    if guess == number:
        print("your guess is correct")
    elif guess > number:
        guess = input("the secret number is less than " + guess + ", try again: ")
        if guess == number:
            print("your guess is correct")
        else:
            print ("you guessed wrong, start over")
    elif guess < number:
        guess = input("the secret number is more than " + guess + ", try again: ")
        if guess == number:
            print("your guess is correct")
        else:
            print("you guessed wrong, start over")
elif guess < number:
    guess = input("the secret number is more than " + guess + ", try again: ")
    if guess == number:
        print("your guess is correct")
    elif guess > number:
        guess = input("the secret number is less than " + guess + ", try again: ")
        if guess == number:
            print("your guess is correct")
        else:
            print ("you guessed wrong, start over")
    elif guess < number:
        guess = input("the secret number is more than " + guess + ", try again: ")
        if guess == number:
            print("your guess is correct")
        else:
            print("you guessed wrong, start over")