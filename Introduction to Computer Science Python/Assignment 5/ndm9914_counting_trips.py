"""
This script takes two dates and returns a list of the number of deliveries
made in each hour on these dates.

Submitted by Nicholas Meng, NetID ndm9914
The user inputs the two files and the specific day they want to examine.
Then, the script iterates through each file, tallying each delivery made on the
specific date that user wants. After the results have been compiled, the script asks
the user for a filename to save the results under.
"""
day_input = input("What day of the month are you interested in? ")
first_file = input("Enter the name of the first file with fhv data: ")
second_file = input("Enter the name of the first file with fhv data: ")
file1 = open(first_file, encoding='windows-1252')
file2 = open(second_file, encoding='windows-1252')
labels1 = file1.readline()
labels2 = file2.readline()

trip_list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
trip_list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]
list_of_counts = [trip_list1, trip_list2]
list_of_files = [file1, file2]
labels_out_file = ["Hour"]
print("Tallying results...")

for file_num in range(len(list_of_files)):
    trips_file = list_of_files[file_num]
    counts_by_hour = list_of_counts[file_num]
    for line in trips_file:
        line_list = line.split(",")
        date, time = line_list[1].split(" ")
        year, month, day = date.split("-")
        if day[0] == "0":
            day = day[1]
        if month[0] == "0":
            month = month[1]
        hour = time[0:2]
        if hour[0] == "0":
            hour = hour[1]
        hour = int(hour)
        if day == day_input:
            counts_by_hour[hour] += 1
    month = int(month)
    labels_out_file.append(f"{months_list[month-1]} {day_input} {year}")
print("Results tallied.")

out_filename = input("Enter the file name to store the output. (output.csv is the default): ")
if not out_filename:
    out_filename = "output.csv"
if out_filename[-3:] != "csv":
    out_filename += ".csv"
out_file = open(out_filename, "wt")
labels_out_file = ",".join(labels_out_file)
out_file.write(labels_out_file + "\n")
for hour_label in range(len(trip_list1)):
    comparison_list = [str(hour_label), str(trip_list1[hour_label]), str(trip_list2[hour_label])]
    comparison_line = ",".join(comparison_list)
    out_file.write(comparison_line + "\n")
print("Results saved.")





