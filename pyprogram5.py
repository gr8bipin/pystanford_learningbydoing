## Age-related riddle. How old are they?

# main function definition
def main():

    # assign age of anton, beth, chen, drew, ethan
    anton_age = 21
    beth_age = anton_age + 6
    chen_age = beth_age + 20
    drew_age = chen_age + anton_age
    ethan_age = chen_age

    # print their age on console
    print("Anton is", str(anton_age))
    print("Beth is", str(beth_age))
    print("Chen is", str(chen_age))
    print("Drew is", str(drew_age))
    print("Ethan is", str(ethan_age))

# Call main function using this line
if __name__ == '__main__':
    main()
