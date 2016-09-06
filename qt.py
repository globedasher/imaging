"""
PyQt5 Hello, World.
Richard Morley
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

# Import Image handling libraries.
from PIL import Image

# Import the conversion code, convert.py
import convert


def main():
    img = convert.Convert(Image.open('original.jpg'))
    app = QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    button = QtWidgets.QPushButton('Hello, World!')
    window.setCentralWidget(button)
    window.show()
    app.exec_()

main()
