from random import choice


def create_link(game):
    ye = "\U0001F7E8"
    gr = "\U0001F7E9"
    bl = "\U0001F7EB"
    row = game.current_row
    attempt = f"{'X' if not game.game_won else str(row)}"
    colors = game.color_history.format(green=gr, yellow=ye, grey=bl)
    link = f"logos'le {attempt}/6\n{colors}"
    return link


def filter_children(list, type):
    filtered_list = []
    for item in list:
        if isinstance(item, type):
            filtered_list.append(item)
    return filtered_list


def draw_password(file_handle):
    list_of_words = []
    for line in file_handle:
        word = line[:-1]
        if len(word) == 5:
            list_of_words.append(word)
        else:
            raise IncorrectWordLengthError("Word has to 5 letters long")
    word_to_guess = choice(list_of_words)
    return (Word(word_to_guess), list_of_words)


class IncorrectWordLengthError(Exception):
    pass


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
