# Exercise 1: Simple while loops
    # a. Write a program to keep asking for a number until you enter a negative
    # number. At the end, print the sum of all 
    # b. Write a program to keep asking for a number until you enter a negative
    # number. At the end, print the average of all entered numbers numbers.
    # c. Write a program to keep asking for a number until you enter a negative
    # number. At the end, print the number of even numbers entere

def user_input_sum():
    userInput = int(input("Enter number -> "))
    total = userInput

    while userInput >= 0:
        userInput = int(input("Enter number -> "))
        total += userInput

    print(f"Total: {total}")

def user_input_average():
    userInput = int(input("Enter number -> "))
    total = userInput
    numOfInputs = 1

    while userInput >= 0:
        userInput = int(input("Enter number -> "))
        total += userInput
        numOfInputs += 1

    average = total / numOfInputs

    print(f"Average: {average}")

def is_even(x):
    return True if x % 2 == 0 else False

def user_input_even():
    userInput = int(input("Enter number -> "))
    numOfEven = 0
    if is_even(userInput):
        numOfEven += 1

    while userInput >= 0:
        userInput = int(input("Enter number -> "))
        if is_even(userInput):
            numOfEven += 1

    print(f"Number of even inputs: {numOfEven}")

def validInput(options):
    print(">> Select your option:")

    for index, option in enumerate(options):
        print(f"{index + 1} - {option}")
    
    userInput = int(input("Enter your choice -> "))

    if userInput < 1 or userInput > len(options):
        return validInput(options)

    return userInput

def main():
    programOptions = ["Sum", "Average", "Even numbers"]
    selectedProgram = validInput(programOptions)

    if selectedProgram == 1:
        user_input_sum()
    elif selectedProgram == 2:
        user_input_average()
    else:
        user_input_even()

main()