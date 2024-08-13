from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QLabel
from PySide2.QtWidgets import QPushButton
import sys
from ui_wordle import Ui_MainWindow
from ui_how_to_play import Ui_how_to_play
from ui_theme import Ui_theme
from ui_game_over import Ui_game_over
from model import Word, draw_password, filter_children


class WordBaseNotFoundError(FileNotFoundError):
    pass


class Game_over(QDialog):
    '''
    This is class responsible for displaying "Game Over" window.

    Attributes:
        ui (Ui_game_over): Stores objects used in QT "Game Over" window.
        link (str): Game results with colorful squares
        and player's guesses.
    '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_game_over()
        self.ui.setupUi(self)
        self.link = self.create_link(parent)
        self.password = parent.password
        self.setup_window()

    def setup_window(self):
        self.ui.results.setText(f"The word is: {self.password}\n{self.link}")
        self.ui.link.setText(self.link)

    def create_link(self, game):
        '''
        Generate Logos'le summary link.

        Parameters:
            game (WordleWindow): Main window of Logos'le game.

        Returns:
            link: Formatted string that includes number of guesses
            and colorful squares that represent player's guesses.
        '''
        ye = "\U0001F7E8"
        gr = "\U0001F7E9"
        bl = "\U0001F7EB"
        row = game.current_row
        attempt = f"{'X' if not game.game_won else str(row)}"
        colors = game.color_history.format(green=gr, yellow=ye, grey=bl)
        link = f"logos'le {attempt}/6\n{colors}"
        return link


class How_to_play(QDialog):
    '''
    The class responsible for displaying "How to play" window.

    Attributes:
        ui (Ui_how_to_play): Stores objects of "How to play" window
    '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_how_to_play()
        self.ui.setupUi(self)


class ThemeDialog(QDialog):
    '''
    The class that enables changing game's theme.

    Attributes:
        ui (Ui_theme): Stores objects of "Theme" window.
        parent (WordleWindow): parent of QDialog
    '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_theme()
        self.ui.setupUi(self)
        self.setup_buttons()
        self.parent = parent

    def setup_buttons(self):
        self.ui.theme_buttons.buttonClicked.connect(self.choose_theme)

    def choose_theme(self, button):
        self.parent.theme = button.objectName()
        self.parent.change_theme(self.parent.theme)


class WordleWindow(QMainWindow):
    '''
    This is main class of Logos'le game.

    Is responsible for displaying and operating main window of the game.

    Attributes:
        ui (Ui_MainWindow): Stores objects of "Logos'le" window.
        current_row (int): Tracks number of guessing attempts.
        current_column (int): Tracks current letter in typed word.
        all_labes (dict): QLabels that display letters in order.
        keyboard_buttons (list): QPushButtons that create keyboard.
        theme (str): One of three possible game themes.
        game_won (bool): Tracks if the word is guessed.
        color_history(str): Memory of all used colors. Used to create
            link with summary of the game.
        password (Word): The word that must be guessed to win the game.
        all_words (list): All possible logos'le words.
    '''
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
        self.setpassword()
        self.theme = "standard"
        self.game_won = False
        self.color_history = ''

    def setpassword(self):
        try:
            with open("all.words.txt", 'r') as file_handle:
                self.password, self.all_words = draw_password(file_handle)
        except FileNotFoundError:
            raise WordBaseNotFoundError("Could not open word database")

    def _input_letter_by_button(self, button):
        '''
        The function to set reaction for keyboard Qpushbutton click.

        Depending on button clicked it either writes letter to the
        particular label, deletes letter or calls check guess function.

        Parameters:
            button (QPushButton): Button that called this function.
        '''
        self.clear_error_label()
        if self.game_won or self.current_row == 7:
            pass
        elif button.text() == "Backspace":
            self.delete_letter()
        elif button.text() == "Enter":
            if self.current_column == 6:
                self.check_guess()
            else:
                self.call_error("Not enough letters")
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
        else:
            self.call_error("You can't change theme while guessing")

    def change_theme(self, theme):
        '''
        The function to change theme of WordleWindow.

        It uses setStyleSheet methods on all QWidgets in WordleWindow
        to set their style appropriate to chosen theme.

        Parameters:
            theme (str): Style that WordleWindow has to adopt.
        '''
        windows_children = self.ui.Windows.children()
        labels_listed = filter_children(windows_children, QLabel)
        if theme == "standard":
            combined_color = "#D8EFC2"
            x = 'black'
        elif theme == "black":
            combined_color = "black"
            x = 'white'
        else:
            combined_color = "white"
            x = 'black'
        self.ui.Combined.setStyleSheet(f"""background-color:
                            {combined_color}""")
        for button in self.keyboard_buttons:
            button.setStyleSheet(f"""border: 1px solid {x};
                            background-color:
                            {'black' if theme=='black' else 'white'};
                            color: {x}""")
        for label in labels_listed:
            label.setStyleSheet(f"""border: 1px solid {x};
                            background-color:
                            {'black' if theme=='black' else 'white'};
                            color: {x}""")
        self.ui.theme.setStyleSheet(f"""border-top: 2px solid {x};
                            border-bottom: 2px solid {x};
                            color: {x}""")
        self.ui.rules.setStyleSheet(f"""border-top: 2px solid {x};
                            border-bottom: 2px solid {x};
                            color: {x}""")
        self.ui.Windows.setStyleSheet(f"border-top: 2px solid {x};")
        self.ui.logo.setStyleSheet(f"color: {x};")

    def delete_letter(self):
        '''
        Function that clears QLabel pointed by
        current_row and current_column class attributes
        and moves tracking on previous QLabel in row.
        '''
        if self.current_column > 1:
            self.current_column -= 1
            row = self.current_row
            column = self.current_column
            self.all_labels[row][column].setText('')

    def dict_all_labels(self):
        '''
        The function to create dictionary of QLabes.

        This function gets all QLebels used to show letters
        of player's guesses and arrange them into dictionary
        so every row (keys) has assigned 5 QLabel objects that
        create one 5 letter word (values)

        Returns:
            labels_in_dict(): Dictionary of QLabel objects
                              in row(keys): columns(values) order.
        '''
        window_widget_list = self.ui.Windows.children()
        labels_listed = filter_children(window_widget_list, QLabel)
        labels_listed.sort(key=lambda x: x.objectName())
        labels_in_dict = {row: {column: labels_listed[(row-1)*5+(column-1)]
                          for column in range(1, 6)}
                          for row in range(1, 7)}
        return labels_in_dict

    def get_keyboard_buttons(self):
        '''
        The function to list all QPushButtons used in keyboard.

        Returns:
            buttons_listed (list): list of all QPushButtons used in keyboard.
        '''
        keyboard_widget_list = self.ui.Keyboard.children()
        buttons_listed = filter_children(keyboard_widget_list, QPushButton)
        return buttons_listed

    def check_guess(self):
        '''
        The Function that reacts to clicked "Enter" button.

        It colors the QLabels depending on how close the quess was
        in accordance to the game rules. It also checks if
        end of the game conditions are met and calls game_over() function
        if the game is either lost or won.
        '''
        letters = ''
        for label in self.all_labels[self.current_row].values():
            letters += label.text().lower()
        if letters in self.all_words:
            written_word = Word(letters)
            colors = self.password.compare(written_word)
            self.color_labels_and_buttons(colors, letters)
            if written_word.name == self.password.name:
                self.game_won = True
                self.game_over()
            self.current_row += 1
            self.color_history += "\n"
            if self.current_row > 6 and not self.game_won:
                self.game_over()
            self.current_column = 1
        else:
            self.call_error("Not in word list")

    def color_labels_and_buttons(self, colors, guess):
        row = self.current_row
        wht = "color: white"
        if self.theme == "white" or self.theme == "standard":
            border = "border: 2px solid black"
        else:
            border = "border: 2px solid white"
        for index, color in enumerate(colors):
            if color == "#FFAE20":
                self.color_history += "{yellow}"
            elif color == "green":
                self.color_history += "{green}"
            else:
                self.color_history += "{grey}"
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

    def game_over(self):
        dialog = Game_over(self)
        dialog.exec()

    def call_error(self, msg):
        self.ui.error_label.setStyleSheet("""
                                    background-color: red;
                                    color: white""")
        self.ui.error_label.setText(msg)


def guiMain(args):
    '''
    The main function that starts the application.
    '''
    app = QApplication(args)
    window = WordleWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
