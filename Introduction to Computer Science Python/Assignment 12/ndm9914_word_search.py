def combinations_fixed_size(letters_list):
    """
    Returns combinations of inputted letters with a fixed size for each combination.

    :param:
        letters_list: list of letters

    :return:
        combinations_list: list of unique combinations of the given letters with a fixed length
    """
    combinations_list = []
    # Base case
    if len(letters_list) == 1:
        return [letters_list[0]]

    # Recursive case
    # Loops through each letter in the list
    for letter in letters_list:
        last_letter = letter
        # Makes a copy of letter_list and removes the element to eventually reach the base case
        letters_partial_copy = letters_list.copy()
        letters_partial_copy.remove(letter)
        # Recursive call
        partial_combinations_list = combinations_fixed_size(letters_partial_copy)
        # Adds each letter one at a time to the existing combinations
        combinations_list += [partial + last_letter for partial in partial_combinations_list]
    return combinations_list


def combinations(letters_list):
    """
    Returns combinations of given letters without a fixed length

    :param:
        letters_list: list of letters
    :return:
        set(combinations_list): list of unique combinations of the given letters without a fixed length
    """
    combinations_list = []
    # Base case
    if len(letters_list) == 1:
        return [letters_list[0]]

    # Recursive case
    # Loops through each letter in the list
    for letter in letters_list:
        last_letter = letter
        # Makes a copy of letter_list and removes the element to eventually reach the base case
        letters_partial_copy = letters_list.copy()
        letters_partial_copy.remove(letter)
        # Recursive call
        partial_combinations_list = combinations(letters_partial_copy)
        # Adds each partial combination and the additional partial + last letter combination to the list
        combinations_list += [partial for partial in partial_combinations_list]
        combinations_list += [partial + last_letter for partial in partial_combinations_list]
    return set(combinations_list)


def word_search(letters_list, min_length):
    """
    Returns a list of words that can be used in games like Scrabble, Wordscape, etc.
    :param:
        letters_list: list of letters
        min_length: minimum length that the words need to be

    :return:
        usable_words: list of words accepted by the word search
    """
    # Ensures each letter is uppercase, so it can be read by the dictionary
    letters_list = [letter.upper() for letter in letters_list]
    # Opens and reads the dictionary file into a list
    dict_file = open("Dictionary.txt", "r")
    dict_file.readline()
    valid_words = dict_file.read()
    valid_words_list = set(valid_words.split("\n"))
    # Calls the combinations function to get a list of all possible combinations of the letters
    combinations_list = combinations(letters_list)
    # Finds the possible combinations that are considered words in the dictionary used by this program
    usable_words = valid_words_list & combinations_list
    usable_words = [word for word in usable_words if len(word) >= min_length]
    return usable_words