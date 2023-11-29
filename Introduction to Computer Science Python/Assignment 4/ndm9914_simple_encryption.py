"""
This script offers an encryption and decryption tool to reveal or hide secret messages

Submitted by Nicholas Meng, NetID ndm9914
The scripts imports a separate module that has an encryption and decryption function.
This script simply asks the user if they want to encrypt or decrypt something, and then
they enter the string they are translating.The script continues asking for
messages until enter is pressed.
"""

import ndm9914_encryption_module as encrypt

encryption_key = 3

while True:
    while True:
        option = input("Do you want to encrypt (E) or decrypt (D)? ")
        if not option:
            exit()
        elif option == "E" or option == "D":
            message_option = "encrypt" if option == "E" else "decrypt"
            break
        elif option == "*":
            while True:
                encryption_key = input("Enter a positive integer to use as the secret key: ")
                if not encryption_key:
                    continue
                else:
                    encryption_key = int(encryption_key)
                    break
        print()
    while True:
        string = input(f"What message do you want to {message_option}? ")
        if not string:
            continue
        elif option == "E":
            print(encrypt.encryption(string, encryption_key))
            break
        elif option == "D":
            print(encrypt.decryption(string, encryption_key))
            break
    print()




