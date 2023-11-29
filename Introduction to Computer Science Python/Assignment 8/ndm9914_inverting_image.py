"""
This script takes a bmp image and flips it upside down.

Submitted by Nicholas Meng, NetID: ndm9914
The script asks for a file, and if the file is not found, the script will keep asking for a file. Then, the script reads
the header and gathers certain important information about the file and prints it out. After that, the script reads
through the whole file, saving each individual pixel in a 2d list. The script then reverses this table horizontally and
vertically, writing out the upside down version of the original image.
"""


def retrieve_int(file_handle, num_bytes):
    """ Converts bytes read from a file into an int
    :param file_handle: file
    :param num_bytes: number of bytes to be read
    :return: an integer representation of the bytes
    This function affects the file as it moves the pointer.
    It handles the binary data as representing numbers
    specified as Little Endian.
    """
    num_bytes = bytearray(file_handle.read(num_bytes))
    # Data in bmp files is in Little Endian format
    num_bytes.reverse()
    num_int = 0
    for byte in num_bytes:
        num_int = num_int * 256 + byte
    return num_int


# Ensures the file exists in the directory before proceeding
while True:
    try:
        filename = input("Please input the file with the image you want to tweak: ")
        image_file = open(filename, 'br')
    except FileNotFoundError:
        print("File not found! Please try again.\n")
    else:
        break

# Reads the header and records certain important info
description = image_file.read(2)
file_size = retrieve_int(image_file, 4)
image_file.seek(10)
offset = retrieve_int(image_file, 4)
header_size = retrieve_int(image_file, 4)
image_width = retrieve_int(image_file, 4)
image_height = retrieve_int(image_file, 4)
planes = retrieve_int(image_file, 2)
bits_per_pixel = retrieve_int(image_file, 2)
bytes_per_pixel = bits_per_pixel//8
padding_length = (-bytes_per_pixel * image_width % 4)

# Prints out all the important info for the user to see
print(description)
print(f"File size: {file_size} bytes")
print(f"The offset is {offset} bytes")
print(f"The image is {image_width} (w) x {image_height} (h)")
print(f"The header size is {header_size}")
print(f"Planes: {planes}")
print(f"It uses {bits_per_pixel} bits per pixel")
print(f"Padding: {padding_length}")
# Positions the file pointer at the beginning of the data section of the bmp image
image_file.seek(0)
header = image_file.read(offset)
# Iterates through and saves all the pixels in the image
pixel_table = []
for line in range(image_height):
    row_pixels = []
    for pixel in range(image_width):
        row_pixels.append(image_file.read(bytes_per_pixel))
    image_file.read(padding_length)
    pixel_table.append(row_pixels)
# Creates the new file, taking the old filename and adding 'inverted' to it
out_file_split = filename.split(".")
*out_filename, extension = out_file_split
out_filename[-1] = out_filename[-1] + " inverted"
out_file = ".".join(out_filename) + "." + extension
inverted_image = open(out_file, "wb")
# Reverses 'pixel_table' and writes each pixel out, producing the original image upside down
inverted_image.write(header)
reversed_pixel_table = pixel_table[::-1]
for row in reversed_pixel_table:
    row = row[::-1]
    for image_byte in row:
        inverted_image.write(image_byte)
    if padding_length != 0:
        for padding_byte in range(padding_length):
            inverted_image.write(b'\x00')
inverted_image.close()







