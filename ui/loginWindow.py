from ui.ui_login import Ui_login
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainterPath, QRegion
from PyQt5.QtCore import QRectF, Qt
from requests_oauthlib import OAuth2Session
import os

CLIENT_ID = os.environ.get('GOOGLE_AUTH')
class LoginWindow(QWidget):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        radius = 20.0
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), radius, radius)
        mask = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)

        self.ui.loginBtn.clicked.connect(self.connectWeb)
        self.ui.closeBtn.clicked.connect(self.close)
    
    def connectWeb(self):
        # authorization_base_url = 'http://localhost:3000/api/auth/authorize'
        # token_url = 'http://localhost:3000/api/auth/token'

        # oauth = OAuth2Session(CLIENT_ID)

        # # Redirect the user to the authorization URL
        # authorization_url, state = oauth.authorization_url(authorization_base_url)
        # print('Please go here and authorize:', authorization_url)
        print("HELLO WORLD")