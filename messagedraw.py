import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


BUBBLE_COLORS = {'user': "#666666", 'assist': "#a5d6a7"}
USER_TRANSLATE = {'user': QPoint(20, 0), 'assist': QPoint(0, 0)}

BUBBLE_PADDING = QMargins(10, 10, 10, 10)
TEXT_PADDING = QMargins(25, 15, 25, 15)


class MessageDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        user, text, pendingFlag = index.model().data(index, Qt.DisplayRole)
        # Create a custom QLabel for the message bubble
        label = QLabel(text)
        label.setWordWrap(True)  # Set the fixed width
        label.adjustSize()
        label.setStyleSheet(f"""
            QLabel {{
                background-color: {"#666666" if user == "user" else "#a5d6a7"};
                color: white;
                padding: 20px;
                border-radius: 20px;
                font-size: 16px;
                {"margin-left: 10px;" if user == "user" else "margin-right: 20px;"}
            }}
        """)

        # Adjust the label size based on the text
        label.adjustSize()

        # Calculate the position of the label based on the user type
        if user == "user":
            x = option.rect.right() - label.width() - 30
        else:
            x = option.rect.left() + 20
        if option.rect.top() == 0:
            y = option.rect.top() + 20
        else:
            y = option.rect.top() + label.height()*index.row() + 20

        # Draw the label on the painter
        painter.save()
        painter.translate(x, y)
        label.render(painter)
        painter.restore()

    def sizeHint(self, option, index):
        user, text, pendingFlag = index.model().data(index, Qt.DisplayRole)

        # Create a temporary QLabel to calculate the size hint
        label = QLabel(text)
        label.setStyleSheet(f"""
            QLabel {{
                background-color: {"#666666" if user == "user" else "#a5d6a7"};
                color: white;
                padding: 10px;
                border-radius: 10px;
            }}
        """)
        label.adjustSize()

        return label.size()

class MessageModel(QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(MessageModel, self).__init__(*args, **kwargs)
        self.messages = []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # Here we pass the delegate the user, message tuple.
            return self.messages[index.row()]

    def setData(self, index, role):
        if role == Qt.DisplayRole:
            if index.row() < len(self.messages):
                message = self.messages[index.row()]
                if message:
                    return message
        return QVariant()

    def rowCount(self, index):
        return len(self.messages)
        
    def update_message(self, index, new_message):
        """
        Update the message at the given index with the new message.
        """
        if 0 <= index < len(self.messages):
            who, _, pending_flag = self.messages[index]
            self.messages[index] = (who, new_message, pending_flag)
            self.dataChanged.emit(self.index(index), self.index(index), [Qt.DisplayRole])
            self.layoutChanged.emit()

    def add_message(self, who, text, pendingFlag):
        """
        Add an message to our message list, getting the text from the QLineEdit
        """
        if text:  # Don't add empty strings.
            # Access the list via the model.
            self.messages.append((who, text, pendingFlag))
            # Trigger refresh.
            self.layoutChanged.emit()