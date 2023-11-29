"""
This script takes a text file containing the Don Quixote novel and produces a summary of the first chapter

Submitted by Nicholas Meng, NetID: ndm9914
The script opens the url and finds chapter 1 by using distinct markers within the text. The script then places
each paragraph of the chapter into a list of Paragraph objects. Using this list, the script finds certain
relevant information to the first chapter and prints out a summary of each paragraph.
"""

from ndm9914_paragraphs import Paragraph
import urllib.request
import urllib.error
import ssl
# Opens the URL, handling connection errors
url = "https://www.gutenberg.org/cache/epub/996/pg996.txt"
ctx = ssl.create_default_context()
ctx.check_hostname = False  # Disables hostname checks.
ctx.verify_mode = ssl.CERT_NONE  # Disables certificate checks.
file = ""
print("This will take a moment...")
try:
    file = urllib.request.urlopen(url, context=ctx)
except urllib.error.URLError:
    print(f"There was an error with your connection. Please try again when you have a better connection.")
    exit()
print(f"Reading file from {url}...")
file_decoded = (file.read().decode("utf-8")).strip().split("\n")
text_list = [text.strip() for text in file_decoded]
print()
# Finds chapter 1 and places the individual paragraphs in a list of Paragraph objects
beginning_marker = text_list.index("p007.jpg (150K)") + 4
ending_marker = text_list.index("p007b.jpg (61K)") - 2
chapter_text_list = text_list[beginning_marker: ending_marker]
chapter_text_list_edited = []
for line in chapter_text_list:
    for char in ["_", "\u201c", "\u201d"]:
        line = line.replace(char, "")
    line = line.replace("\u2014", " ")
    chapter_text_list_edited.append(line)
chapter_text_string = "\n".join(chapter_text_list_edited)
beginning_index = 0
paragraphs_list = []
for text_line in chapter_text_list_edited:
    if not text_line:
        end_index = chapter_text_list_edited.index(text_line, beginning_index)
        paragraph = Paragraph(" ".join(chapter_text_list_edited[beginning_index:end_index + 1]))
        paragraphs_list.append(paragraph)
        beginning_index = end_index + 1

sentence_count = 0
word_count = 0
he_count = 0
mancha_count = 0
for para in paragraphs_list:
    sentence_count += len(para)
    for sentence in para.sentences_list:
        word_count += len(sentence)
        if "he" in sentence:
            he_count += 1
        if "mancha" in sentence:
            mancha_count += 1
print(f"The total number of paragraphs: {len(paragraphs_list)}")
print(f"The total number of sentences: {sentence_count}")
print(f"The total number of words: {word_count}")
print(f"The average number of words per sentence: {(word_count/sentence_count):.2f}")
print(f"The average number of sentences per paragraph: {(sentence_count/len(paragraphs_list)):.2f}")
print(f"The number of times the word 'he' appears: {he_count}")
print(f"The number of times the word 'mancha' appears: {mancha_count}")

print("\nA summary of the chapter:\n")
for para_num, new_para in enumerate(paragraphs_list):
    for new_sentence in new_para.sentences_list:
        if new_sentence == new_para.sentences_list[0]:
            print(new_sentence)
            print(f"Paragraph {para_num + 1}: {len(new_para)} hidden sentences.")
        if new_sentence == new_para.sentences_list[-1]:
            print(new_sentence)
            print()