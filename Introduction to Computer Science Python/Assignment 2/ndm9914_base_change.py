"""
This script converts a natural number of base 10 into the same number but with a different
base between 2 and 9.

Submitted by Nicholas Meng, NetID ndm9914
The user inputs a natural number to be converted and a base number. If the base number is 
not between 2 and 9, the program asks the user to input a number within these parameters 
until an appropriate number is given. Once a base between 2 and 9 is given, the program 
uses the modulo function to produce each converted digit and the floor division function
to loop through each digit.
"""
initial_number = int(input("What number are you interested in converting? "))
if initial_number == 0:
    print("The number 0 is always represented by the number 0 no matter what base is used.")
else:
    while True:
        base_number = int(input("What base should we use? "))
        if 2 <= base_number <= 9:
            break
        print("The base has to be between 2 and 9. Please try again.")
        print()
    temp = initial_number
    new_base_number = ""
    while temp != 0:
        new_base_number = str(temp % base_number) + new_base_number
        temp = temp // base_number
    print(f"The number {initial_number} is represented by {new_base_number} in base {base_number}")

