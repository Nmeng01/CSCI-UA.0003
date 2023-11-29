"""
This script allows the user to make listings for studios and two-bedroom apartments

Submitted by Nicholas Meng, Netid: ndm9914
The script asks the user what type of apartment they are listing, as well as the unit's ID and the rent per month.
Based on the type of apartment, the script will create an object Studio or TwoBedroom and ask more questions
relevant to that specific type of apartment. The objects are saved in a list and once the user makes an empty input
in the 'type-of-apartment' question, the script will print out each object's listing.
"""

from apt_functions import Studio
from apt_functions import TwoBedroom

listings = []
while True:
    # General questions about the apartment
    apartment_type = input("Are you listing a studio or two bedroom apartment? (S/T) ")
    if not apartment_type:
        break
    apartment_id = input("Please input the unit's id: ")
    apartment_rent = int(input("Please input the rent per month: $"))
    if apartment_type.lower() == "s":
        # Specific questions for studio listings
        studio = Studio(apartment_id, apartment_rent)
        studio_square_footage = int(input("What is the studio's square footage? "))
        studio.set_square_footage(studio_square_footage)
        studio_has_kitchen = input("Does the studio have a kitchen? (Y/N) ")
        studio.set_kitchen_status(True if studio_has_kitchen.lower() == "y" else False)
        listings.append(studio)
    if apartment_type.lower() == "t":
        # Specific questions for two-bedroom listings
        two_bedroom = TwoBedroom(apartment_id, apartment_rent)
        room1_square_footage = int(input("What is the first bedroom's square footage? "))
        room2_square_footage = int(input("What is the second bedroom's square footage? "))
        common_area_square_footage = int(input("What is the common area's square footage? "))
        two_bedroom.set_areas([room1_square_footage, room2_square_footage, common_area_square_footage])
        apartment_has_roommate = input("Does the apartment have a roommate? (Y/N) ")
        if apartment_has_roommate.lower() == "y":
            roommate_first_name = input("What is their first name? ")
            roommate_last_name = input("What is their last name? ")
            two_bedroom.set_roommate_info(roommate_last_name, roommate_first_name)
        listings.append(two_bedroom)
    print("Listing saved.\n")
# Displays the listings
print("Here are your listings:\n")
for listing in listings:
    print(listing)
    if listing.get_apartment_type() == "two bedroom apartment" and listing.get_roommate_status():
        print("Note: The price per area uses an effective area to take into account that some areas are shared.")
    print()



