# Exercise 2: Simple for loops
    # a. Write a program that prompts the user to input a positive integer N and
    # print the sum of all the positive even numbers smaller or equal to N.
    # b. Write a program that prompts the user to input a positive integer. It should
    # then print the multiplication table of that number.
    # c. Write a program to print the factorial value n! of any number entered
    # through the keyboard. You must use a for loop, and not any math function
    # that already exists. To refresh your memory:
    # 𝑛! = 𝑛 × (𝑛 − 1) × (𝑛 − 2) × … × 1

def positive_integer():
    x = int(input("Enter a positive integer -> "))
    return x if x > 0 else positive_integer()

def is_even(x):
    return True if x % 2 == 0 else False

def even_numbers():
    n = positive_integer()
    for i in range(1, n + 1):
        if is_even(i):
            print(i)

def multiplication_table():
    n = positive_integer()
    for i in range(1, 11):
        print(n, ' x ', i, ' = ', n * i)

def factorial():
    n = positive_integer()
    total = 1
    for i in range(1, n + 1):
        total *= i

    print(f"{n}! = {total}")

factorial()