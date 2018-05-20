import random
from random import randint
def game ():
    right_choices = 0
    user_input = int(raw_input("guess a number from 1 to 9 or type 0 to exit: "))
    if 0<user_input <11:
        robot_choice = randint(1,10)
        if user_input == robot_choice:
            print "Congrat you win! :) "
            game()
        if user_input < robot_choice:
            print "Wrong answer your choice is smaller than the robot choice"
            game()
        if user_input > robot_choice:
            print "Wrong answer your choice is bigger than the robot choice"
            game()
    else:
        if user_input == 0:
            exit()
        else:
            game()
        
game()