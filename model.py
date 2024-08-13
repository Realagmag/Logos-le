from random import choice


def filter_children(list, type):
    '''
    Get all elements from the list of given type.

    Parameters:
        list (list): List that is filtered.
        type (any): Type of data that must stay in list.

    Returns:
        filtered_list (list): List that cointains only given type of data.
    '''
    filtered_list = []
    for item in list:
        if isinstance(item, type):
            filtered_list.append(item)
    return filtered_list


def draw_password(file_handle):
    '''
    Load words from file and chose game's password.

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
            raise IncorrectWordLengthError(
                f"Word has to 5 letters long, but {word} has {len(word)}")
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
        Check what letters are placed correctly and set
        corresponding color.

        Parameters:
            other (Word): Word to compare with.
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
