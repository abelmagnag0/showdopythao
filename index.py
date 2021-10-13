import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
# function imports
from functions import frame1, frame2, frame3, frame4, grid

# inicia aplicação e config iniciais do gui
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Show do Pythão")

# tamanho da tela e onde ela se inicia
window.setFixedWidth(1100)
window.move(460, 200)

window.setStyleSheet("background:  #62BAAC;")

frame1()
window.setLayout(grid)

window.show()
sys.exit(app.exec())
