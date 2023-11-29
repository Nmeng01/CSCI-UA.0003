"""
This script takes a string and prints it backwards

Submitted by Nicholas Meng, NetID ndm9914
The user inputs a string and the script creates a new string
which updates with the inputted string backward. The script prints
each letter and then prints the full word backwards.
"""

string = input("Input a word: ")
new_string = ''
for letter in string:
    new_string = letter + new_string
for letter in new_string:
    print(letter)
print(f'{string} backwards is {new_string}')