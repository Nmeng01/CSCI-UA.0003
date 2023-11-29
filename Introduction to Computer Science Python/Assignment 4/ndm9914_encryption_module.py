"""
This module creates a list of characters and defines functions for encryption and decryption based on this list

Submitted by Nicholas Meng, NetID ndm9914

"""

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
            "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C",
            "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
            "S", "T", "U", "V", "W", "X", "Y", "Z", ".", ",", ":", ";", "!", "?", "-",
            "&", "(", ")", "#"]


def encryption(message, key):
    """
    This function takes a string for encryption and a key value that determines each letter of the new string.
    """
    new_message = ''
    for letter_pos in range(len(message)):
        list_pos = alphabet.index(message[letter_pos])
        if list_pos < len(alphabet) - key:
            new_message += alphabet[list_pos + key]
        else:
            wrap = (list_pos + key) - len(alphabet)
            new_message += alphabet[wrap]
    return new_message


def decryption(message, key):
    """
    This function takes a string for decryption and a key value that determines each letter of the new string.
    """
    new_message = ''
    for letter_pos in range(len(message)):
        list_pos = alphabet.index(message[letter_pos])
        if list_pos - key >= 0:
            new_message += alphabet[list_pos - key]
        else:
            wrap = len(alphabet) + (list_pos - key)
            new_message += alphabet[wrap]
    return new_message
