# Karel is in the top left corner of a 2 row, 3 column world with three slots in the 
# bottommost row, as such:

# Write a program which will place beepers in each slot of the bottom row, 
# so that the end world looks like this:

# For an extra challenge, try writing this code with a while loop instead so that 
# it works for worlds with any number of columns / slots!


from stanfordkarel import *

def main():
    """
    Place beepers in the bottom row of a world with 3 slots.
    """
    
    while front_is_clear():

        turn_right()
        move()
        turn_left()
        put_beeper()
        turn_left()
        move()
        turn_right()
        move()

        turn_right()
        move()
        turn_left()
        put_beeper()
        turn_left()
        move()

        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        put_beeper()
        turn_left()
        move()
        turn_right()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    main()