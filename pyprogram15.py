## Place 10 beepers on the spot Karel is currently standing on.

from stanfordkarel import *

def main():
    """
    Places 10 beepers in the spot that Karel is standing on
    """
    for i in range(10):
        put_beeper()

if __name__ == '__main__':
    main()