"""
PyQt5 Image Editor application.

author: Richard Morley
"""

import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
        QHBoxLayout, QLabel)
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QPixmap

# Import Image handling libraries.
from PIL import Image

# Import the conversion code, convert.py
from convert import Convert


class Editor(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        """
        This method sets up the UI for the Editor Application.
        """
        disp_btn = QPushButton('Display Original', self)
        disp_btn.clicked.connect(self.display_original)
        disp_btn.resize(disp_btn.sizeHint())
        disp_btn.move(5, 30)

        red_btn = QPushButton('Make Red', self)
        red_btn.clicked.connect(self.redButtonClicked)
        red_btn.resize(red_btn.sizeHint())
        red_btn.move(5, 5)

        grn_btn = QPushButton('Make Green', self)
        grn_btn.clicked.connect(self.greenButtonClicked)
        grn_btn.resize(red_btn.sizeHint())
        grn_btn.move(90, 5)

        blu_btn = QPushButton('Make Blue', self)
        blu_btn.clicked.connect(self.blueButtonClicked)
        blu_btn.resize(red_btn.sizeHint())
        blu_btn.move(175, 5)

        button = QPushButton('Quit', self)
        button.clicked.connect(QCoreApplication.instance().quit)
        button.resize(button.sizeHint())
        button.move(265, 5)

        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle('Image Editor')
        self.show()

    def display_original(self):
        """
        Display the original picture to be modified.
        """
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('original.jpg')

        lbl =  QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

    def redButtonClicked(self):
        """
        This function is called when the Make Blue button is pressed in the
        application to then call the convert_image_to_xxx method.
        """
        img = Convert(Image.open('original.jpg'))
        img.convert_image_to_red()
        self.display_saved()
    
    def greenButtonClicked(self):
        """
        This function is called when the Make Blue button is pressed in the
        application to then call the convert_image_to_xxx method.
        """
        img = Convert(Image.open('original.jpg'))
        img.convert_image_to_green()
        self.display_saved()
    
    def blueButtonClicked(self):
        """
        This function is called when the Make Blue button is pressed in the
        application to then call the convert_image_to_xxx method.
        """
        img = Convert(Image.open('original.jpg'))
        img.convert_image_to_blue()
        self.display_saved()

    def display_saved(self):
        """
        Displays the altered image after the alter image button is pressed in 
        application.
        """
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('saved.jpg')

        lbl =  QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        #self.setLayout(hbox)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ed = Editor()
    sys.exit(app.exec_())
