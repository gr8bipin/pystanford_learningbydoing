# If Karel is facing a wall, put a beeper down, turn left, and move forward. 
# If not, do nothing.

""" If Karel is facing a wall, put a beeper, turn left and move forward."""

from stanfordkarel import *

def main():
    if front_is_blocked():
        put_beeper()
        turn_left()
        move()

if __name__ == '__main__':
    main()