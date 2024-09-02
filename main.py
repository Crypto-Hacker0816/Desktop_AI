from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import *
from ui.ui_main import Ui_main
from ui.smode import *
from ui.loginWindow import *
from ui.chatbox import ChatBox
from gptProcess import *
from messagedraw import *
import sys
import os
import asyncio
from gptProcess import *


chatHistory = []
        
class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)
        menu = QMenu(parent)
        openAction = menu.addAction("Open")
        exitAction = menu.addAction("Exit")
        self.setContextMenu(menu)

class GptProcess(QObject):
    global chatHistory
    finished = pyqtSignal()
    subTaskGenerated = pyqtSignal()
    messageReceived = pyqtSignal(tuple)

    def run(self):
        global chatHistory
        try:
            new_chat_history = []
            
            for item in chatHistory:
                new_item = {'role': item['role'], 'content': item['content']}
                new_chat_history.append(new_item)
            sendData = dataToSend
            sendData["messages"].extend(new_chat_history)
            headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {RP_CHAT_TOKEN}'}
            url = f'https://api.runpod.ai/v2/{RP_CHAT_ID}/openai/v1/chat/completions'
            try:
                response =  requests.post(url=url, json=sendData, headers=headers, timeout=60000)
                buffer = ""
                finalMessage = ""
                piece_buffer = []
                chatBox = ChatBox(inputType="assistant", msg="")
                for chunk in response:
                    buffer = buffer + chunk.decode('utf-8')
                    piece_buffer = buffer.split('\n\n')
                for index, piece in enumerate(piece_buffer):
                    if piece.find('[DONE]') !=-1:
                        return
                    jsonString = fix_malformed_json(piece)
                    try:
                        jsonContent = json.loads(jsonString)
                        try:
                            finalMessage = finalMessage + jsonContent['choices'][0]['delta']['content']
                            self.messageReceived.emit((index, jsonContent['choices'][0]['delta']['content'], chatBox))
                        except Exception as e:
                            continue
                    except json.JSONDecodeError as e:
                        continue
            except requests.exceptions.RequestException as e:
                print("Error", e)
                pass
            except ValueError as e:
                print("Error", e)
                pass
            self.subTaskGenerated.emit()
            self.finished.emit()
        except Exception as e:
            print(e)
class MainWindow(QWidget):
    render_chat_Box = pyqtSignal(list)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_main()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.smode = SModeWindow(self)
        self.login = LoginWindow(self)
        radius = 20.0
        path = QPainterPath()
        self.update_msg = ""
        self.chatBox_list = []
        
        path.addRoundedRect(QRectF(self.rect()), radius, radius)
        mask = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
        resource_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resource')
        icon_path = os.path.join(resource_dir, 'tray.png')
        screeWidth = QDesktopWidget().availableGeometry().width()
        self.setGeometry(QRect(screeWidth - self.width(), 0, self.width(), self.height()))

        self.trayIcon = SystemTrayIcon(QIcon(icon_path), self)
        self.trayIcon.show()
        self.trayIcon.activated.connect(self.show_main_window)
        self.trayIcon.contextMenu().actions()[1].triggered.connect(self.quit_app)
        self.trayIcon.contextMenu().actions()[0].triggered.connect(self.show_app)
        self.render_chat_Box.connect(self.renderChatBoxes)
        self.scrollAreaWidget = QWidget()
        self.chatLayout = QVBoxLayout(self.ui.scrollArea)
        
        self.scrollAreaWidget.setLayout(self.chatLayout)
        self.ui.scrollArea.setWidget(self.scrollAreaWidget)
        self.scrollAreaWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ui.scrollArea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    
        
        self.ui.closeBtn.clicked.connect(self.close)
        self.ui.smodeBtn.clicked.connect(self.switchUi)
        self.ui.sendMsgBtn.clicked.connect(self.sendMsg)

    def show_main_window(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            # self.login.show()
            self.show()

    def resizeEvent(self, e):
        pass
        # self.model.layoutChanged.emit()    
    
    def quit_app(self):
        self.hide()
    
    def show_app(self):
        # self.login.show()
        self.show()
    
    def switchUi(self):
        if self.isVisible():
            self.hide()
            self.smode.show()
        elif self.smode.isVisible():
            self.smode.hide()
            self.show()

    def finishGPT(self):
        return

    def sendMsg(self):
        global chatHistory
        msg = self.ui.messagInput.text()
        chatHistory.append({'role' : 'user', 'content' : msg, 'pendingMessage' : False})
        chatBox = ChatBox(inputType='user', msg=msg)
        self.chatBox_list.append(chatBox)
        self.scrollAreaWidget.adjustSize()
        self.render_chat_Box.emit(self.chatBox_list)
        
        self.ui.messagInput.clear()
        self.thread = QThread(parent=self)
        self.gptProcess = GptProcess()

        self.gptProcess.moveToThread(self.thread)
        self.thread.started.connect(self.gptProcess.run)
        self.gptProcess.messageReceived.connect(self.handleMessage)
        self.gptProcess.finished.connect(self.thread.quit)
        self.gptProcess.finished.connect(self.gptProcess.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.gptProcess.finished.connect(self.finishGPT)

        self.thread.start()
    def handleMessage(self, data): 
        index, message, chatBox = data
        global chatHistory
        if message:
            self.update_msg = self.update_msg + message
            chatBox.setMessage(self.update_msg)
            self.chatBox_list.append(chatBox)
        else:
            chatHistory.append({'role' : 'assistant', 'content' : self.update_msg, 'pendingMessage' : False})
            self.update_msg = ''
            chatBox.setMessage(self.update_msg)
            self.chatBox_list.append(chatBox)
        self.chatBox_list.pop(len(self.chatBox_list) - 1)

    def renderChatBoxes(self, data):
        for chatBox in data:
            self.chatLayout.addWidget(chatBox)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.hide()
    sys.exit(app.exec())
