from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal


class numberButton(QPushButton):
    clickWithButtonName = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.clicked.connect(self.emitClickWithButtonName)

    def emitClickWithButtonName(self):
        self.clickWithButtonName.emit(self.text())
