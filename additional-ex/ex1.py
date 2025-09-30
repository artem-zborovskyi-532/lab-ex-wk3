# Exercise 1:
    # a. Write a script asking the user to enter a series of positive integers separated
    # by a white space and then printout the number of even numbers that were
    # entered. For example:
    # >>> enter a series of numbers: 1 2 4 3 6 8 5 2 11 100 101
    # There are 6 even numbers
    # You will need to use the built-in function input() and the string method
    # split(). You should also remember that we can convert a string
    # representing an integer into an int like so:
    # >>> twenty = int('20')
    # >>> type(twenty)
    # <class 'int'>
    # >>> twenty + 2
    # 22
    # b. Same question except we would like to have the list of even numbers as
    # well
    # >>> enter a series of numbers: 1 2 4 3 6 8 5 2 11 100 101
    # There are 6 even numbers: 2 4 6 8 2 100
    # c. Same question except we would like to have the list of even numbers
    # without any duplicates. i.e. remove the second 2 in the example below.
    # >>> enter a series of numbers: 1 2 4 3 6 8 5 2 11 100 101
    # There are 5 distinct even numbers: 2 4 6 8 100

def count_even():
    numbers = input("enter a series of numbers: ")
    numbers = numbers.split()
    count = 0

    for num in numbers:
        num = int(num)
        if num % 2 == 0:
            count += 1

    print(f"There are {count} even numbers")

def list_even():
    numbers = input("enter a series of numbers: ")
    numbers = numbers.split()
    count = 0
    even = []

    for num in numbers:
        if int(num) % 2 == 0:
            count += 1
            even.append(num)

    print(f"There are {count} even numbers: {" ".join(even)}")

def distinct_even():
    numbers = input("enter a series of numbers: ")
    numbers = numbers.split()
    count = 0
    even = []

    for num in numbers:
        if int(num) % 2 == 0 and even.count(num) == 0:
            count += 1
            even.append(num)

    print(f"There are {count} distinct even numbers: {" ".join(even)}")