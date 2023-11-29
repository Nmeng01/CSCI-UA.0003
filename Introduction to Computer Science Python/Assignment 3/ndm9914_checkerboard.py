"""
This script makes a checkerboard

Submitted by Nicholas Meng, NetID ndm9914
The user inputs the number of cells and the length of each cell with certain limits.
Then the script iterates over the image adding lines of colors to fill in the square
created by the header function.
"""

import lib.utilities_BMP as bmp
import colors_BMP as colors

filename = "my_other_bitmap.bmp"
picture_file = open(filename,'wb')

while True:
    cell_length = input('What is the length of each cell? Choose an integer between 1 and 200. ') or 50
    if 0 < int(cell_length) < 200:
        cell_length = int(cell_length)
        break
while True:
    cells = input('How many cells per line? Choose a number between 1 and 200. ') or 8
    if 0 < int(cells) < 200:
        cells = int(cells)
        break

image_width = cells*cell_length
if image_width > 2000:
    print('The values inputted are too high. Please try again.')
    exit()
border_thickness = int(image_width / 80)
image_full_width = image_width + 2 * border_thickness

image_binary = bmp.header(image_full_width, image_full_width, colors.bytes_per_pix)
padding = bmp.pad_byte * (-image_full_width * colors.bytes_per_pix % 4)
color1 = colors.brown_pix
color2 = colors.coral_pix
border_color = colors.black_pix

cell1 = color1 * cell_length
cell2 = color2 * cell_length

for border in range(border_thickness):
    image_binary += border_color * image_full_width + padding
for alt in range(cells):
    first_color = color1 if alt%2 == 1 else color2
    second_color = color2 if alt%2 == 1 else color1
    for line in range(cell_length):
        image_binary += border_color * border_thickness
        for pixel in range(cells//2):
            image_binary += first_color * cell_length
            image_binary += second_color * cell_length
        if cells % 2 == 1:
            image_binary += first_color * cell_length + border_color * border_thickness
        else:
            image_binary += border_color * border_thickness
        image_binary += padding
for border in range(border_thickness):
    image_binary += border_color * image_full_width + padding

print(f"The actual file size is {len(image_binary)}.")
print("Make sure the last two numbers coincide. You might be missing", end='')
print(" horizontal lines (big differences) or padding (small differences).")
picture_file.write(image_binary)
picture_file.close()