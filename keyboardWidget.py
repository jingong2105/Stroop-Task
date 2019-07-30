import sys
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import *

class KeyboardWidget (QWidget):
    keyPressed = pyqtSignal(str)
    def keyPressEvent(self, keyEvent):
        self.keyPressed.emit(keyEvent.text())
