"""
Defines some classes for a future apartment search app

Submitted by Nicholas Meng, NetID: ndm9914
The script defines a parent class Apartment and then defines two child classes called Studio and TwoBedroom.
Studio: A single room with a kitchen/kitchenette
Two-Bedroom: An apartment with 2 bedrooms and a common room, and it sometimes comes with a roommate
"""


class Apartment:
    """
    This class sets up a generic apartment object with certain important info related to any type of unit

    Methods
            __init__(self, unit_id, rent):
                This is the constructor that initializes the Apartment object with a unique ID and monthly rent
            set_square_footage(self, area):
                Sets the square footage of the apartment
            get_square_footage(self):
                This returns the square footage of the apartment
            get_rent_per_square_foot(self):
                This returns the rent/square footage
            get_target_wages(self):
                This returns the wages a renter should be making to rent the apartment
            get_apartment_type(self):
                This returns the type of apartment the object is
            __str__(self):
                Sets the general format when printing the object

            Attributes
                apt_id: The unique ID associated with the apartment
                apt_rent: The monthly rent associated with the apartment
                square_footage: The square footage of the apartment
                type_apartment: Sets the type of apartment to 'apartment'
    """
    def __init__(self, unit_id, rent):
        """Initializes general info related to the apartment"""
        self.apt_id = unit_id
        self.apt_rent = rent
        self.square_footage = 0
        self.type_apartment = "apartment"

    def set_square_footage(self, area):
        """Sets the square footage"""
        self.square_footage = area

    def get_square_footage(self):
        """Returns the square footage"""
        return self.square_footage

    def get_rent_per_square_foot(self):
        """Returns the monthly rent per square foot"""
        if self.square_footage == 0:
            raise ValueError("Area not defined")
        else:
            return self.apt_rent/self.square_footage

    def get_target_wages(self):
        """Returns the target wage of a potential renter"""
        return self.apt_rent*12/0.4

    def get_apartment_type(self):
        """Returns the type of apartment"""
        return self.type_apartment

    def __str__(self):
        """Sets what is printed when the Apartment object is printed"""
        return (f"This {self.type_apartment} has a rent of ${self.apt_rent} per month. \nIt has a square footage of "
                f"{self.square_footage} square feet, which means that the price per square foot is "
                f"${self.get_rent_per_square_foot():.2f} per square foot.\nIts ID is {self.apt_id} and the wage "
                f"you should be earning to rent this place is ${self.get_target_wages():.2f}. ")


class Studio(Apartment):
    """
    This class sets up a specific type of Apartment called Studio

    Methods
        __init__(self, studio_id, studio_rent, kitchen=True):
            Inherited from the Apartment class's constructor, adding an initialization for the kitchen status
        set_square_footage(self, area):
            Inherited from the Apartment class
        get_square_footage(self):
            Inherited from the Apartment class
        get_rent_per_square_foot(self):
            Inherited from the Apartment class
        get_target_wages(self):
            Inherited from the Apartment class
        get_apartment_type(self):
            Inherited from the Apartment class
        set_kitchen_status(self, status: bool):
            Sets the status of the kitchen
        get_kitchen_status(self):
            Returns whether the studio has a kitchen or not
        __str__(self):
            Inherited from the Apartment class's str method, adding the kitchen status to the format

    Attributes
        self.apt_id: Inherited from the Apartment class
        self.apt_rent: Inherited from the Apartment class
        self.square_footage: Inherited from the Apartment class
        self.type_apartment: Sets the type of apartment to 'studio'
        self.has_kitchen: Indicates whether the studio has a kitchen or not
    """
    def __init__(self, studio_id, studio_rent, kitchen=True):
        """Initializes the general info related to the studio"""
        super().__init__(studio_id, studio_rent)
        self.type_apartment = "studio"
        self.has_kitchen = kitchen

    def set_kitchen_status(self, status: bool):
        """Sets whether there is a kitchen or not"""
        self.has_kitchen = status

    def get_kitchen_status(self):
        """Returns whether there is a kitchen or not"""
        return self.has_kitchen

    def __str__(self):
        """Sets what is printed when the Studio object is printed"""
        return (super().__str__() +
                f"The studio comes with a {'kitchen' if self.get_kitchen_status() else 'kitchenette'}.")


class TwoBedroom(Apartment):
    """
    This class sets up a specific type of Apartment called TwoBedroom

    Methods
        __init__(self, two_bedroom_id, two_bedroom_rent, roommate=False):
            Inherited from the Apartment class's constructor, adding an initialization for the roommate status,
            the roommate's first and last name, and the area of each room in the apartment
        set_areas(self, areas_list: list):
            Sets the areas of each room in the apartment
        set_square_footage(self, area):
            Inherited from the Apartment class, but it sets the total square footage by adding all the room areas
            if each room's area has been set already
        get_square_footage(self):
            Inherited from the Apartment class
        set_roommate_status(self, status: bool):
            Sets whether the apartment comes with a roommate
        get_roommate_status(self):
            Returns whether the apartment comes with a roommate
        set_roommate_info(self, family_name, given_name):
            Sets the first and last name of the roommate
        get_rent_per_square_foot(self):
            Inherited from the Apartment class, but it returns double the cost per square foot if there is a roommate
        __str__(self):
            Inherited from the Apartment class's str method, adding the roommate status and info to the format

    Attributes:
        self.apt_id: Inherited from the Apartment class
        self.apt_rent: Inherited from the Apartment class
        self.square_footage: Inherited from the Apartment class
        self.type_apartment: Sets the type of apartment to 'two bedroom apartment'
        self.has_roommate: The status of the roommate
        self.room_areas: Contains the area of each room
        self.roommate_last_name: The roommate's last name
        self.roommate_first_name: The roommate's first name
    """
    def __init__(self, two_bedroom_id, two_bedroom_rent, roommate=False):
        """Initializes the general info related to the two-bedroom apartment"""
        super().__init__(two_bedroom_id, two_bedroom_rent)
        self.type_apartment = "two bedroom apartment"
        self.has_roommate = roommate
        self.room_areas = {"Room 1": 0, "Room 2": 0, "Common Area": 0}
        self.roommate_last_name = ""
        self.roommate_first_name = ""

    def set_areas(self, areas_list: list):
        """Sets the area of each room"""
        self.room_areas = dict(zip(self.room_areas.keys(), areas_list))
        for area in areas_list:
            self.square_footage += area
        if self.room_areas["Common Area"] < (0.2*self.square_footage):
            raise ValueError(f"Common area is too small: {self.room_areas}")

    def set_square_footage(self, area):
        """Sets the total square footage of the two-bedroom apartment"""
        self.square_footage = area
        if self.room_areas["Common Area"] and self.room_areas["Room 1"] and self.room_areas["Room 2"]:
            if self.square_footage - (self.room_areas["Room 1"] + self.room_areas["Room 2"]) < (0.2 * self.square_footage):
                raise ValueError(f"Common area is too small: {self.room_areas}")
            else:
                self.room_areas["Common Area"] = area - (self.room_areas["Room 1"] + self.room_areas["Room 2"])

    def set_roommate_status(self, status: bool):
        """Sets whether there is a roommate or not"""
        self.has_roommate = status

    def get_roommate_status(self):
        """Returns whether there is a roommate or not"""
        return self.has_roommate

    def set_roommate_info(self, family_name, given_name):
        """Sets the first and last name of the roommate"""
        self.has_roommate = True
        self.roommate_last_name = family_name
        self.roommate_first_name = given_name

    def get_rent_per_square_foot(self):
        """Returns the rent per square foot"""
        if self.square_footage == 0:
            raise ValueError("Area not defined.")
        if self.has_roommate:
            return self.apt_rent/(self.room_areas["Room 2"] + (self.room_areas["Common Area"]/2))
        else:
            return self.apt_rent/self.square_footage

    def __str__(self):
        """Sets what is printed when the TwoBedroom object is printed"""
        return (super().__str__() +
                f"This apartment comes with a roommate named {self.roommate_first_name} {self.roommate_last_name}."
                if self.has_roommate else super().__str__() + '\nThis apartment does not come with a roommate.')



