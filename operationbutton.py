from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal


class operationButton(QPushButton):
    clickWithOperationName = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.clicked.connect(self.emitClickWithOperationName)

    def emitClickWithOperationName(self):
        self.clickWithOperationName.emit(self.text())
