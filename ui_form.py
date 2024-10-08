# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from label import Label
from numberbutton import numberButton
from operationbutton import operationButton
import rc_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(360, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/calculator.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = Label(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"FiraMono Nerd Font"])
        font.setPointSize(40)
        font.setWeight(QFont.Black)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: black; color: green;")
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)
        self.label.setWordWrap(True)
        self.label.setMargin(10)

        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Button_3 = numberButton(self.centralwidget)
        self.Button_3.setObjectName(u"Button_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Button_3.sizePolicy().hasHeightForWidth())
        self.Button_3.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Button_3, 0, 2, 1, 1)

        self.Button_Div = operationButton(self.centralwidget)
        self.Button_Div.setObjectName(u"Button_Div")
        sizePolicy2.setHeightForWidth(self.Button_Div.sizePolicy().hasHeightForWidth())
        self.Button_Div.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Button_Div, 3, 3, 1, 1)

        self.Button_2 = numberButton(self.centralwidget)
        self.Button_2.setObjectName(u"Button_2")
        sizePolicy2.setHeightForWidth(self.Button_2.sizePolicy().hasHeightForWidth())
        self.Button_2.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Button_2, 0, 1, 1, 1)

        self.Button_Minus = operationButton(self.centralwidget)
        self.Button_Minus.setObjectName(u"Button_Minus")
        sizePolicy2.setHeightForWidth(self.Button_Minus.sizePolicy().hasHeightForWidth())
        self.Button_Minus.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Button_Minus, 1, 3, 1, 1)

        self.Button_Plus = operationButton(self.centralwidget)
        self.Button_Plus.setObjectName(u"Button_Plus")
        sizePolicy2.setHeightForWidth(self.Button_Plus.sizePolicy().hasHeightForWidth())
        self.Button_Plus.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Button_Plus, 0, 3, 1, 1)

        self.Button_0 = numberButton(self.centralwidget)
        self.Button_0.setObjectName(u"Button_0")
        sizePolicy2.setHeightForWidth(self.Button_0.sizePolicy().hasHeightForWidth())
        self.Button_0.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Button_0, 3, 1, 1, 1)

        self.Button_6 = numberButton(self.centralwidget)
        self.Button_6.setObjectName(u"Button_6")
        sizePolicy2.setHeightForWidth(self.Button_6.sizePolicy().hasHeightForWidth())
        self.Button_6.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Button_6, 1, 2, 1, 1)

        self.Button_8 = numberButton(self.centralwidget)
        self.Button_8.setObjectName(u"Button_8")
        sizePolicy2.setHeightForWidth(self.Button_8.sizePolicy().hasHeightForWidth())
        self.Button_8.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Button_8, 2, 1, 1, 1)

        self.Button_Into = operationButton(self.centralwidget)
        self.Button_Into.setObjectName(u"Button_Into")
        sizePolicy2.setHeightForWidth(self.Button_Into.sizePolicy().hasHeightForWidth())
        self.Button_Into.setSizePolicy(sizePolicy2)
        self.Button_Into.setCheckable(False)

        self.gridLayout.addWidget(self.Button_Into, 2, 3, 1, 1)

        self.Button_5 = numberButton(self.centralwidget)
        self.Button_5.setObjectName(u"Button_5")
        sizePolicy2.setHeightForWidth(self.Button_5.sizePolicy().hasHeightForWidth())
        self.Button_5.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Button_5, 1, 1, 1, 1)

        self.Button_9 = numberButton(self.centralwidget)
        self.Button_9.setObjectName(u"Button_9")
        sizePolicy2.setHeightForWidth(self.Button_9.sizePolicy().hasHeightForWidth())
        self.Button_9.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Button_9, 2, 2, 1, 1)

        self.Button_Equal = QPushButton(self.centralwidget)
        self.Button_Equal.setObjectName(u"Button_Equal")
        sizePolicy2.setHeightForWidth(self.Button_Equal.sizePolicy().hasHeightForWidth())
        self.Button_Equal.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Button_Equal, 3, 2, 1, 1)

        self.Button_7 = numberButton(self.centralwidget)
        self.Button_7.setObjectName(u"Button_7")
        sizePolicy2.setHeightForWidth(self.Button_7.sizePolicy().hasHeightForWidth())
        self.Button_7.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Button_7, 2, 0, 1, 1)

        self.Button_1 = numberButton(self.centralwidget)
        self.Button_1.setObjectName(u"Button_1")
        sizePolicy2.setHeightForWidth(self.Button_1.sizePolicy().hasHeightForWidth())
        self.Button_1.setSizePolicy(sizePolicy2)
        self.Button_1.setAutoDefault(False)

        self.gridLayout.addWidget(self.Button_1, 0, 0, 1, 1)

        self.Button_4 = numberButton(self.centralwidget)
        self.Button_4.setObjectName(u"Button_4")
        sizePolicy2.setHeightForWidth(self.Button_4.sizePolicy().hasHeightForWidth())
        self.Button_4.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Button_4, 1, 0, 1, 1)

        self.Button_Clear = QPushButton(self.centralwidget)
        self.Button_Clear.setObjectName(u"Button_Clear")
        sizePolicy2.setHeightForWidth(self.Button_Clear.sizePolicy().hasHeightForWidth())
        self.Button_Clear.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Button_Clear, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Button_Clear.clicked.connect(self.label.clrScreen)
        self.Button_1.clickWithButtonName.connect(self.label.changeOutput)
        self.Button_2.clickWithButtonName.connect(self.label.changeOutput)
        self.Button_3.clickWithButtonName.connect(self.label.changeOutput)
        self.Button_4.clickWithButtonName.connect(self.label.changeOutput)
        self.Button_5.clickWithButtonName.connect(self.label.changeOutput)
        self.Button_6.clickWithButtonName.connect(self.label.changeOutput)
        self.Button_7.clickWithButtonName.connect(self.label.changeOutput)
        self.Button_8.clickWithButtonName.connect(self.label.changeOutput)
        self.Button_9.clickWithButtonName.connect(self.label.changeOutput)
        self.Button_0.clickWithButtonName.connect(self.label.changeOutput)
        self.Button_Plus.clickWithOperationName.connect(self.label.doOperation)
        self.Button_Minus.clickWithOperationName.connect(self.label.doOperation)
        self.Button_Into.clickWithOperationName.connect(self.label.doOperation)
        self.Button_Div.clickWithOperationName.connect(self.label.doOperation)
        self.Button_Equal.clicked.connect(self.label.getAnswer)

        self.Button_1.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Button_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Button_Div.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.Button_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Button_Minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.Button_Plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Button_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Button_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.Button_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.Button_Into.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.Button_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Button_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Button_Equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.Button_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.Button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Button_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Button_Clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
    # retranslateUi

