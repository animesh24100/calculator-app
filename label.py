from PySide6.QtWidgets import QLabel


class Label(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.clrScreen()

        self.currentAnswer = self.text()

    def clrScreen(self):
        self.setText("0")
        self.currentAnswer = "0"

    def changeOutput(self, buttonName):
        newText = str(int(self.text() + buttonName))
        self.setText(newText)
        self.currentAnswer = newText

    def doOperation(self, operation):
        self.num1 = self.currentAnswer
        self.clrScreen()
        self.getchop = operation

    def getAnswer(self):
        self.currentAnswer = self.text()
        match self.getchop:
            case "+":
                answer = str(int(self.num1) + int(self.currentAnswer))
                self.setText(answer)
            case "-":
                answer = str(int(self.num1) - int(self.currentAnswer))
                self.setText(answer)
            case "×":
                answer = str(int(self.num1) * int(self.currentAnswer))
                self.setText(answer)
            case "÷":
                try:
                    answer = str(int(self.num1) / int(self.currentAnswer))
                    self.setText(answer)
                except ZeroDivisionError:
                    self.setText("CANNOT DIVIDE BY ZERO")
        self.num1 = None
        self.currentAnswer = None
        self.getchop = None
