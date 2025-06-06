# Turn left until Karel is facing a wall. 
# We've provided 2 worlds for you to test your code on.

from stanfordkarel import *

def main():
    """Turns Karel until facing a wall."""

    while front_is_clear():
        turn_left()

if __name__ == '__main__':
    main()