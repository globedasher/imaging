#!/urs/bin/python3
#-*- coding: utf-8 -*-

"""
PyQt5 Hello, World.

author: Richard Morley
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

# Import Image handling libraries.
from PIL import Image

# Import the conversion code, convert.py
import convert


class Editor(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        img = convert.Convert(Image.open('original.jpg'))
        
        red_btn = QPushButton('Make Red', self)
        red_btn.clicked.connect(convert.Convert.convert_image_to_red)
        red_btn.resize(red_btn.sizeHint())
        red_btn.move(50, 20)

        button = QPushButton('Quit', self)
        button.clicked.connect(QCoreApplication.instance().quit)
        button.resize(button.sizeHint())
        button.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Image Editor')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ed = Editor()
    sys.exit(app.exec_())
