"""
The code takes a csv file and allows the user to create a new tsv file with specific columns from the original csv file

Submitted by Nicholas Meng, NetID ndm9914
The code first extracts the labels from the original file and places the actual information in a table (list of lists).
The script prints out the columns that the user can put in a separate file and the user inputs the columns he/she wants
to extract (using column numbers). The script ensures that only certain numbers can be inputted and writes their
respective columns in a new tsv file. The script can keep taking inputs for more tsv files until the user inputs an
empty input, at which point the code stops and the user receives their files.
"""
filename = input("Input the filename with the information about consumer goods: ")
if not filename:
    exit()
goods_file = open(filename)
header_line = goods_file.readline()
labels_list = (header_line.strip()).split("\t")

price_table = []
for line in goods_file:
    row_list = (line.strip()).split("\t")
    price_table.append(row_list)
print("Prices of the following products were found:")
for count, label in enumerate(labels_list[1:], 1):
    print(f"{count}) {label}")
index = 1
filename = filename.replace(".csv", ".tsv")

while True:
    print()
    print("Press enter without inputting anything else to exit and receive your files.")
    columns = input("Select the columns you desire: (separated by commas) ")
    if not columns:
        exit()
    columns = " ".join(columns.split(",")).split()
    columns_set = {number for number in columns}
    columns_list = [int(item) for item in columns_set if item.isnumeric() and 1 <= int(item) < len(labels_list)]
    columns_list += [0]
    columns_list.sort()
    labels_out_file = []
    for column in columns_list:
        labels_out_file.append(labels_list[column])
    labels_out_string = "\t".join(labels_out_file)
    out_file = open(f"Subset {index} of {filename}", "wt")
    out_file.write(labels_out_string + "\n")
    for nested_list in price_table:
        saved_row = []
        for column in columns_list:
            saved_row.append(nested_list[column])
        saved_row_string = "\t".join(saved_row)
        out_file.write(saved_row_string + "\n")
    out_file.close()
    print(f"Information saved in 'Subset {index} of {filename}.'")
    index += 1



