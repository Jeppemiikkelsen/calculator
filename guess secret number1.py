guess = input("type a number in the interval from 1-10: ")
if guess == "3":
    print("your guess is correct")
elif guess > "3":
    guess = input("the secret number is less than " + guess + ", try again: ")
    if guess == "3":
        print("your guess is correct")
    elif guess > "3":
        guess = input("the secret number is less than " + guess + ", try again: ")
        if guess == "3":
            print("your guess is correct")
        else:
            print ("you guessed wrong, start over")
    elif guess < "3":
        guess = input("the secret number is more than " + guess + ", try again: ")
        if guess == "3":
            print("your guess is correct")
        else:
            print("you guessed wrong, start over")
elif guess < "3":
    guess = input("the secret number is more than " + guess + ", try again: ")
    if guess == "3":
        print("your guess is correct")
    elif guess > "3":
        guess = input("the secret number is less than " + guess + ", try again: ")
        if guess == "3":
            print("your guess is correct")
        else:
            print ("you guessed wrong, start over")
    elif guess < "3":
        guess = input("the secret number is more than " + guess + ", try again: ")
        if guess == "3":
            print("your guess is correct")
        else:
            print("you guessed wrong, start over")