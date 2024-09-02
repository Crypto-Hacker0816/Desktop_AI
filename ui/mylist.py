from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyList(QScrollArea):
    def __init__(self):
        super().__init__()
        self._widget = QWidget()
        self._layout = QVBoxLayout()

        self._widget.setLayout(self._layout)
        self.setWidget(self._widget)
        self.setWidgetResizable(True)