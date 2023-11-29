"""
This script allows the user to look up house reps in a specific file

Submitted by Nicholas Meng, NetID: ndm9914
The script reads through a file and places all its information into a dictionary using
two objects ('Seat' and 'Person') to organize the information. The user inputs a state/territory
they're interested in and the district id of the representative they are looking up, and the script returns
that specific representative along with other important information.
"""
import csv


class Seat:
    """
    This class handles information regarding a representative's position separate from their identity

    Methods
    __init__(self, state, district):
        This is the constructor that initializes state and district info
    __str__(self):
        Whenever this object is printed, this method ensures that it is printed in a clear, concise way
    phone_set(self, phone):
        This sets the seat's phone number
    office_set(self, office):
        This sets the seat's office
    phone_get(self, phone):
        This retrieves the seat's phone number
    office_get(self, office):
        This retrieves the seat's office info
    person_set(self, representative):
        This sets the current representative holding the seat associated with the state and district in the constructor
    seat_full_name_get(self):
        This retrieves the current representative's full name

    Attributes
        state_name: This is the state associated with this seat
        district_id: This is the district number associated with this seat. The district can also be 'At Large'
        phone_number: This is the phone number associated with this seat
        office_number: This is the office associated with this seat
        rep: This is the representative currently associated this seat
    """
    def __init__(self, state, district):
        self.state_name = state
        self.district_id = district
        self.phone_number = ""
        self.office_number = ""
        self.rep = None

    def __str__(self):
        return (f"Seat for district {self.district_id} in the state of {self.state_name}:\n"
                f"Phone number: {self.phone_number}.\n"
                f"Office: {self.office_number}\n"
                f"Representative: {self.seat_full_name_get()}"
                if self.district_id.isnumeric()
                else f"{self.district_id.capitalize()} seat for the state of {self.state_name}:\n"
                     f"Phone number: {self.phone_number}.\n"
                     f"Office: {self.office_number}\n"
                     f"Representative: {self.seat_full_name_get()}")

    def phone_set(self, phone):
        self.phone_number = phone

    def office_set(self, office):
        self.office_number = office

    def phone_get(self):
        return self.phone_number

    def office_get(self):
        return self.office_number

    def person_set(self, rep):
        self.rep = rep

    def seat_full_name_get(self):
        return self.rep.full_name_get()


class Person:
    """
    This class handles information regarding a representative's identity

    Methods
    __init__(self, given_name, family_name)
        This is the constructor that initializes the rep's first and last name
    __str__(self)
        Whenever this object is printed, this method ensures that it is printed in a clear, concise way
    first_name_get(self)
        This retrieves the rep's first name
    last_name_get(self)
        This retrieves the rep's last name
    full_name_get(self)
        This retrieves the rep's full name
    party_set(self, party_letter)
        This sets the rep's party affiliation
    party_get(self)
        This retrieves the rep's party affiliation

    Attributes
        first_name: This is the rep's first name
        last_name: This is the rep's last name
        party: This is the rep's party affiliation
    """
    def __init__(self, given_name, family_name):
        self.first_name = given_name
        self.last_name = family_name
        self.party = ""

    def __str__(self):
        return f"Representative: {self.full_name_get()} {self.party_get()}"

    def first_name_get(self):
        return self.first_name

    def last_name_get(self):
        return self.last_name

    def full_name_get(self):
        return f"{self.first_name} {self.last_name}"

    def party_set(self, party_letter):
        self.party = "(" + party_letter + ")" if party_letter.isalpha() else ""

    def party_get(self):
        return self.party


# Main
while True:
    dir_filename = input("Which file contains the information about the "
                         "representatives? (Enter to exit.) ")
    if not dir_filename:
        exit()
    try:
        directory = open(dir_filename, "r", encoding="latin-1")
    except FileNotFoundError:
        print(f"The file {dir_filename} could not be open.\n\n\n")
    else:
        break

# Places the file's text in a dictionary and establishes the labels
house_seats = csv.DictReader(directory)
state_label = "State or Territory"
district_label = "District or Representation Type"
phone_label = "Phone "
office_label = "Office Room "
given_name_label = "Given name"
family_name_label = "Family name"
party_label = "Party "

# Places corresponding information into the two objects 'Seat' and 'Person' and creates a dictionary with them
encompassing_dict = {}
for row in house_seats:
    if row[district_label] == "At Large" or row[district_label].isnumeric():
        row = {label: info.strip() for (label, info) in row.items()}
        new_seat = Seat(row[state_label], row[district_label].lower())
        new_seat.phone_set(row[phone_label])
        new_seat.office_set(row[office_label])
        new_person = Person(row[given_name_label], row[family_name_label])
        new_person.party_set(row[party_label])
        new_seat.person_set(new_person)
        encompassing_dict_key = (new_seat.state_name, new_seat.district_id)
        encompassing_dict[encompassing_dict_key] = new_seat
# User interaction
while True:
    area = input("For which state/territory would you like information? ")
    if not area:
        break
    area = area.lower().strip()
    district_id = input("Please provide the district number/type of representative: ")
    if not district_id:
        break
    district_id = district_id.strip()
    query = (area, district_id)
    print()
    for state_key, info in encompassing_dict.items():
        if query[0] == state_key[0].lower() and \
                (state_key[1].lower() if state_key[1].isalpha else state_key[1]) == query[1]:
            print(info)
            print()
            break
    else:
        print("No representative was found. Please try again.")
