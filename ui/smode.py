from ui.ui_smode import Ui_smode
from PyQt5.QtWidgets import QWidget, QDesktopWidget
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainterPath, QRegion

class SModeWindow(QWidget):
    def __init__(self, parent=None):
        super(SModeWindow, self).__init__()
        self.ui = Ui_smode()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.parent = parent
        radius = 20.0
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), radius, radius)
        mask = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
        # self.setGeometry(QDesktopWidget().availableGeometry().width() - self.width(), 0, self.width(), self.height())

        self.ui.smodeBtn.clicked.connect(self.switchUi)
        self.ui.closeBtn.clicked.connect(self.close)
        self.hide()

    def switchUi(self):
        if self.isVisible():
            self.hide()
            self.parent.show()
        else:
            self.show().hide()