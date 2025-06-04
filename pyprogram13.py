# This tells python who Karel is!
from stanfordkarel import *

# this program executes in a special function called main
def main():
    move()
    for i in range(5):
        put_beeper()
    move()

# This is "boilerplate" code which launches your code
# when you hit the run button
if __name__ == '__main__':
    main()