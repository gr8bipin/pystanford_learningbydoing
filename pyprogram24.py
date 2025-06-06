# # Write code to move forward once and put a beeper down if Karel isn't facing a wall.
#  If Karel is facing a wall, don't move and just put a beeper down.

# One solution to this uses an if statement and an else statement. 
# One solution to this just uses an if statement. Can you think of both?

from stanfordkarel import *

def main():
    """
    Karel will move and put a beeper down if there isn't a wall; 
    Karel will just put a beeper down if there is.
    """

    if front_is_clear():
        move()
        put_beeper()
    else:
        put_beeper()

if __name__ == '__main__':
    main()