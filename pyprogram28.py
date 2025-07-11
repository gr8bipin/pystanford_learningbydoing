# Place 10 beepers in each position in the bottom row. 
# Karel will begin in the bottom left corner of a world with no beepers; 
# Karel should end in the bottom right corner of the world with 10 beepers across 
# the bottom row (including the positions Karel starts and ends on!).



# You could start by writing this assuming you know the number of columns 
# (i.e. the length of each row) beforehand, and then tweak your code 
# to make it work for any number of columns!

from stanfordkarel import *

def main():
    """
    Put 10 beepers in every cell in the bottom row of the world.
    """

    while front_is_clear():
        for i in range(10):
            put_beeper()
        move()
    for i in range(10):
        put_beeper()

if __name__ == '__main__':
    main()