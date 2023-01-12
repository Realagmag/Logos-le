from PySide2.QtWidgets import QMainWindow, QApplication
import sys
from ui_wordle import Ui_MainWindow


class WordleWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setupKeyboard()
        self._setupWindows()

    def _setupKeyboard(self):
        pass

    def _setupWindows(self):
        pass


def guiMain(args):
    app = QApplication(args)
    window = WordleWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
