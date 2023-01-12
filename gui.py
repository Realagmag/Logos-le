import sys
from ui_wordle import Ui_MainWindow

class WordleWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setupKeyboard()
        self._setupWindows()

    def _setupKeyboard():



def guiMain(args):
    app = Ui_MainWindow(args)

    pass


if __name__ == "__main__":
    guiMain(sys.argv)
