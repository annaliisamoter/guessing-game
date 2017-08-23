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

def ask_to_play():
    score = None
    play = "Y"
    while play == "Y":
        new_score = play_game()
        if score == None:
            score = new_score
        else:
            if new_score < score:
                score = new_score
                print "Congrats {}!  You got a new best score!" .format(greeting)
            else:
                print "The current best score is {}.".format(score)
        play = raw_input("Do you want to play again? Y/N: ")
        play = play.upper()





def play_game():
    #input: none
    #output: score
    random_number = random.randint(1,100)
    print random_number
    count = 0
    while count <= 5:
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
                count +=1
                print "Well done, {}!  You found my number in {} tries!".format(
                    greeting, count)
                return count
    print "You lose! Too many tries!"

    # retry = raw_input("Do you want to try again? (Y/N): ")
    # if retry == "Y":
    #     ask_to_play()



ask_to_play()




