from PySide2.QtWidgets import QMainWindow, QApplication
import sys
from ui_wordle import Ui_MainWindow
from classes import Word
from random import choice


def draw_password():
    with open("all.words.txt", "r") as file_handle:
        list_of_words = []
        for line in file_handle:
            line = line[:-1]
            list_of_words.append(line)
        word_to_guess = choice(list_of_words)
        return (Word(word_to_guess), list_of_words)


class WordleWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setupKeyboard()
        self.current_column = 1
        self.current_row = 1
        self.all_labels = self.dict_all_labels()
        self.password, self.all_words = draw_password()

    def _input_letter_by_button(self, button):
        if button.text() == "Backspace":
            self.delete_letter()
        elif button.text() == "Enter":
            if self.current_column == 6:
                self.check_guess()
            else:
                # Błąd, że musi być 5 liter wpisanych
                pass
        elif self.current_column == 6:
            pass
        else:
            row = self.current_row
            column = self.current_column
            self.all_labels[row][column].setText(button.text())
            self.current_column += 1

    def _setupKeyboard(self):
        self.ui.all_buttons.buttonClicked.connect(self._input_letter_by_button)

    def delete_letter(self):
        if self.current_column > 1:
            self.current_column -= 1
            row = self.current_row
            column = self.current_column
            self.all_labels[row][column].setText('')
        else:
            pass

    def dict_all_labels(self):
        labels_listed = self.ui.Windows.children()
        labels_listed.sort(key=lambda x: x.objectName())
        labels_in_dict = {row: {column: labels_listed[(row-1)*5+(column-1)]
                          for column in range(1, 6)}
                          for row in range(1, 7)}
        return labels_in_dict

    def check_guess(self):
        letters = ''
        for label in self.all_labels[self.current_row].values():
            letters += label.text().lower()
        if letters in self.all_words:
            written_word = Word(letters)
            row = self.current_row
            wht = "color: white"
            border = "border: 2px solid black"
            colors = self.password.compare(written_word)
            for index, color in enumerate(colors):

                self.all_labels[row][index+1].setStyleSheet(
                    f"background-color: {color}; {border}; {wht};")
                button_name = 2*letters[index]
                for button in self.ui.Keyboard.children():
                    if button.objectName() == button_name:
                        button.setStyleSheet(
                            f"background-color: {color}; {wht};")

            self.current_row += 1
            if self.current_row > 6:
                self.game_lost()
            self.current_column = 1
        else:
            # błąd, że nie ma takiego hasła w bazie
            pass

    def game_lost(self):
        # jak w nazwie
        pass


def guiMain(args):
    app = QApplication(args)
    window = WordleWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
