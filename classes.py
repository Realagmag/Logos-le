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
