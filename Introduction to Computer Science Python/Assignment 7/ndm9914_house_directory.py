"""
This script takes a file listing house representatives and allows the user to find info on a specific member.

Submitted by Nicholas Meng, NetID: ndm9914
This script takes a file and creates mini-dictionaries using the file's column labels as the keys and each
voting representative's info as the values. These mini-dictionaries are placed in an encompassing dictionary using
the state and district ID as the keys and the rest of the info on the representative as the values.
The script then asks the user to enter a state and district ID, and it will search for the corresponding representative.
If nobody is found, the script will let the user know, but if they are found, then their information is provided.
An empty input ends the script.
"""

import csv

# Places each rep's info in a mini-dictionary. The mini-dictionaries are then placed in an encompassing dictionary
filename = input("What is the file with the House of Reps in 2019? ")
if not filename:
    exit()
house_directory = open(filename, encoding="latin1")
labels = house_directory.readline()
labels_list_unedited = (labels.strip()).split(",")
labels_list = [label.strip().lower() for label in labels_list_unedited]
house_reader = csv.reader(house_directory)
encompassing_dict = {}
for row in house_reader:
    if row[1] == "At Large" or row[1].isnumeric():
        row = [item.strip() for item in row]
        representative_data = dict(zip(labels_list, row))
        encompassing_dict_key = (representative_data["state or territory"].lower(),
                                 int(representative_data["district or representation type"])
                                 if representative_data["district or representation type"].isnumeric()
                                 else representative_data["district or representation type"].lower())
        encompassing_dict[encompassing_dict_key] = representative_data

# Asks the state and district ID for the representative and returns their info if they exist
while True:
    area = input("For which state/territory would you like information? ")
    if not area:
        break
    area = area.lower().strip()
    district_id = input("Please provide the district number/type of representative: ")
    if not district_id:
        break
    district_id = int(district_id) if district_id.isnumeric() else district_id.strip().lower()
    query = (area, district_id)
    for key, value in encompassing_dict.items():
        if query == key:
            print(f"The representative for district/type of representative {district_id} in the state/territory of "
                  f"{area} is {encompassing_dict[key]['given name']} {encompassing_dict[key]['family name']}. "
                  f"The phone number is {encompassing_dict[key]['phone']}.")
            break
    else:
        print(f"No representative was found for district/type of representative {district_id} in the state/territory of "
              f"{area}.")
house_directory.close()