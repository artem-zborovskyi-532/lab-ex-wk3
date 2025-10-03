# Exercise 5: Cryptography, Caesar Cipher
    # In cryptography, a Caesar cipher, also known as the
    # shift cipher, is one of the simplest and most widely
    # known encryption techniques. It is a type of substitution
    # cipher in which each letter in the plain text is replaced
    # by a letter some fixed number of positions down the
    # alphabet.
    # For example, with a shift of 3, A would be replaced by
    # D, B would become E, and so on. The method is named
    # after Julius Caesar, who used it to communicate with
    # his generals.
    # Mathematically, a Caesar cipher can be expressed by the following equation:
    # c = (p + a) mod 26
    # Here, ‘mod 26’ means that you
    # use clock arithmetic for values
    # greater than 26, i.e., 0=26 mod
    # 26, 1=27 mod 26, 2=28 mod 26,
    # …, 0=52 mod 26, 1=53 mod 26,
    # …, 10=62 mod 26, and so on.
        # a. Write a script that encrypts a plain text into a cypher text using the Caesar
        # Cipher algorithm.
        # b. Write a script that decrypts a cipher text into a plain text using the Caesar
        # Cipher algorithm.

def is_plain(s: str) -> bool:
    return all(c.isalpha() or c.isspace() for c in s)

def letter_pos(letter: str) -> int:
    letter = letter.lower()
    return ord(letter) - ord('a') + 1

def letter_from_pos(pos: int, upper: bool) -> str:
    return chr(ord('a') + pos - 1).upper() if upper == True else chr(ord('a') + pos - 1);

def caesar_encrypt():
    str = input("Enter plain text to encrypt -> ")
    if is_plain(str) == False:
        return caesar_encrypt()
    
    shift = int(input("Enter number of shifts for letter's position -> "))
    while shift < 0:
        shift = int(input("Enter number of shifts for letter's position -> "))
    
    res = ""
    for char in str:
        if char == " ":
            res += char
            continue
        c = (letter_pos(char) + shift) % 26
        res += letter_from_pos(c, char.isupper())

    print(f"Encrypted string: {res}")

def caesar_decrypt():
    str = input("Enter encrypted text to decrypt -> ")
    if is_plain(str) == False:
        return caesar_decrypt()
    
    shift = int(input("Enter number of shifts for letter's position -> "))
    while shift < 0:
        shift = int(input("Enter number of shifts for letter's position -> "))

    res = ""
    for char in str:
        if char == " ":
            res += char
            continue
        c = (letter_pos(char) - shift) % 26
        res += letter_from_pos(c, char.isupper())

    print(f"Decrypted string: {res}")