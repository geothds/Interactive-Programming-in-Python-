# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random
#----------------------- helper functions ----------------------------
def name_to_number(name):
# converts name to number using if/elif/else and returns the result
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else: 
        print "Invalid name"
        return -1
        
def number_to_name(number):
# converts number to a name using if/elif/else and returns the result
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else: 
        return "invalid number"

#----------------------- rpsls function --------------------------------
def rpsls(player_choice):

# print out the message for the player's choice    
    print "Player chooses " + player_choice
# converts the player's choice to player_number using the function name_to_number()    
    player_number = name_to_number(player_choice)
# computes random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
# convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
# prints out the message for computer's choice    
    print "Computer chooses " + comp_choice
    
# computes difference of comp_number and player_number modulo    
    diff = (comp_number - player_number) % 5
    
# uses if/elif/else to determine winner, prints winner message
    if (player_number != -1) and (comp_choice != "invalid number"):
        if (diff == 1 or diff == 2):
            print "Computer wins!"
        elif (diff == 3 or diff == 4):
            print "Player wins!" 
        else: 
            print "Player and computer tie!"
    else:
        print "Error!"

# prints a blank line to separate consecutive games    
    print

#---------------------- Test ----------------------------
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



