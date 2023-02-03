import random

number = random.randint(1, 100)

guess = 0

while guess != number:
    try:
        guess = int(input("\n Guess the number between 1 and 100: "))
        if guess == number:
            print("\n Congratulations!! you've found the number, it is {}".format(number))
        elif guess > number:
            print("\n {} is higher".format(guess))
        elif guess < number:
            print("\n {} is lower".format(guess))
    except ValueError:
        print("\n That is not a valid number, try again")

