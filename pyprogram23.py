## Invert the spot Karel is currently standing on -- if there is a beeper present, pick it up; if there isn't a beeper present, 
# put one down. (This may be a convenient helper function for the "Invert" practice problem later in this lesson!) 
# There are 2 worlds for you to test your code on.

from stanfordkarel import *

def main():
    
    if beepers_present():
        put_beeper()
    else:
        pick_beeper()
    print("Program successfully run.")

if __name__ == '__main__':
    main()
