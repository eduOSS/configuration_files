#template for "Guess the number" mini-project

# input will come from buttons and an input field

# all output for the game will be printed in the console
 

import random

import simplegui

# initialize global variables used in your code

range_num = 100


# helper function to start and restart the game

def new_game():

    global secret_num, range_num, count

    if(range_num == 100):

        count = 7

    else:

        count = 10

    secret_num = random.randrange(0, range_num)

    print"New game, Range is from 0 to", range_num

    print"Number of remaining guess is", count

    print""

def range100():

    # button that changes range to range [0,100) and restarts

    global range_num, count

    range_num = 100

    count = 7

    new_game()


def range1000():

    # button that changes range to range [0,1000) and restarts

    global range_num, count

    range_num = 1000

    count = 10

    new_game()
 
def input_guess(guess):

     # main game logic goes here 

    global guess_num, count, secret_num

    guess_num = int(guess)

    count -= 1

    print"Guess was", guess_num 

    print"Number of remaining guess is",count

    if(count <= 0):

        print"You ran out of guess. The number was", secret_num

        print""

        new_game()

    else:

        if(guess_num > secret_num):

            print"Lower!"

        elif(guess_num < secret_num):

            print"Higher!"

        else:

            print"Correct!" 

            print""

            new_game()   

    print""

 

# create frame        

frame = simplegui.create_frame("Guess the number", 200, 200)

 

# register event handlers for control elements

frame.add_button("Range is [0, 100)", range100, 200)

frame.add_button("Range is [0, 1000)", range1000, 200)

frame.add_input("Enter a guess", input_guess, 200)

 

# call new_game and start frame

frame.start()

new_game() 


