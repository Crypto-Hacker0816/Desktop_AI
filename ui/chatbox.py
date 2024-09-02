from ui.ui_chatbox import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class ChatBox(QWidget):
    
    def __init__(self, parent=None, flags: Qt.WindowFlags = Qt.FramelessWindowHint, inputType: str = "", msg : str = ''):
        super(ChatBox, self).__init__(parent, flags)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.inputType = inputType
        self.parent = parent
        self.changeMessage = pyqtSignal(str)
        if self.inputType == "user":
            self.ui.label.setText("USER")
        else:
            self.ui.label.setText("MIRADA AI")
        self.ui.label.setAlignment(Qt.AlignCenter)  # Set text alignment to center

        # Set the font size
        font = QFont()
        font.setBold(True)
        self.ui.label.setFont(font)
         
        self.ui.label.setStyleSheet(
            f"""
                QLabel{{
                    border-radius:10px;
                    background-color: {"#888888" if self.inputType == "user" else "#a22015"};
                    color: #FFFFFF;  
                    font-size: 10pt;
                    text-align: center;                  
                }}
            """
        )

        self.ui.plainTextEdit.setPlainText(msg)
        self.updateHeight()
        self.msg = msg
        self.changeMessage.connect(self.set_msg)

        

    def set_msg(self, msg):
        print(msg)
        self.ui.plainTextEdit.setPlainText(msg)
    def updateHeight(self):
        # Get the new height of the QPlainTextEdit
        new_height = self.ui.plainTextEdit.document().size().height() + self.ui.plainTextEdit.contentsMargins().top() + self.ui.plainTextEdit.contentsMargins().bottom()
        # Scaling factors and additional height
        scaling_factor_1 = 20  # Increase the height of self.ui.plainTextEdit by 50%  # Increase the height of self by 50%
        additional_height = 40  # Additional height for the ChatBox widget

        # Set the new minimum height of the QPlainTextEdit
        self.ui.plainTextEdit.setGeometry(13, 20, self.ui.plainTextEdit.width(), int(new_height * scaling_factor_1))
        
        # Set the new minimum height of the ChatBox
        self.ui.widget.setGeometry(0, 8, self.width(), int(new_height * scaling_factor_1 + additional_height))
        self.setGeometry(0, 0, self.width(), int(new_height * scaling_factor_1 + additional_height))

    def setMessage(self, msg):
        self.changeMessage.emit(msg)