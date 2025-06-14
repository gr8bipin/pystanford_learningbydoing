import random

def main():

    print("Addition Mastery Academy")
    
    correct_in_a_row = 0

    while correct_in_a_row < 3:

        # Random Number Generation for addition
        input1 = random.randint(10, 99)
        input2 = random.randint(10, 99)
        correct_answer = input1 + input2

        # Ask user an answer
        print(f"What is {input1} + {input2}? ")
        try:
            user_answer = int(input("The correct answer is "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue
    
        # Check user_answer with correct_answer
        if user_answer == correct_answer:
            correct_in_a_row += 1
            print("Correct answer!")
            print(f"There are {correct_in_a_row} correct in a row.")
        else:
            correct_in_a_row = 0
            print("Incorrect Answer!")
            print("Try again.")

    print("Congratulations! You have mastered addition.")

if __name__ == '__main__':
    main()