from stanfordkarel import *

def main():
    """
    Karel should place 5 beepers in the bottommost row of the world, 
    if the world is more than 5 columns wide.
    If the world is less than 5 columns wide, Karel should fill the bottommmost row 
    with beepers and not walk through any walls.
    """
    put_beeper()
    for i in range(4):
        if front_is_clear():
            move()
            put_beeper()
        
if __name__ == '__main__':
    main()