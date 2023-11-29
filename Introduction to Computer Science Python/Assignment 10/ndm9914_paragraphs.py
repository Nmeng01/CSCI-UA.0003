from ndm9914_sentences import Sentence


class Paragraph:
    """
            This class handles paragraphs and sentences within a paragraph

            Methods
            __init__(self, full_paragraph):
                This is the constructor that initializes the Paragraph object with a paragraph string and breaks
                this paragraph string down to just sentences (No punctuation)
            __str__(self):
                Printing a Paragraph object will return the initial paragraph string
            __getitem__(self, sentence_index):
                This returns a specific sentence in the paragraph
            __len__(self):
                This returns the length of the paragraph in sentences
            __iter__(self):
                Allows the code to loop through each sentence of the paragraph
            __next__(self):
                Pushes the iterator to the next sentence and returns the previous sentence

            Attributes
                new_paragraph: This is the paragraph string associated with the object
                sentences_list: This is a list holding all the sentences in the paragraph
                count: This keeps track of the number of iterations the object handles when looping
            """

    def __init__(self, full_paragraph):
        self.new_paragraph = full_paragraph
        self.sentences_list = []
        self.count = 0
        beginning_index = 0
        for letter in full_paragraph:
            if letter in "?!.":
                end_index = full_paragraph.index(letter, beginning_index)
                sentence = Sentence(full_paragraph[beginning_index:end_index + 1])
                colon_check_sentence = sentence.split()
                for colon_sentence in colon_check_sentence:
                    self.sentences_list.append(colon_sentence)
                beginning_index = end_index + 2

    def __str__(self):
        return self.new_paragraph

    def __getitem__(self, sentence_index):
        if abs(sentence_index) > (len(self.sentences_list) - 1):
            return None
        return self.sentences_list[sentence_index]

    def __len__(self):
        return len(self.sentences_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.sentences_list):
            raise StopIteration
        self.count += 1
        return self.sentences_list[self.count - 1]




