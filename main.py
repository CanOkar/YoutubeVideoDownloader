import sys
import threading
import pytube
from urllib.request import urlretrieve
from pytube import YouTube
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QComboBox, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from click_events import start_download, start_check

class App(QWidget):
    """this class assigns variables that relevant dimensions of the screen and calls initUI module which creates GUI """

    def __init__(self):
        super().__init__()
        self.title = "Youtube Video Downloader"
        self.left = 100
        self.top = 100
        self.width = 360
        self.height = 250
        self.initUI()

    def initUI(self):

        # create a window
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)

        # create a textbox for video address
        self.videoaddress = QLineEdit(self)
        self.videoaddress.move(10, 30)
        self.videoaddress.resize(240, 25)

        # create a textfield to display path that video will be downladed
        self.downloadpath = QLineEdit(self)
        self.downloadpath.move(10, 84)
        self.downloadpath.resize(240, 25)
        self.downloadpath.setEnabled(False)

        # check-video button to check available items to download
        self.checkvideo = QPushButton("Check Video", self)
        self.checkvideo.setToolTip("Click to check to see available resulations")
        self.checkvideo.resize(100, 25)
        self.checkvideo.move(251, 30)
        self.checkvideo.clicked.connect(self.on_click_check)

        # create a button named by download
        self.downloadbutton = QPushButton('Download', self)
        self.downloadbutton.setToolTip('Download')
        self.downloadbutton.move(251, 57)
        self.downloadbutton.resize(100, 25)
        self.downloadbutton.clicked.connect(self.on_click_download)

        # create a button named by browse
        self.browsebutton = QPushButton("Browse", self)
        self.browsebutton.move(251, 84)
        self.browsebutton.resize(100, 25)
        self.browsebutton.clicked.connect(self.on_click_browse)

        # create a combobox that shows available resulations of a video
        self.chooseresulation = QComboBox(self)
        self.chooseresulation.setFixedSize(240, 25)
        self.chooseresulation.move(10, 57)

        # show the video's thumbnail
        self.videothumb = QLabel(self)
        self.videothumb.move(10, 120)
        self.videothumb.setFixedSize(120, 90)

        # show video's name
        self.namelabel = QLabel(self)
        self.namelabel.setWordWrap(True)
        self.namelabel.move(140, 114)
        self.namelabel.resize(210, 70)
        self.show()

    def on_click_download(self):
        start_download(self , QMessageBox, threading, YouTube, pytube)

    def on_click_check(self):
        start_check(self, QMessageBox, threading, YouTube, urlretrieve, QPixmap)

    def on_click_browse(self):
        directory = QFileDialog.getExistingDirectory()
        self.downloadpath.setText(directory)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
