"""
This script takes a string and returns it with each word summarized

Submitted by Nicholas Meng, NetID: ndm9914
The script takes the string and splits it into individual words. Then, the script iterates over each word, stripping
each word of any punctuation it may have before determining the summarized form (first letter + the number of letters
between the first and last letter + last letter). Once the word is stripped down to only alphabetic terms, the script
then summarizes the word accordingly and returns the full string in summarized form.
"""
# Asks the user for a string
original_string = input("Provide an input string: ")
# Splits the string into a list, so we can iterate over each word. Does not remove punctuation yet.
words_list = original_string.split(" ")
words_summarized_list = []
for word in words_list:
    front_punc = ""
    back_punc = ""
    # Checks if the word contains a non-alphabetic term
    if not word.isalpha():
        # Removes any preceding non-alphabetic terms
        for front_letter_index in range(len(word)):
            if not word[front_letter_index].isalpha():
                front_punc += word[front_letter_index]
                word = word[front_letter_index + 1:]
            else:
                break
        # Removes any concluding non-alphabetic terms
        for back_letter_index in range(len(word)-1, -1, -1):
            if not word[back_letter_index].isalpha():
                back_punc += word[back_letter_index]
                word = word[0:back_letter_index]
            else:
                break
    # Puts each word into summarized form and places the punctuation back accordingly
    if len(word) > 2:
        first, *middle, last = word
        middle = str(len(middle))
        summarized_word = front_punc + first + middle + last + back_punc
        words_summarized_list.append(summarized_word)
    else:
        word = front_punc + word + back_punc
        words_summarized_list.append(word)
summarized_sentence = " ".join(words_summarized_list)
print(summarized_sentence)
