from PySide2.QtWidgets import QLabel
from random import choice


def clear_from_nonlabels(list):
    filtered_list = []
    for item in list:
        if isinstance(item, QLabel):
            filtered_list.append(item)
    return filtered_list


def draw_password():
    with open("all.words.txt", "r") as file_handle:
        list_of_words = []
        for line in file_handle:
            line = line[:-1]
            list_of_words.append(line)
        word_to_guess = choice(list_of_words)
        return (Word(word_to_guess), list_of_words)


class Word():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def compare(self, other):
        list_of_colors = []
        for index, letter in enumerate(other.name):
            if letter == self.name[index]:
                list_of_colors.append('green')
            elif letter in self.name:
                list_of_colors.append('#FFAE20')
            else:
                list_of_colors.append('grey')
        return list_of_colors
