from PySide2.QtWidgets import QMainWindow, QApplication
import sys
from ui_wordle import Ui_MainWindow


letter_box = {1: {1: "r1c1", 2: "r1c2", 3: "r1c3",
              4: "r1c4", 5: "r1c5"},
              2: {1: "r2c1", 2: "r2c2", 3: "r2c3",
              4: "r2c4", 5: "r2c5"},
              3: {1: "r3c1", 2: "r3c2", 3: "r3c3",
              4: "r3c4", 5: "r3c5"},
              4: {1: "r4c1", 2: "r4c2", 3: "r4c3",
              4: "r4c4", 5: "r4c5"},
              5: {1: "r5c1", 2: "r5c2", 3: "r5c3",
              4: "r5c4", 5: "r5c5"},
              6: {1: "r6c1", 2: "r6c2", 3: "r6c3",
              4: "r6c4", 5: "r6c5"}}


class WordleWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setupKeyboard()
        self._setupWindows()
        self.current_column = 1
        self.current_row = 1


    def _input_letter_by_button(self, button):
        row = self.current_row
        column = self.current_column
        label_position = letter_box[row][column]
        all_labels = self.ui.Windows.children()
        for label in all_labels:
            if str(label.objectName()) == label_position:
                label.setText(button.text())
        self.current_column += 1
        pass

    def _setupWindows(self):
        pass

    def _setupKeyboard(self):
        self.ui.all_buttons.buttonClicked.connect(self._input_letter_by_button)


def guiMain(args):
    app = QApplication(args)
    window = WordleWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
