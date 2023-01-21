from random import choice


def filter_children(list, type):
    '''
    The function that leaves only specific data type in list.

    Parameters:
        list (list): List that is filtered.
        type (any): Type of data that must stay in list.

    Returns:
        filtered_list (list): List that cointain only on type of data.
    '''
    filtered_list = []
    for item in list:
        if isinstance(item, type):
            filtered_list.append(item)
    return filtered_list


def draw_password(file_handle):
    '''
    The function that reads from file. It also checks if number of letters
    in each word is correct.

    Parameters:
        file_handle (_io.TextIOWrapper): Indicator on current position in file.

    Returns:
        tuple (Word, list): Word that is randomly chosen from words in file,
            list of all words in file.
    '''
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
    '''
    The class used to catch word with incorrect word lenght.
    '''
    pass


class Word():
    '''
    The class for operations on words.

    Attributes:
        name (str): Name of word assigned to Word object.
    '''
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def compare(self, other):
        '''
        The function that compares two Word objects.

        It analize the similarity of the word inputted by player
        to the game's password Word in accordance with game rules.

        Parameters:
            other (Word): object of the Word class.
        Returns:
            list_of_colors (list): Color for each letter of the second word,
            depending of its presence in first word.
        '''
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
