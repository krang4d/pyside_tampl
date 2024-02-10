import sys, os
from src.ui_interface import *
#from Custom_Widgets import *

## Generate py from ui
os.system("pyside6-uic ui/interface.ui -o src/ui_interface.py")

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        #loadJsonStyle(self, self.ui)
        ########################################################################
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

