# -*- coding: utf-8 -*-
__author__ = "Felipe Oliveira"
__license__ = "MIT"
"""home.py: Navegador Open Source """

from PyQt5.QtWidgets import QApplication, QMainWindow,QToolButton, QLineEdit, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon, QPixmap

application = QApplication([])

mainWindow= QMainWindow()
mainWindow.setGeometry(0,0,1015,768)
mainWindow.setMinimumWidth(1015)
mainWindow.setMaximumWidth(1015)
mainWindow.setMinimumHeight(768)
mainWindow.setMaximumHeight(768)
mainWindow.setWindowTitle("MyBrowser")
mainWindow.setStyleSheet("background-color:rgb(0,0,0);")
mainWindow.setWindowIcon(QIcon("browser.png"))

mainWindow.show()
application.exec_()