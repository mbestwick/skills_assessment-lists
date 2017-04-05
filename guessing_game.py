"""A number-guessing game."""

import random

print "hi my name is michela"


def guess_check(guess, secret_number):
    """check user guess against generated number"""
    try:
        guess = int(raw_input('guess: '))
    except:
        print "A number only please"
        return 0
    if guess < 1 or guess > 100:
        print "Really?? A number between 1 and 100 please"
    elif guess > secret_number:
        print "Too high!"
    elif guess < secret_number:
        print "Too low!"
    return guess


print "Hello, welcome to our game"
name = raw_input('username: ')
print "Hi "+name+", guess a number between 1 and 100"
play_again = 'yes'
lowest_guess = 1000


while play_again == 'yes':
    secret_number = random.randint(1, 100)
    num_of_guesses = 0
    print "shh...the secret number is %d" % (secret_number)
    guess = 0
    while secret_number != guess and num_of_guesses < 10:
        guess = guess_check(guess, secret_number)
        num_of_guesses += 1
        if num_of_guesses > 9:
            print "You've exceeded total number of guesses!! Game over"
    if secret_number == guess:
        print "You got it right with %d guesses. The number was %d" % (num_of_guesses, secret_number)
    if num_of_guesses < lowest_guess:
        lowest_guess = num_of_guesses
        print "Congratulations! You improved your best score to %d" % (lowest_guess)
    print "So %s, would you like to play again?" % (name)

    play_again = raw_input('response ')