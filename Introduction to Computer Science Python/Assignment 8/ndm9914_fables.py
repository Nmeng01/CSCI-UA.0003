"""
This scripts opens a url from gutenberg.org and allows the user to read a specific fable from this url.

Submitted by Nicholas Meng, NetID: ndm9914
The script opens the url, cleans up the text, and places each line of text in a list. Then, the script parses the
url, finding the positions of each fable in the text. Then, using these positions, the user is asked to select a fable
they want to read and the corresponding fable is displayed.
"""
import urllib.request
import urllib.error
import ssl # library to handle security in IP
url = "http://www.gutenberg.org/cache/epub/28/pg28.txt"
print("Connecting...\r", end="")
# Modifying some settings urllib.request will use.
ctx = ssl.create_default_context()
ctx.check_hostname = False  # Disables hostname checks.
ctx.verify_mode = ssl.CERT_NONE  # Disables certificate checks.
# Opens the URL, handling any kind of network connection errors neatly
file = ""
try:
    file = urllib.request.urlopen(url, context=ctx, )
except urllib.error.URLError:
    print(f"There was an error with your connection. Please try again when you have a better connection.")
    exit()
print(f"File read from {url}")
# Cleans up the text and puts each line of text into a list
file_decoded = (file.read().decode("utf-8")).strip().split("\n")
text_list = [text.strip() for text in file_decoded if text.strip()]
# Finds the table of contents and saves that in a list
contents_index_start = text_list.index("Contents") + 3
contents = []
for line in text_list[contents_index_start:]:
    if line != "PREFACE":
        contents.append(line)
    else:
        break
# The script parses the url, finding the position of each fable
fables_start = text_list.index("Aesop’s Fables")
fables_end = text_list.index("And this is the end of Æsop’s Fables. HURRAH!")
fable_starts_list = []
fable_ends_list = []
for fable_title in contents:
    for fable_line in text_list[fables_start:fables_end]:
        if fable_line == fable_title:
            fable_starts_list.append(text_list.index(fable_line, fables_start, fables_end))
            end_of_fable_index = 0
            for line_within in text_list[fable_starts_list[-1] + 1:fables_end + 1]:
                if line_within in contents:
                    end_of_fable_index = text_list.index(line_within, fables_start, fables_end + 1) - 1
                    fable_ends_list.append(end_of_fable_index)
                    break
                elif line_within == "And this is the end of Æsop’s Fables. HURRAH!":
                    end_of_fable_index = text_list.index(line_within, fables_start, fables_end + 1) - 1
                    fable_ends_list.append(end_of_fable_index)
                    break
            break
fable_indices_list = list(zip(fable_starts_list, fable_ends_list))
# User interaction, handles any errors that the user might cause
while True:
    print('\n' * 2 + '=' * 20 + ' + ' + '=' * 20 + '\n' * 2)
    for num, story in enumerate(contents):
        print(f"{num + 1}) {story}")
    fable = input("Which fable would you like to read next? (1-82) ")
    if not fable:
        break
    print()
    try:
        fable_number = int(fable) - 1
        if fable_number < 0:
            raise IndexError
        for story_line in text_list[fable_indices_list[fable_number][0]:fable_indices_list[fable_number][1] + 1]:
            print(story_line)
    except (IndexError, ValueError):
        print("Please select a number between 1 and 82.")
    continue_function = input("\nPress enter to continue. ")



