from pytube.exceptions import RegexMatchError
import threading
import time
# this function downloads videos


def start_download(self, QMessageBox, threading, YouTube, pytube, chooseresulation, downloadbutton):
    videoAddressValue = self.videoaddress.text()
    downloadFolder = self.downloadpath.text()

    if videoAddressValue == "":
        QMessageBox.warning(self, "Video address error", "Please paste your video address and hit Check Video"
                                                         " button", QMessageBox.Ok)
    elif self.chooseresulation.currentText() == "":
        QMessageBox.warning(self, "Youtube Downloader", "Please click Check button to select resulation")
    elif downloadFolder == "":
        QMessageBox.warning(self, 'Youtube Downloader', "Please set a download path by Browse button",
                            QMessageBox.Ok)
    else:
        # change text on download button with "downloading" and deactive the button
        self.downloadbutton.setText("Downloading")
        self.downloadbutton.setEnabled(False)


        # create the class of download-thread to divide download event from main thread
        class Download_thread(threading.Thread):
            def __init__(self, coohseResulation, downloadbutton):
                threading.Thread.__init__(self)
                self.chooseresulation = coohseResulation
                self.downloadbutton = downloadbutton

            def run(self):
                # download the video from youtube
                yt = YouTube(videoAddressValue)
                resulation = self.chooseresulation.currentText()
                itagValue = int(resulation.split(' ', 5)[3])
                stream = yt.streams.get_by_itag(itagValue).download(downloadFolder)
                self.downloadbutton.setText("Download")
                self.downloadbutton.setEnabled(True)

        # start download thread
        download_thread = Download_thread(chooseresulation, downloadbutton)
        download_thread.start()

def start_check(self, QMessageBox, YouTube, urlretrieve, QPixmap, namelabel, videothumb,
                chooseresulation, checkvideo, videoaddress):
    # this function when a player hit the check button, fetchs downloadable items and pushes them into the combobox# this function when a player hit the check button, fetchs downloadable items and pushes them into the combobox

    videoAddressValue = videoaddress.text()

    if videoAddressValue == "":
        QMessageBox.warning(self, "Video address error", "Please paste your video address into the textbox"
                            , QMessageBox.Ok)

    else:

        class CheckIt(threading.Thread):
            def __init__(self, checkvideo, videoaddress):
                threading.Thread.__init__(self)
                self.checkvideo = checkvideo
                self.videoaddress = videoaddress

            def run(self):
                try:
                    self.checkvideo.setText("Checking")
                    self.checkvideo.setEnabled(False)
                    yt = YouTube(videoAddressValue)
                    yt.streams.desc()
                    allStreams = yt.streams.all()

                    # display video's name
                    videoTitle = yt.title

                    # display video's thumbnail
                    thumbnail = yt.thumbnail_url

                    for i in allStreams:
                        if str(i.audio_codec) != "None" and str(i.resolution) != "None":
                            tocombobox = str(i.resolution) + " " + str(i.mime_type) + " " + str(i.fps) + " " + str(
                                i.itag) + \
                                         " " + str(i.audio_codec)
                            chooseresulation.addItem(tocombobox)

                    namelabel.setText(videoTitle)
                    urlretrieve(thumbnail, "img.jpg")
                    thumb = QPixmap("img.jpg")
                    videothumb.setPixmap(thumb)
                    self.checkvideo.setText("Check Video")
                    self.checkvideo.setEnabled(True)

                except RegexMatchError:
                    self.videoaddress.setText("")
                    self.checkvideo.setText("Invalid Entry")
                    self.checkvideo.setEnabled(True)
                    time.sleep(1)
                    self.checkvideo.setText("Check Video")


        check_it = CheckIt(checkvideo, videoaddress)
        check_it.start()
