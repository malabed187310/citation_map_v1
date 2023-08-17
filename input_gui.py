from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
from subprocess import Popen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(980, 450)

        # set window title
        self.setWindowTitle("Citation Map")
        self.setObjectName("MainWindow")
        
        # set the background
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap("ComEd-2.png"))
        self.background_label.setGeometry(675, 325, 275, 100)
        self.background_label.setScaledContents(True)
        
        # create a label and add to layout
        self.label = QLabel("Enter the articel name:", self)
        self.label.move(165, 100)
        self.label.adjustSize()
        self.label.setFont(QFont("Times", 16, QFont.Bold))
        self.label.resize(800, 45)

        # create a text field
        self.textbox = QLineEdit(self)
        self.textbox.move(150, 150)
        self.textbox.resize(550, 40)

        # create table button and add to layout
        self.button = QPushButton("Enter", self)
        self.button.setGeometry(750, 145, 100, 50)
        self.button.clicked.connect(self.on_click)


    def on_click(self):
        script_path = 'api_cited.py'
        Popen(['python', script_path])





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())