from PyQt5.QtWidgets import QFrame 
from PyQt5.uic import loadUi 

class Message(QFrame):
    def __init__(self, text, parent):
        super().__init__(parent)
        loadUi("./app/ui/dialog.ui", self)
        
        self.ok_button.clicked.connect(self.deleteLater)
        self.label.setText(text)
        self.setGeometry(630, 30, 350, 433)
        self.show()

class ChoiceMessage(QFrame):
    def __init__(self, text, func,parent):
        super().__init__(parent)
        loadUi("./app/ui/choice_dialog.ui", self)
        self.func = func
        self.cancel_button.clicked.connect(self.deleteLater)
        self.ok_button.clicked.connect(self.ok_action)
        self.label.setText(text)
        self.setGeometry(630, 30, 350, 433)
        self.show()

    def ok_action(self):
        self.func()
        self.deleteLater()