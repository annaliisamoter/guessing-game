"""A number-guessing game.
greet player
get player name
choose random number between 1 and 100
repeat forever:
    get guess
    if guess is incorrect:
        give hint
        increase number of guesses
    else:
        congratulate player"""

# Put your code here
import random
greeting = raw_input("Hello, what's your name? ")

random_number = random.randint(1,100)
while True:
    count = 0
    get_guess = int(raw_input("Guess a number between 1 and 100: "))
    if get_guess != random_number:
        count += 1
        if get_guess > random_number:
            print "your guess is too high, try again"
        else:
            print "your guess is too low, try again"


