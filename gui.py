from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QLabel
from PySide2.QtWidgets import QPushButton
import sys
from ui_wordle import Ui_MainWindow
from ui_how_to_play import Ui_how_to_play
from ui_theme import Ui_theme
from model import Word, draw_password, filter_children


class How_to_play(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_how_to_play()
        self.ui.setupUi(self)


class ThemeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_theme()
        self.ui.setupUi(self)
        self.setup_buttons()
        self.chosen_theme = parent.theme

    def setup_buttons(self):
        self.ui.theme_buttons.buttonClicked.connect(self.choose_theme)

    def choose_theme(self, button):
        self.chosen_theme = button.objectName()


class WordleWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setupKeyboard()
        self._setupAccesories()
        self.current_column = 1
        self.current_row = 1
        self.all_labels = self.dict_all_labels()
        self.keyboard_buttons = self.get_keyboard_buttons()
        self.password, self.all_words = draw_password()
        self.theme = "standard"

    def _input_letter_by_button(self, button):
        self.clear_error_label()
        if button.text() == "Backspace":
            self.delete_letter()
        elif button.text() == "Enter":
            if self.current_column == 6:
                self.check_guess()
            else:
                self.ui.error_label.setStyleSheet("""
                                    background-color: red;
                                    color: white""")
                self.ui.error_label.setText("Not enough letters")
        elif self.current_column == 6:
            pass
        else:
            row = self.current_row
            column = self.current_column
            self.all_labels[row][column].setText(button.text())
            self.current_column += 1

    def _setupKeyboard(self):
        self.ui.all_buttons.buttonClicked.connect(self._input_letter_by_button)

    def _setupAccesories(self):
        self.ui.rules.clicked.connect(self._display_rules)
        self.ui.theme.clicked.connect(self._display_themes)

    def _display_rules(self):
        dialog = How_to_play(self)
        dialog.exec()

    def _display_themes(self):
        if self.current_row == 1:
            dialog = ThemeDialog(self)
            dialog.exec()
            theme = dialog.chosen_theme
            self.theme = theme
            self.change_theme(self.theme)
        else:
            self.ui.error_label.setStyleSheet("""
                                    background-color: red;
                                    color: white""")
            self.ui.error_label.setText(
                "You can't change theme while guessing")

    def change_theme(self, theme):
        windows_children = self.ui.Windows.children()
        labels_listed = filter_children(windows_children, QLabel)
        if theme == "standard":
            combined_color = "#D8EFC2"
        elif theme == "black":
            combined_color = "black"
        else:
            combined_color = "white"
        self.ui.Combined.setStyleSheet(f"""background-color:
                            {combined_color}""")
        for button in self.keyboard_buttons:
            button.setStyleSheet(f"""border: 1px solid
                            {'white' if theme=='black' else 'black'};
                            background-color:
                            {'black' if theme=='black' else 'white'};
                            color: {'white' if theme=='black' else 'black'}
                            """)
        for label in labels_listed:
            label.setStyleSheet(f"""border: 1px solid
                            {'white' if theme=='black' else 'black'};
                            background-color:
                            {'black' if theme=='black' else 'white'};
                            color: {'white' if theme=='black' else 'black'}
                            """)
        self.ui.theme.setStyleSheet(f"""border-top: 2px solid
                            {'white' if theme=='black' else 'black'};
                            border-bottom: 2px solid
                            {'white' if theme=='black' else 'black'};
                            color: {'white' if theme=='black' else 'black'}
                            """)
        self.ui.rules.setStyleSheet(f"""border-top: 2px solid
                            {'white' if theme=='black' else 'black'};
                            border-bottom: 2px solid
                            {'white' if theme=='black' else 'black'};
                            color: {'white' if theme=='black' else 'black'}
                            """)
        self.ui.Windows.setStyleSheet(f"""border-top: 2px solid
                            {'white' if theme=='black'
                            else 'black'};""")
        self.ui.logo.setStyleSheet(f"""color:
                            {'white' if theme=='black' else 'black'};""")

    def delete_letter(self):
        if self.current_column > 1:
            self.current_column -= 1
            row = self.current_row
            column = self.current_column
            self.all_labels[row][column].setText('')
        else:
            pass

    def dict_all_labels(self):
        window_widget_list = self.ui.Windows.children()
        labels_listed = filter_children(window_widget_list, QLabel)
        labels_listed.sort(key=lambda x: x.objectName())
        labels_in_dict = {row: {column: labels_listed[(row-1)*5+(column-1)]
                          for column in range(1, 6)}
                          for row in range(1, 7)}
        return labels_in_dict

    def get_keyboard_buttons(self):
        keyboard_widget_list = self.ui.Keyboard.children()
        buttons_listed = filter_children(keyboard_widget_list, QPushButton)
        return buttons_listed

    def check_guess(self):
        letters = ''
        for label in self.all_labels[self.current_row].values():
            letters += label.text().lower()
        if letters in self.all_words:
            written_word = Word(letters)
            colors = self.password.compare(written_word)
            self.color_labels_and_buttons(colors, letters)
            self.current_row += 1
            if self.current_row > 6:
                self.game_lost()
            self.current_column = 1
        else:
            self.ui.error_label.setStyleSheet("""
                                    background-color: red;
                                    color: white""")
            self.ui.error_label.setText("Not in word list")

    def color_labels_and_buttons(self, colors, guess):
        row = self.current_row
        wht = "color: white"
        if self.theme == "white" or self.theme == "standard":
            border = "border: 2px solid black"
        else:
            border = "border: 2px solid white"
        for index, color in enumerate(colors):
            self.all_labels[row][index+1].setStyleSheet(
                f"background-color: {color}; {border}; {wht};")
            button_name = 2*guess[index]
            for button in self.keyboard_buttons:
                if button.objectName() == button_name:
                    b = button.palette().color(button.backgroundRole())
                    if b == 'green' or (b == '#FFAE20' and color != 'green'):
                        break
                    else:
                        button.setStyleSheet(
                            f"background-color: {color}; {border}; {wht};")

    def clear_error_label(self):
        self.ui.error_label.setStyleSheet('')
        self.ui.error_label.setText('')

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
