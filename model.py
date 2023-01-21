from random import choice


def filter_children(list, type):
    filtered_list = []
    for item in list:
        if isinstance(item, type):
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
        not_green_letters = []
        for index, letter in enumerate(other.name):
            if letter != self.name[index]:
                not_green_letters.append(self.name[index])
        for index, letter in enumerate(other.name):
            if letter == self.name[index]:
                list_of_colors.append('green')
            elif letter in self.name and letter in not_green_letters:
                list_of_colors.append('#FFAE20')
                not_green_letters.remove(letter)
            else:
                list_of_colors.append('grey')
        return list_of_colors
