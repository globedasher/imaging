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
from convert import Convert


class Editor(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        
        red_btn = QPushButton('Make Red', self)
        red_btn.clicked.connect(self.redButtonClicked)
        red_btn.resize(red_btn.sizeHint())
        red_btn.move(5, 5)

        grn_btn = QPushButton('Make Green', self)
        grn_btn.clicked.connect(self.greenButtonClicked)
        grn_btn.resize(red_btn.sizeHint())
        grn_btn.move(5, 30)

        blu_btn = QPushButton('Make Blue', self)
        blu_btn.clicked.connect(self.blueButtonClicked)
        blu_btn.resize(red_btn.sizeHint())
        blu_btn.move(5, 55)

        button = QPushButton('Quit', self)
        button.clicked.connect(QCoreApplication.instance().quit)
        button.resize(button.sizeHint())
        button.move(5, 80)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Image Editor')
        self.show()

    def redButtonClicked(self):
        img = Convert(Image.open('original.jpg'))
        img.convert_image_to_red()
    
    def greenButtonClicked(self):
        img = Convert(Image.open('original.jpg'))
        img.convert_image_to_green()
    
    def blueButtonClicked(self):
        img = Convert(Image.open('original.jpg'))
        img.convert_image_to_blue()




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ed = Editor()
    sys.exit(app.exec_())
