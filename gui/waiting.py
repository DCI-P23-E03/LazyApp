import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PyQt6.QtGui import QMovie, QPixmap
from PyQt6 import QtCore

def msg_wait():
    global msg
    msg = QMessageBox()
    msg.setIconPixmap(QPixmap('gui/loading_cat.gif').scaledToWidth(550))
    
    icon_label = msg.findChild(QLabel, "qt_msgboxex_icon_label")
    movie = QMovie('gui/loading_cat.gif')
    setattr(msg, 'icon_label', movie)
    icon_label.setMovie(movie)
    movie.start()

   # msg.setText("")
    msg.setWindowTitle("Just a minute...")
    msg.setModal(False)
    msg.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    msg_wait()
    sys.exit(app.exec())