# Move Karel forward until you run into a wall (don't walk through the wall!). 
# We've provided 3 worlds for you to test your code on!

from stanfordkarel import *

def main():
    """Moves Karel forward until a wall."""
    while front_is_clear():
        move()

if __name__ == '__main__':
    main()