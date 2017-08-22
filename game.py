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

def play_game():

    random_number = random.randint(1,100)
    count = 0
    while True:
        try:

            get_guess = int(raw_input("Guess a number between 1 and 100: "))

        except ValueError:
            print ("Oops! That was not a valid number. Try again...")
            continue

        if get_guess not in range(1, 101):
            print "You Fool! That is not an acceptable number!"

        else:
            if get_guess != random_number:
                count += 1
                if get_guess > random_number:
                    print "your guess is too high, try again"
                else:
                    print "your guess is too low, try again"
            else:
                print "Well done, {}!  You found my number in {} tries!".format(
                    greeting, count)
                replay = raw_input("Would you like to play again? Y/N: ")
                replay = replay.upper()
                if replay == "Y":
                    play_game()
                else:
                    print "thanks for playing!"
                    break


play_game()




