# This Python file uses the following encoding: utf-8
from ui_form import Ui_MainWindow
import rc_resources
import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtGui

basedir = os.path.dirname(__file__)


try:
    from ctypes import windll  # Only exists on Windows.

    myappid = "mycompany.myproduct.subproduct.version"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    app.setWindowIcon(QtGui.QIcon(":/icons/hand_icon.ico"))
    widget.show()
    sys.exit(app.exec())
