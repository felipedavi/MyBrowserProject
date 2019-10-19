# -*- coding: utf-8 -*-
__author__ = "Felipe Oliveira"
__license__ = "MIT"
"""home.py: Navegador Open Source """

from PyQt5.QtWidgets import QApplication, QMainWindow,QToolButton, QLineEdit, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon, QPixmap

home_url     = "https://www.google.com"
facebook_url = "https://www.facebook.com"
twitter_url  = "https://www.twitter.com"
youtube_url  = "https://www.youtube.com"

def home(mainWindow):
	web.load(QUrl(home_url))
def reload(mainWindow):
	web.reload()
def back(mainWindow):
	web.back()
def forward(mainWindow):
	web.forward()
def go(mainWindow):
	go_url = go_line.text()
	web.load(QUrl(go_url))
def facebook(mainWindow):
	web.load(QUrl(facebook_url))
def twitter(mainWindow):
	web.load(QUrl(twitter_url))
def youtube(mainWindow):
	web.load(QUrl(youtube_url))
def download(item):
	item.accept()
	msg = QMessageBox()
	msg.setWindowTitle("DOWNLOAD")
	msg.setText("O SEU DOWNLOAD FOI INICIALIZADO")
	msg.setIcon(QMessageBox.Warning)
	msg.exec_()

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

web = QWebEngineView(mainWindow)
web.setGeometry(0,30,1015,768)
web.setStyleSheet("background-color:rgb(255,255,255);")
web.load(QUrl(home_url))

home_button = QToolButton(mainWindow)
home_button.setGeometry(10,3,25,25)
home_button.setStyleSheet("background-color:transparent;")
home_button_icon = QIcon()
home_button_icon.addPixmap(QPixmap("home.png"))
home_button.setIcon(home_button_icon)
home_button.clicked.connect(home)

reload_button = QToolButton(mainWindow)
reload_button.setGeometry(60,3,25,25)
reload_button.setStyleSheet("background-color:transparent;")
reload_button_icon = QIcon()
reload_button_icon.addPixmap(QPixmap("reload.png"))
reload_button.setIcon(reload_button_icon)
reload_button.clicked.connect(reload)

back_button = QToolButton(mainWindow)
back_button.setGeometry(140,3,25,25)
back_button.setStyleSheet("background-color:transparent;")
back_button_icon = QIcon()
back_button_icon.addPixmap(QPixmap("back.png"))
back_button.setIcon(back_button_icon)
back_button.clicked.connect(back)

forward_button = QToolButton(mainWindow)
forward_button.setGeometry(180,3,25,25)
forward_button.setStyleSheet("background-color:transparent;")
forward_button_icon = QIcon()
forward_button_icon.addPixmap(QPixmap("forward.png"))
forward_button.setIcon(forward_button_icon)
forward_button.clicked.connect(forward)

go_line = QLineEdit(mainWindow)
go_line.setGeometry(280,3,300,25)
go_line.setStyleSheet("background-color:rgb(255,255,255);")

go_button = QToolButton(mainWindow)
go_button.setGeometry(600,3,25,25)
go_button.setStyleSheet("background-color:transparent;")
go_button_icon = QIcon()
go_button_icon.addPixmap(QPixmap("go.png"))
go_button.setIcon(go_button_icon)
go_button.clicked.connect(go)

facebook_button = QToolButton(mainWindow)
facebook_button.setGeometry(905,3,50,25)
facebook_button.setStyleSheet("background-color:transparent;")
facebook_button_icon = QIcon()
facebook_button_icon.addPixmap(QPixmap("fb.png"))
facebook_button.setIcon(facebook_button_icon)
facebook_button.setIconSize(QSize(22,22))
facebook_button.clicked.connect(facebook)

twitter_button = QToolButton(mainWindow)
twitter_button.setGeometry(940,3,50,25)
twitter_button.setStyleSheet("background-color:transparent;")
twitter_button_icon = QIcon()
twitter_button_icon.addPixmap(QPixmap("tw.png"))
twitter_button.setIcon(twitter_button_icon)
twitter_button.setIconSize(QSize(22,22))
twitter_button.clicked.connect(twitter)

youtube_button = QToolButton(mainWindow)
youtube_button.setGeometry(975,3,50,25)
youtube_button.setStyleSheet("background-color:transparent;")
youtube_button_icon = QIcon()
youtube_button_icon.addPixmap(QPixmap("yt.png"))
youtube_button.setIcon(youtube_button_icon)
youtube_button.setIconSize(QSize(22,22))
youtube_button.clicked.connect(youtube)


mainWindow.show()
application.exec_()