"""
This script returns a list of car equipment ids based on their numeric value in ascending order
and based on the year they were made in descending order.

Submitted by Nicholas Meng, NetID: ndm9914
The script finds the column in the file inputted which has the years listed and assumes that the equipment ids are in the
first column. Then, the script creates a dictionary with the keys being the car equipment ids and the values being the
year.The dictionary is then sorted based on their numeric value ascending and the year in descending order. The info is
saved in separate files.
"""

import csv

# Parses the file and puts the necessary info in a dictionary.
filename = input("What is the file for car equipment? ")
car_equipment_file = open(filename)
labels = car_equipment_file.readline()
labels_list_unedited = (labels.strip()).split(",")
labels_list = [label.strip().lower() for label in labels_list_unedited]
car_equipment_reader = csv.reader(car_equipment_file, quotechar="'")
year_column = -1
for label in labels_list:
    if "year" in label:
        year_column = labels_list.index(label)
        break
car_dict = {}
for car in car_equipment_reader:
    # The ternary operator ensures that the car ids can be sorted by making all data in the dictionary an integer
    car_dict[int(car[0])] = int(car[year_column]) if car[year_column].isnumeric() and len(car[year_column]) == 4 else 0

# Orders the dictionary based on the numeric value of the ids and saves it in a separate file
ordered_id = sorted(car_dict.keys())
out_filename_ids = "ndm9914_output_sorted_by_id.csv"
out_id_file = open(out_filename_ids, "w", newline="")
sorted_ids_writer = csv.writer(out_id_file)
sorted_ids_writer.writerow([labels_list[0], labels_list[year_column]])
for car in ordered_id:
    # The ternary operator here changes all values that were changed to 0 to NULL which denotes that the year was
    # unknown or otherwise took a value that was not a year.
    sorted_ids_writer.writerow([car, car_dict[car] if car_dict[car] != 0 else "NULL"])
out_id_file.close()

# Orders the dictionary based on the year and saves it in a separate file
ordered_year = sorted(car_dict, key=lambda car_id: car_dict[car_id], reverse=True)
out_filename_ids_by_year = "ndm9914_output_sorted_by_year.csv"
out_ids_by_year_file = open(out_filename_ids_by_year, "w", newline="")
sorted_ids_by_years_writer = csv.writer(out_ids_by_year_file)
sorted_ids_by_years_writer.writerow([labels_list[0], labels_list[year_column]])
for car in ordered_year:
    # The ternary operator here changes all values that were changed to 0 to NULL which denotes that the year was
    # unknown or otherwise took a value that was not a year.
    sorted_ids_by_years_writer.writerow([car, car_dict[car] if car_dict[car] != 0 else "NULL"])
out_ids_by_year_file.close()
