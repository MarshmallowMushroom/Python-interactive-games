# Rock-paper-scissors-lizard-Spock 



# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
# Rock-paper-scissors-lizard-Spock 

import random

def name_to_number(name):
    # convert string to number
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "Invalid player's choice"
    return number
        
    
def number_to_name(number):
    # convert number to string
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print "number doesn't match with names"
    return name
    

def rpsls(player_choice): 
    # print out a blank line to separate consecutive games
    # print out the message for the player's choice
    # convert player's choice to number
    print
    print "Player chooses " + player_choice
    player_number = name_to_number (player_choice) 
    
    # compute random guess for comp_number and convert to comp_choice
    # print out the message for computer's choice
    comp_number = random.randrange(0,5)
    comp_name = number_to_name (comp_number)
    print "Computer chooses " + comp_name
    
    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number)%5
    if diff == 0:
        print "Player and computer tie!"
        print 
    elif diff == 1:
        print "Computer wins!"
        print 
    elif diff == 2:
        print "Computer wins!"
        print 
    elif diff == 3:
        print "Player wins!"
        print 
    elif diff == 4:
        print "Player wins!"
        print 
    else:
        print "Something is wrong here, please check the logic!"
        print 
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


