## Get Karel to turn based on whether or not a beeper is present -- if there is a beeper
#  in the current spot, turn left; if there isn't a beeper in the current spot, 
# turn right.
from stanfordkarel import *

def main():
    if beepers_present():
        turn_left()
    else:
        turn_right()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
