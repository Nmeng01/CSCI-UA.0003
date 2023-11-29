"""
This script takes a file listing house representatives and allows the user to find info on a specific member.

Submitted by Nicholas Meng, NetID ndm9914
The script takes a file with house reps and their info, and it finds certain columns with important information.
Then the script asks the user to input a state/territory and the district ID of the specific member they are
looking for. The code runs through each line of the file searching for the specified criteria and returns the
info it exists in the file. If it does not exist, the script will let the user know. The user can keep inputting
searches until they enter a blank input, at which point the script ends.
"""
file_name = input("Which file contains the information about the House of Representatives? ")
if not file_name:
    exit()
reps_file = open(file_name, encoding='windows-1252')
header_line = reps_file.readline()
labels_list_unedited = (header_line.strip()).split(",")
labels_list = [label.strip().lower() for label in labels_list_unedited]
position = reps_file.tell()
family_name_column = -1
given_name_column = -1
district_column = -1
phone_column = -1

for label in labels_list:
    if "family" in label:
        family_name_column = labels_list.index(label)
    elif "given" in label:
        given_name_column = labels_list.index(label)
    elif "district" in label:
        district_column = labels_list.index(label)
    elif "phone" in label:
        phone_column = labels_list.index(label)
if family_name_column == -1 or given_name_column == -1 or district_column == -1 or phone_column == -1:
    exit()
while True:
    area = input("For which state/territory would you like information? ")
    if not area:
        exit()
    area_lower = area.lower()
    district_id = input("Please provide the district number/type of representative: ")
    if not district_id:
        exit()
    district_id_ = district_id.lower() if district_id.isalpha() else district_id
    for line in reps_file:
        info_list_unedited = line.split(",")
        info_list = [info.strip() for info in info_list_unedited]
        district = info_list[district_column]
        district_words = district.split(" ")
        if district_words[-1] == "Large" or district_words[-1] == "Commissioner" or district_words[-1] == "Delegate":
            district_final = (" ".join(district_words)).lower()
        else:
            district_words[-1] = "".join(number for number in district_words[-1] if number.isdigit())
            district_words = [word.lower() if word.isalpha else word for word in district_words]
            district_final = " ".join(district_words)
        if area_lower in district_final and district_id in district_final:
            family_name = info_list[family_name_column]
            given_name = info_list[given_name_column]
            phone = info_list[phone_column]
            print(f"The representative for district/type of representative {district_id} in the state/territory of "
                  f"{area} is {given_name} {family_name}. The phone number is {phone}.")
            break
    else:
        print(f"No representative was found for district/type of representative {district_id} in the state/territory of "
              f"{area}.")
    reps_file.seek(position)




