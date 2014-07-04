# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# initialize global variables used in your code
secret_number = 0
num_range = 100
count = 7

# helper function to start and restart the game
def new_game():
    if num_range == 100:
        range100()
    elif num_range == 1000:
        range1000()
    else:
        print "Check your code, num_range can only be 100 or 1000"

# define event handlers for control panel
def range100():
    # button that changes range to range [0, 100) and restarts
    global num_range 
    global count
    num_range = 100
    count = 7
    print
    print "New game. Range is from 0 to 100."
    print "Number of remaining guesses is 7"
    global secret_number
    secret_number = random.randrange(0,100)
    return secret_number
         
def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range 
    global count
    num_range = 1000
    count = 10
    print
    print "New game. Range is from 0 to 1000."
    print "Number of remaining guesses is 10"
    global secret_number
    secret_number = random.randrange(0,1000)
    return secret_number
            
def input_guess(guess):
    # main game logic goes here
    global secret_number
    global count
    count -= 1
	print
	print "Guess was " + guess + '.'
    print "Number of remaining guesses is " + str(count) + "."
    if count > 0:
        if int(guess) < secret_number:
            print "Higher!"
        elif int(guess) > secret_number:
            print "Lower!"
        else:
            print "Correct! You win!"
            new_game()
    else:
        if int(guess) == secret_number:
            print "Correct! You win!"
        else:
            print "Oops, you ran out of guesses. The number was " + str(secret_number) + '.'
        new_game()
          
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)
frame.set_canvas_background("Red")

# register event handlers for control elements
button1 = frame.add_button("Range: [0 - 100)", range100, 200)
button2 = frame.add_button("Range: [0 - 1000)", range1000, 200)
inp = frame.add_input("Enter a guess", input_guess, 200)
                     
# call new_game and start frame
new_game()
frame.start()
