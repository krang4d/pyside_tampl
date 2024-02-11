import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow
from src.sidebar import MySideBar
#from Custom_Widgets import *

## Generate py from ui
os.system("pyside6-uic ui/interface.ui -o src/ui_interface.py")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MySideBar()
    window.show()
    sys.exit(app.exec())
