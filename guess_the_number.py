# "Guess the number" mini-project #2
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num_range = 100

def new_game():
# Ιnitializes global variables secret_number and count 
    global secret_number
    global count
# Sets parameteres and starts a new game   
    count = int(math.ceil(math.log(num_range + 1, 2)))
    secret_number = random.randrange(0, num_range)
    print "New game. Range is from 0 to", num_range - 1
    print "Number of remaining guesses is", count

def range100():
# Button that changes the range to [0,100) and starts a new game 
    print
    global num_range
    num_range = 100
    new_game()

def range1000():
# Button that changes the range to [0,1000) and starts a new game     
    print
    global num_range
    num_range = 1000
    new_game()

def input_guess(guess):
# Main game logic goes here
    global count
    num = int(guess)
    if (num >= 0 and num < num_range):
        if count <= 0:
            print "\nYou ran out of guesses. Secret number is", secret_number, "\n"
            new_game()
        else:
            print "\nGuess was", num
            count -= 1
            if (num < secret_number):
                print "Higher!"
                print count, "guesses remaining!"
            elif (num > secret_number):
                print "Lower!"
                print count, "guesses remaining!"
            else:
                print "Correct!\n"
                new_game()
    else:
        print "\nGuess within appropriate range!"

# Create frame
frame = simplegui.create_frame('Guess the number!', 300, 300)

# Register event handlers for control elements and start frame
frame.add_input('Enter a number!', input_guess, 120)
frame.add_button('Range is [0,100)', range100)
frame.add_button('Range is [0,1000)', range1000)

# frame start
frame.start()

new_game()