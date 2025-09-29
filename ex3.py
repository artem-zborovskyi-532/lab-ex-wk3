# Exercise 3: Palindrome
# A palindrome is a word, phrase, number, or other sequence of units that may be
# read the same way in either direction, 'radar' and 'Delia saw I was ailed'
# are palindromes, whereas 'reader' is not. Write a program that take a sentence
# or a word as an input and print if it is a palindrome or not.

def is_palindrome(string):
    reverse = string.lower()[::-1]
    return True if reverse == string.lower() else False

# The advanced bit
# 'Dammit, I'm mad!' is also considered a palindrome when neither punctuation nor
# spaces are considered. Change your program so it can recognise these
# palindromes too.

def is_palindrome_advanced(string):
    filteredString = ""
    for char in string:
        if char.isalpha():
            filteredString += char

    return is_palindrome(filteredString)