import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
import pyjokes
#from PyQt6.QtGui import QMovie, QPixmap
#from PyQt6 import QtCore

def msg_wait(language):
    global msg
    msg = QMessageBox()
    msg.setGeometry(200,200,200,200)

    # picture option that was not working smoothly
    #   msg.setIconPixmap(QPixmap('gui/loading_cat.gif').scaledToWidth(550))
    
    #   icon_label = msg.findChild(QLabel, "qt_msgboxex_icon_label")
    #   movie = QMovie('gui/loading_cat.gif')
    #   setattr(msg, 'icon_label', movie)
    #i  con_label.setMovie(movie)
    #   movie.start()

    
    if language == "de":
        joke = pyjokes.get_joke("de", "all")
        msg.setText(joke)
        msg.setWindowTitle("Nur eine Minute...")
    else:
        joke = pyjokes.get_joke("en", "all")
        msg.setText(joke)
        msg.setWindowTitle("Just a minute...")
    msg.setModal(False)
    msg.show()

def msg_close():
    msg.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    msg_wait("en")
    sys.exit(app.exec())