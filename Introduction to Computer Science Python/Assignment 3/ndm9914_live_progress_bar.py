"""
This script creates a live task bar that updates in real time

Submitted by Nicholas Meng, NetID ndm9914
The user inputs a number of updates and how many times the bar should update.
Then, the script creates a progress bar, filling in a fraction of the updates
over each iteration.
"""

import time
total = int(input("How many numbers should be added? "))
updates = int(input("How many times should the bar update? "))
bar_begin = "Progress |"
bar_end = "| "
complete = " completed."
progress_chr = ">"
not_done_chr = "-"
bar_length = 50

total_sum = 0
total_complete = 0

for num in range(0, total+1):
    if num == int(total_complete):
        percent_decimal = total_complete / total
        percent_complete = f"{percent_decimal:>6.1%}"
        number_progress = int(percent_decimal * bar_length)
        number_not_done = (bar_length - number_progress)
        total_progress = (number_progress * progress_chr) + (number_not_done * not_done_chr)
        print(f"{bar_begin}{total_progress}{bar_end}{percent_complete}{complete}\r", end="")
        time.sleep(3/total)
        total_complete += total/updates
    total_sum += num
else:
    total_sum -= total
    print(f"\nAll done: {total} tasks performed.")
    print(f"The total sum was {total_sum}.")

