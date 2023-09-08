import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QMovie


class LoadingGif(object):
    def setupUi(self, FrontWindow):
        FrontWindow.setObjectName("FTwindow")
        FrontWindow.resize(550, 300)
        self.centralwidget = QtWidgets.QWidget(FrontWindow)
        self.centralwidget.setObjectName("waiting")
        self.centralwidget.setAutoFillBackground(False)

        # Label Create
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 25, 500, 200))
        self.label.setMinimumSize(QtCore.QSize(500, 250))
        self.label.setMaximumSize(QtCore.QSize(500, 250))
        self.label.setAutoFillBackground(False)

        self.label.setObjectName("wait")
        FrontWindow.setCentralWidget(self.centralwidget)

        # Loading the GIF
        self.movie = QMovie("loading_cat.gif")
        self.label.setMovie(self.movie)

        self.startAnimation()

    # Start Animation
    def startAnimation(self):
        self.movie.start()

    # Stop Animation (According to need)
    def stopAnimation(self):
        self.movie.stop()


def waiting_window():
    waitingwindow = QtWidgets.QMainWindow()
    waiting = LoadingGif()
    waiting.setupUi(waitingwindow)
    waitingwindow.show()
    waiting.startAnimation()
    print("AI is working on your request.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    demo = LoadingGif()
    demo.setupUi(window)
    window.show()

    # Start the animation after the window is visible
    demo.startAnimation()
    # time.sleep(4)
    # demo.stopAnimation()
    sys.exit(app.exec())
