"""
This script takes the file with info about squirrels and searches for keywords

Submitted by Nicholas Meng, NetID ndm9914
The user inputs the filename and the string they want to search for.
Then, using string methods to search each individual line in the file,
the script returns the number of times the string appears in the whole file,
how many lines it appears in, and how many times it appears in the specific
column inputted by the user.
"""
while True:
    filename = input("Input the filename with the information about squirrels: ")
    if not filename:
        exit()
    squirrels_file = open(filename)
    header_line = squirrels_file.readline()
    string = input("What string would you like to look for? (case insensitive): ")
    labels_list = (header_line.strip()).split(",")

    column_number = 1
    for label in labels_list:
        print(f"{column_number}) {label}")
        column_number += 1
    print()
    while True:
        column = int(input("Which column should be checked? (1 to " + str(len(labels_list)) + "): "))
        if 1 <= column <= len(labels_list):
            break
    print(f"Checking {labels_list[column - 1]} column...")

    lines_with_string = 0
    occurrences = 0
    column_occurrences = 0
    for item in squirrels_file:
        item = item.lower()
        if item.find(string.lower()) >= 0:
            lines_with_string += 1
            occurrences += item.count(string.lower())
            item_list = item.split(",")
            if item_list[column - 1].find(string.lower()) >= 0:
                column_occurrences += 1
    print(f"The string {string} occurs in {lines_with_string} line(s) and a total of {occurrences} time(s).")
    print(f"It occurs in {column_occurrences} line(s) in the column {labels_list[column - 1]}.")
    print()

