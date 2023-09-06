import random


def guess_number():

    number = random.randint(1, 10)

    guess = int(input("Guess a number between 1 and 100: "))

    if guess == number:
        print("Congratulations! You guessed the correct number.")
    else:
        print("Sorry, the correct number is {}. Please try again.".format(number))


guess_number()
