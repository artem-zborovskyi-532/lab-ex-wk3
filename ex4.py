# Exercise 4:
    # a. Write a script that takes a sentence from the user without any punctuation
    # and prints the sentence without any white spaces. Note a white space is
    # represented by ' ', and an empty string is represented by ''.
    # >>> enter a sentence: this is a SHORT sentence
    # thisisaSHORTsentence

    # b. Same as above except that each word in the output should start with a
    # upper case letter and all other letter should be lower case (also known as
    # CamelCase).
    # >>> enter a sentence: this is a SHORT sentence
    # ThisIsAShortSentence

    # c. Write a script that takes a sentence from a user written in CamelCase
    # (without any blank spaces), creates the list of words from that sentence,
    # and then prints that list.
    # >>> enter a sentence in CamelCase: ThisIsAShortSentence
    # ['This','Is','A','Short','Sentence']

def has_punctuation(string):
    for char in string:
        if char.isalpha() == False and char != " ":
            return False
        
    return True

def remove_whitespaces():
    string = input("enter a sentence: ")
    if has_punctuation(string) == False:
        return remove_whitespaces()

    print(string.replace(" ", ""))

def camelcase():
    string = input("enter a sentence: ")
    if has_punctuation(string) == False:
        return camelcase()
    
    res = ""
    for word in string.split():
        res += word.capitalize()

    print(res)

def split_camelcase():
    string = input("enter a sentence in CamelCase: ")
    string = string[:1].lower() + string[1:]

    res = ""
    word = ""
    index = 0
    
    for char in string:
        if index == len(string):
            res += word
        if char.islower() == True: # lowercase letter
            word += char
        else: # uppercase letter
            res = res + word + " "
            word = char

        index += 1

    print(res)

split_camelcase()