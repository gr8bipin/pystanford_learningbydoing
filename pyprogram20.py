# Write code which will "clean" the spot Karel is standing on by picking up beepers until there aren't any left 
# (you can't pick_beeper() if there aren't any!). We've provided 2 worlds for your to test your code on.

from stanfordkarel import *

def main():
    """Picks up beepers in current spot until there are none left."""
    while beepers_present():
        pick_beeper()

if __name__ == '__main__':
    main()