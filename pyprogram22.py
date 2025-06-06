## Fill the entire bottom row of the world with beepers, making sure not to forget to 
# put a beeper on the spots Karel starts / ends on. 
# This tests your understanding of the fencepost problem from lecture.

from stanfordkarel import *

def main():
    """
    Fills entire bottom row of any sized world with beepers.
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

if __name__ == '__main__':
    main()