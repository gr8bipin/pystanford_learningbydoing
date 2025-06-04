from stanfordkarel import *

def main():
    """
    Makes Karel place beepers in a square (4 beepers total) and end in the same position Karel starts in.
    """

    put_beeper()
    move()
    turn_left()
    put_beeper()
    move()
    turn_left()
    put_beeper()
    move()
    turn_left()
    put_beeper()
    move()
    turn_left()

if __name__ == '__main__':
    main()
