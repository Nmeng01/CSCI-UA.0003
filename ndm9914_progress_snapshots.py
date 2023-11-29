# Define the initial variables that make up the progress bar
progress_character = '>'
fill_character = '-'
bar_length = 50
percent_completed = 0
# Ask the user to enter the number of tasks to complete and how many have already been completed
total = int(input('How many total tasks? (Choose an integer greater than 0) '))
complete = int(input(f'How many are completed? (Choose an integer between 0 and {total}) '))
print()
# Calculate how much of the progress bar will be made up of the 'progress_character'
bar_complete = int(complete/total * bar_length)
# Show the initial incomplete progress bar
print('Snapshot 1')
print(f'Progress |{fill_character * bar_length}|{percent_completed:8.1f}% completed')
print()
# Make the initial 'percent_completed' variable reflect the percent of tasks that have been completed
percent_completed = (percent_completed + complete)/total * 100
# Show the updated progress bar that reflects the change in the 'percent_completed' variable
print('Snapshot 2')
print(f'Progress |{progress_character * bar_complete}{fill_character * (bar_length - bar_complete)}|'
      f'{percent_completed:8.1f}% completed')
