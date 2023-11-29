"""
This script returns a file with different foods ordered by energy in descending order and carbs in ascending order.
It also returns the foods with the highest energy and the foods with the lowest carbs.

Submitted by Nicholas Meng, NetID: ndm9914
The script takes the file with Food contents and creates an encompassing dictionary of dictionaries of each food. The
keys in the encompassing dictionary are the names of each food and the values are dictionaries containing nutrition facts
for each food. The script then orders the dictionary according to the highest energy and saves it in a separate file. The
same is done according to the lowest carbs.
"""

import csv
# This forms the encompassing dictionary of food info
filename = input("What is the file for food content in 2019? ")
food_file = open(filename, encoding="latin1")
food_dict_reader = csv.DictReader(food_file)
encompassing_dict = {}
for food in food_dict_reader:
    encompassing_dict[food['Food Name']] = food

# This orders the food according to energy in kcal
ordered_kcal = sorted(encompassing_dict, key=lambda food_name: float(encompassing_dict[food_name]["Energy (kcal)"]),
                      reverse=True)
highest_kcal = float(encompassing_dict[ordered_kcal[0]]["Energy (kcal)"])
highest_kcal_list = []
for possible_highest_kcal_food in ordered_kcal:
    if float(encompassing_dict[possible_highest_kcal_food]["Energy (kcal)"]) == highest_kcal:
        highest_kcal_list.append(possible_highest_kcal_food)
    else:
        highest_kcal_list = " | ".join(highest_kcal_list)
        break
out_kcal_filename = "ndm9914_food_contents_by_energy.csv"
out_kcal_file = open(out_kcal_filename, "w")
for food_kcal in ordered_kcal:
    kcal_row = "\t".join([food_kcal, encompassing_dict[food_kcal]["Energy (kcal)"]])
    out_kcal_file.write(f"{kcal_row}\n")
out_kcal_file.close()
print(f"Food with the highest energy ({highest_kcal} kcal): {highest_kcal_list}")

# This orders the food according to carbs in grams
ordered_carb = sorted(encompassing_dict, key=lambda food_name: float(encompassing_dict[food_name]["Carbohydrate (g)"]))
lowest_carb = float(encompassing_dict[ordered_kcal[0]]["Carbohydrate (g)"])
lowest_carb_list = []
for possible_lowest_carb_food in ordered_carb:
    if float(encompassing_dict[possible_lowest_carb_food]["Carbohydrate (g)"]) == lowest_carb:
        lowest_carb_list.append(possible_lowest_carb_food)
    else:
        lowest_carb_list = " | ".join(lowest_carb_list)
        break
out_carb_filename = "ndm9914_food_contents_by_carbohydrate.csv"
out_carb_file = open(out_carb_filename, "w")
for food_carb in ordered_carb:
    carb_row = "\t".join([food_carb, encompassing_dict[food_carb]["Carbohydrate (g)"]])
    out_carb_file.write(f"{carb_row}\n")
out_carb_file.close()
print(f"Food with the lowest carbs ({lowest_carb} g): {lowest_carb_list}")

