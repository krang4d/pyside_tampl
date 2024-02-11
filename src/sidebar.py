from PySide6.QtCore import Qt
from src.ui_interface import *
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Tamplate")

        self.side_menu.setHidden(True)
        self.side_icons.setHidden(False)

        self.item1_btn1.clicked.connect( lambda : { self.switch_to_item(0) } )
        self.item2_btn1.clicked.connect( lambda : { self.switch_to_item(1) } )
        self.item3_btn1.clicked.connect( lambda : { self.switch_to_item(2) } )
        self.item4_btn1.clicked.connect( lambda : { self.switch_to_item(3) } )

        self.item1_btn2.clicked.connect( lambda : { self.switch_to_item(0) } )
        self.item2_btn2.clicked.connect( lambda : { self.switch_to_item(1) } )
        self.item3_btn2.clicked.connect( lambda : { self.switch_to_item(2) } )
        self.item4_btn2.clicked.connect( lambda : { self.switch_to_item(3) } )

    def switch_to_item(self, item):
        self.stackedWidget.setCurrentIndex(item)