from random import choice


def get_random_word():
    with open("all_words.txt", "r") as file_handle:
        list_of_words = []
        for line in file_handle:
            list_of_words.append(line)
        word_to_guess = choice(list_of_words)
        return Word(word_to_guess)


class Word():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
