class Sentence:
    """
        This class handles sentences and words within a sentence

        Methods
        __init__(self, full_sentence):
            This is the constructor that initializes the Sentence object with a sentence string and breaks
            this sentence string down to just words (No punctuation)
        __str__(self):
            Printing a Sentence object will return the initial sentence string
        __getitem__(self, word_index):
            This returns a specific word in the sentence
        __len__(self):
            This returns the length of the sentence in words
        __iter__(self):
            Allows the code to loop through each word of the sentence
        __next__(self):
            Pushes the iterator to the next word and returns the previous word
        __contains__(self, specific_word):
            This returns True if a specified word is in the sentence and False if not
        def split(self):
            This splits up any sentences with a semicolon into separate two sentences

        Attributes
            new_sentence: This is the sentence string associated with the object
            words_list: This is a list holding all the words in the sentence
            words_list_edited: This is a list holding all the words with the punctuation removed from certain words
            count: This keeps track of the number of iterations the object handles when looping
            sentence_list: This holds a single sentence or two sentences if the particular sentence has a semicolon
        """

    def __init__(self, full_sentence):
        self.new_sentence = full_sentence
        self.words_list = (full_sentence.strip(".?!)(:")).lower().split(" ")
        self.words_list_edited = []
        self.count = 0
        self.sentence_list = []
        for word in self.words_list:
            # Checks if the word contains a non-alphabetic term
            final_word = word
            if not word.isalpha():
                # Removes any preceding non-alphabetic terms
                new_word = word
                for front_letter_index in range(len(word)):
                    if not word[front_letter_index].isalpha():
                        new_word = word[front_letter_index + 1:]
                    else:
                        break
                # Removes any concluding non-alphabetic terms
                final_word = new_word
                for back_letter_index in range(len(new_word) - 1, -1, -1):
                    if not word[back_letter_index].isalpha():
                        final_word = word[0:back_letter_index]
                    else:
                        break
            self.words_list_edited.append(final_word)

    def __str__(self):
        return self.new_sentence

    def __getitem__(self, word_index):
        if abs(word_index) > (len(self.words_list_edited) - 1):
            raise IndexError
        return self.words_list_edited[word_index]

    def __len__(self):
        return len(self.words_list_edited)

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.words_list_edited):
            raise StopIteration
        self.count += 1
        return self.words_list_edited[self.count - 1]

    def __contains__(self, specific_word):
        if specific_word.lower() in self.words_list_edited:
            return True
        else:
            return False

    def split(self):
        if ";" in self.new_sentence:
            for sentence_string in self.new_sentence.split(";"):
                sentence_string = sentence_string.strip().capitalize()
                if sentence_string[-1] not in ".!?":
                    sentence_string = sentence_string + "."
                self.sentence_list.append(Sentence(sentence_string))
            return self.sentence_list
        else:
            return [self]




