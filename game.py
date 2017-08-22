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
