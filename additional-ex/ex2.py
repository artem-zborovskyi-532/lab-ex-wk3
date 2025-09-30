# Exercise 2:
    # The aim of this exercise is to draw a sudoku board (not to solve it). To start with,
    # we will be using a 4 × 4 board (as opposed to the classic 9 × 9).
    # a. Write a script that asks a user to enter 4 digits (comprised between 0 and
    # 4) separated by a white space, then stores each digit in a list and print the
    # list.
    # >>> enter 4 digits (0..4) separated by a space: 0 2 1 4
    # [0, 2, 1, 4]
    # b. Write a script that ask a user to enter a sequence of 4 digits 4 times, and
    # store those values in a 2D list. That is a list containing 4 lists of 4 digits
    # each. The script should print the 2D list. The output should look like:
    # [[0,2,1,4],[3,4,2,1],[1,2,3,4],[0,0,2,3]]
    # c. Modify your script so the output looks likes:
    # +-+-+-+-+
    # |0|2|1|4|
    # +-+-+-+-+
    # |3|4|2|1|
    # +-+-+-+-+
    # |1|2|3|4|
    # +-+-+-+-+
    # |0|0|2|3|
    # +-+-+-+-+
    # d. Modify your script so the 0s are replaced by a blank space.
    # +-+-+-+-+
    # | |2|1|4|
    # +-+-+-+-+
    # |3|4|2|1|
    # +-+-+-+-+
    # |1|2|3|4|
    # +-+-+-+-+
    # | | |2|3|
    # +-+-+-+-+

def can_cast_to_int(char:str) -> bool:
    try:
        int(char)
        return True
    except ValueError:
        return False

def is_valid(string:str) -> bool:
    elements = string.split(" ")

    if len(elements) != 4:
        return False
    
    for x in elements:
        if can_cast_to_int(x) == False:
            return False
        x = int(x)
        if x > 4 or x < 0:
            return False
        
    return True

def one_row():
    numbers = input("enter 4 digits (0..4) separated by a space: ")
    if is_valid(numbers) == False:
        return one_row()
    numbers = numbers.split()
    print(numbers)
    return numbers

def form_matrix():
    matrix = []
    for i in range(4):
        matrix.append(one_row())

    print(matrix)
    return matrix

def print_grid(matrix):
    for arr in matrix:
        print("+-+-+-+-+")
        str = "|"
        for x in arr:
            str = str + x + "|"
        print(str)
    print("+-+-+-+-+")

def replace_zeros(matrix):
    newMatrix = []
    for arr in matrix:
        newArr = []
        for x in arr:
            if int(x) == 0:
                newArr.append(" ")
            else:
                newArr.append(x)
        newMatrix.append(newArr)
    
    return newMatrix

matrix = form_matrix()
print_grid(matrix)
matrix = replace_zeros(matrix)
print_grid(matrix)