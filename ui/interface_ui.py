# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import icons_rc
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	background-color:  transparent;\n"
"	color:  white;\n"
"	/*border: none;*/\n"
"}\n"
"#side_menu, #side_icons, #header, main \n"
"{\n"
"	background-color: rgb(7, 30, 38);\n"
"}\n"
"#centralwidget\n"
"{\n"
"	background-color: rgb(4, 15, 19);\n"
"}\n"
"#side_menu QPushButton, #side_icons QPushButton\n"
"{\n"
"	padding: 10px;\n"
"	margin: 10px;\n"
"}\n"
"#side_menu QPushButton\n"
"{\n"
"	margin-right: 0px;\n"
"}\n"
"#side_menu QPushButton:checked\n"
"{\n"
"	background-color: rgb(4, 15, 19);\n"
"	color: rgb(38, 162, 105);\n"
"	font-weight: bold;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	/*margin: 1px;*/\n"
"}\n"
"#side_icons QPushButton:checked\n"
"{\n"
"	background-color: rgb(4, 15, 19);\n"
"	color: rgb(38, 162, 105);\n"
"	font-weight: bold;\n"
"	border-radius: 10px;\n"
"	/*margin: 1px;*/\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	background-color: rgb(7, 30, 38);\n"
"	border: none;\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.body = QFrame(self.centralwidget)
        self.body.setObjectName(u"body")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.body)
        self.gridLayout.setObjectName(u"gridLayout")
        self.side_icons = QFrame(self.body)
        self.side_icons.setObjectName(u"side_icons")
        self.side_icons.setMinimumSize(QSize(40, 0))
        self.side_icons.setFrameShape(QFrame.NoFrame)
        self.side_icons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.side_icons)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.icon_frame1 = QFrame(self.side_icons)
        self.icon_frame1.setObjectName(u"icon_frame1")
        self.icon_frame1.setFrameShape(QFrame.NoFrame)
        self.icon_frame1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.icon_frame1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.icon_frame1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(40, 40))
        self.label_5.setPixmap(QPixmap(u":/icons/photo.jpg"))
        self.label_5.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.label_5)


        self.verticalLayout_9.addWidget(self.icon_frame1, 0, Qt.AlignHCenter)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.item1_btn1 = QPushButton(self.side_icons)
        self.item1_btn1.setObjectName(u"item1_btn1")
        self.item1_btn1.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/feather/aperture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.item1_btn1.setIcon(icon)
        self.item1_btn1.setIconSize(QSize(24, 24))
        self.item1_btn1.setCheckable(True)
        self.item1_btn1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.item1_btn1)

        self.item2_btn1 = QPushButton(self.side_icons)
        self.item2_btn1.setObjectName(u"item2_btn1")
        self.item2_btn1.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/icons/feather/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.item2_btn1.setIcon(icon1)
        self.item2_btn1.setIconSize(QSize(24, 24))
        self.item2_btn1.setCheckable(True)
        self.item2_btn1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.item2_btn1)

        self.item3_btn1 = QPushButton(self.side_icons)
        self.item3_btn1.setObjectName(u"item3_btn1")
        self.item3_btn1.setFocusPolicy(Qt.NoFocus)
        self.item3_btn1.setIcon(icon)
        self.item3_btn1.setIconSize(QSize(24, 24))
        self.item3_btn1.setCheckable(True)
        self.item3_btn1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.item3_btn1)

        self.item4_btn1 = QPushButton(self.side_icons)
        self.item4_btn1.setObjectName(u"item4_btn1")
        self.item4_btn1.setFocusPolicy(Qt.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u":/icons/feather/paperclip.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.item4_btn1.setIcon(icon2)
        self.item4_btn1.setIconSize(QSize(24, 24))
        self.item4_btn1.setCheckable(True)
        self.item4_btn1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.item4_btn1)


        self.verticalLayout_9.addLayout(self.verticalLayout_3)

        self.verticalSpacer1 = QSpacerItem(20, 433, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer1)

        self.exit_btn1 = QPushButton(self.side_icons)
        self.exit_btn1.setObjectName(u"exit_btn1")
        self.exit_btn1.setFocusPolicy(Qt.NoFocus)
        icon3 = QIcon()
        icon3.addFile(u":/icons/feather/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn1.setIcon(icon3)
        self.exit_btn1.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.exit_btn1)


        self.gridLayout.addWidget(self.side_icons, 0, 0, 2, 1)

        self.side_menu = QFrame(self.body)
        self.side_menu.setObjectName(u"side_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.side_menu.sizePolicy().hasHeightForWidth())
        self.side_menu.setSizePolicy(sizePolicy1)
        self.side_menu.setMinimumSize(QSize(100, 0))
        self.side_menu.setMaximumSize(QSize(16777215, 16777215))
        self.side_menu.setStyleSheet(u"")
        self.side_menu.setFrameShape(QFrame.NoFrame)
        self.side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.side_menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_frame2 = QFrame(self.side_menu)
        self.icon_frame2.setObjectName(u"icon_frame2")
        self.icon_frame2.setMinimumSize(QSize(0, 40))
        self.icon_frame2.setFrameShape(QFrame.NoFrame)
        self.icon_frame2.setFrameShadow(QFrame.Raised)
        self.icon_frame2.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.icon_frame2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.icon_frame2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(40, 40))
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/icons/photo.jpg"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.icon_frame2)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setMargin(10)

        self.horizontalLayout.addWidget(self.label_7)


        self.verticalLayout.addWidget(self.icon_frame2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.item1_btn2 = QPushButton(self.side_menu)
        self.item1_btn2.setObjectName(u"item1_btn2")
        self.item1_btn2.setFocusPolicy(Qt.NoFocus)
        icon4 = QIcon()
        icon4.addFile(u":/icons/feather/chrome.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.item1_btn2.setIcon(icon4)
        self.item1_btn2.setIconSize(QSize(24, 24))
        self.item1_btn2.setCheckable(True)
        self.item1_btn2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.item1_btn2)

        self.item2_btn2 = QPushButton(self.side_menu)
        self.item2_btn2.setObjectName(u"item2_btn2")
        self.item2_btn2.setFocusPolicy(Qt.NoFocus)
        self.item2_btn2.setIcon(icon1)
        self.item2_btn2.setIconSize(QSize(24, 24))
        self.item2_btn2.setCheckable(True)
        self.item2_btn2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.item2_btn2)

        self.item3_btn2 = QPushButton(self.side_menu)
        self.item3_btn2.setObjectName(u"item3_btn2")
        self.item3_btn2.setFocusPolicy(Qt.NoFocus)
        self.item3_btn2.setIcon(icon)
        self.item3_btn2.setIconSize(QSize(24, 24))
        self.item3_btn2.setCheckable(True)
        self.item3_btn2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.item3_btn2)

        self.item4_btn2 = QPushButton(self.side_menu)
        self.item4_btn2.setObjectName(u"item4_btn2")
        self.item4_btn2.setMinimumSize(QSize(100, 0))
        self.item4_btn2.setFocusPolicy(Qt.NoFocus)
        self.item4_btn2.setIcon(icon2)
        self.item4_btn2.setIconSize(QSize(24, 24))
        self.item4_btn2.setCheckable(True)
        self.item4_btn2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.item4_btn2)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.verticalSpacer2 = QSpacerItem(20, 433, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer2)

        self.exit_btn2 = QPushButton(self.side_menu)
        self.exit_btn2.setObjectName(u"exit_btn2")
        self.exit_btn2.setFocusPolicy(Qt.NoFocus)
        self.exit_btn2.setIcon(icon3)
        self.exit_btn2.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.exit_btn2)


        self.gridLayout.addWidget(self.side_menu, 0, 1, 2, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.body)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 10))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)

        self.frame = QFrame(self.body)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(20, 20))
        self.frame.setMaximumSize(QSize(20, 20))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.menu_Btn = QPushButton(self.body)
        self.menu_Btn.setObjectName(u"menu_Btn")
        sizePolicy1.setHeightForWidth(self.menu_Btn.sizePolicy().hasHeightForWidth())
        self.menu_Btn.setSizePolicy(sizePolicy1)
        self.menu_Btn.setMinimumSize(QSize(40, 40))
        self.menu_Btn.setMaximumSize(QSize(40, 40))
        self.menu_Btn.setFocusPolicy(Qt.NoFocus)
        icon5 = QIcon()
        icon5.addFile(u":/icons/feather/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_Btn.setIcon(icon5)
        self.menu_Btn.setIconSize(QSize(24, 24))
        self.menu_Btn.setCheckable(True)
        self.menu_Btn.setChecked(True)

        self.gridLayout_3.addWidget(self.menu_Btn, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 0, 2, 1, 1)

        self.main = QFrame(self.body)
        self.main.setObjectName(u"main")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy2)
        self.main.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.main)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(False)
        self.stackedWidget.setFocusPolicy(Qt.TabFocus)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_8 = QVBoxLayout(self.page_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_1 = QLabel(self.page_1)
        self.label_1.setObjectName(u"label_1")
        font2 = QFont()
        font2.setPointSize(24)
        self.label_1.setFont(font2)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_6 = QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_7 = QVBoxLayout(self.page_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.page_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.page_4)

        self.horizontalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.body, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.item1_btn1, self.item2_btn1)
        QWidget.setTabOrder(self.item2_btn1, self.item3_btn1)
        QWidget.setTabOrder(self.item3_btn1, self.item4_btn1)
        QWidget.setTabOrder(self.item4_btn1, self.exit_btn1)
        QWidget.setTabOrder(self.exit_btn1, self.exit_btn2)

        self.retranslateUi(MainWindow)
        self.menu_Btn.toggled.connect(self.side_menu.setHidden)
        self.exit_btn2.clicked.connect(MainWindow.close)
        self.menu_Btn.toggled.connect(self.side_icons.setVisible)
        self.exit_btn1.clicked.connect(MainWindow.close)
        self.item1_btn1.toggled.connect(self.item1_btn2.setChecked)
        self.item2_btn1.toggled.connect(self.item2_btn2.setChecked)
        self.item3_btn1.toggled.connect(self.item3_btn2.setChecked)
        self.item4_btn1.toggled.connect(self.item4_btn2.setChecked)
        self.item4_btn2.toggled.connect(self.item4_btn1.setChecked)
        self.item3_btn2.toggled.connect(self.item3_btn1.setChecked)
        self.item2_btn2.toggled.connect(self.item2_btn1.setChecked)
        self.item1_btn2.toggled.connect(self.item1_btn1.setChecked)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText("")
        self.item1_btn1.setText("")
        self.item2_btn1.setText("")
        self.item3_btn1.setText("")
        self.item4_btn1.setText("")
        self.exit_btn1.setText("")
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.item1_btn2.setText(QCoreApplication.translate("MainWindow", u"Item 1", None))
        self.item2_btn2.setText(QCoreApplication.translate("MainWindow", u"Item 2", None))
        self.item3_btn2.setText(QCoreApplication.translate("MainWindow", u"Item 3", None))
        self.item4_btn2.setText(QCoreApplication.translate("MainWindow", u"Item 4", None))
        self.exit_btn2.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MY APP", None))
        self.menu_Btn.setText("")
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Item 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Item 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Item 3", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Item 4", None))
    # retranslateUi

