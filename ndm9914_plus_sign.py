"""This program makes a BMP file with a plus sign of a specified color"""


import utilities_BMP as bmp
import colors_BMP as colors

filename = "my_other_bitmap.bmp"
picture_file = open(filename,'wb')

# ToDo: put the corresponding sizes below according to the instructions
# in the assignment
plus_thickness = int(input('How thick will the plus sign be? '))  # Thickness for the lines in the actual plus sign
# Size information for the image
image_width = int(input('What is the width? '))  # Total width for the image
image_height = int(input('What is the length? '))  # Total height for the image


# Header with information about the size of the file.
image_binary = bmp.header(image_width, image_height, colors.bytes_per_pix)

# ToDo: write the code to fill the data section in the space below
# Pixel by pixel color information starting from the bottom up and left
# to right. All rows are padded to a multiple of 4. For each pixel,
# colors are specified as follows: Blue channel, Green channel & then
# Red channel.
# The number of bytes in each line has to a multiple of 4. For padding,
# a special pad_byte is used. See the other template for the padding
# code.

# This lines creates the padding that allows for integer inputs that are not multiples of 4
padding = bmp.pad_byte * (-image_width * colors.bytes_per_pix % 4)

# These variables establish the colors of the image
main_color = colors.dim_grey_pix
plus_color = colors.steel_blue_pix

# The next four variables provide for better readability in the main body code
# These variables establish half of the width and height of just the areas that are 'main_color'
width_main_half = (image_width - plus_thickness)
height_main_half = (image_height - plus_thickness)

# These variables establish a quarter of the width and height of just the areas that are 'main_color'
width_main_quadrant = width_main_half // 2
height_main_quadrant = height_main_half // 2

# This variable establishes the building piece of all the 'main_color' areas and the vertical part of the plus
horizontal_line1 = (main_color * width_main_quadrant + plus_color * plus_thickness +
                    main_color * (width_main_half - width_main_quadrant) + padding)

# This variable establishes the building piece of the horizontal part of the plus
horizontal_line2 = ((plus_color * image_width) + padding)

# This is the main body which stacks the horizontal lines vertically to create a shape
image_binary = image_binary + horizontal_line1 * height_main_quadrant + horizontal_line2 * plus_thickness \
               + horizontal_line1 * (height_main_half - height_main_quadrant)



# Do not edit after this point
print(f"The actual file size is {len(image_binary)}.")
print("Make sure the last two numbers coincide. You might be missing", end='')
print(" horizontal lines (big differences) or padding (small differences).")
picture_file.write(image_binary)
picture_file.close()