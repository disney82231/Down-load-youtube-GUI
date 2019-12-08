import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize , QTimer
from PyQt5.QtGui import * 
from pytube import YouTube
import os
import time
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(600, 200))    
        self.setWindowTitle("下載影片程式") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('網址:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(500, 32)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('下載', self)
#        pybutton.clicked.connect(self.clickMethod)
        pybutton.clicked.connect(self.Download)
#        pybutton.clicked.connect(self.Download1)
        pybutton.resize(200,32)
        pybutton.move(80, 60)        

        self.statusline = QLineEdit(self)
        self.statusline.move(80, 100)
        self.statusline.resize(200, 32)
        
#        self.statusline1 = QLineEdit(self)
#        self.statusline1.move(80, 140)
#        self.statusline1.resize(200, 32)
#        
    def clickMethod(self):
        print('')
    def Download(self):
        self.statusline.setText('開始下載')
        if not os.path.isdir('D:\\下載影片'):
            os.mkdir('D:\\下載影片')
        yt = YouTube(self.line.text())
        
        

        video=yt.streams.filter(file_extension='mp4').first()
        video.download(r'D:\\下載影片')
        QTimer.singleShot(1000, lambda: self.statusline.setText('下載完成'))

#    def Download1(self):
#        self.statusline.setText('下載完成')
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
    
