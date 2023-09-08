import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PyQt6.QtGui import QMovie, QPixmap
from PyQt6 import QtCore

def msg_wait(language):
    global msg
    msg = QMessageBox()
    msg.setGeometry(200,200,200,200)
    #msg.setIconPixmap(QPixmap('gui/loading_cat.gif').scaledToWidth(550))
    
   # icon_label = msg.findChild(QLabel, "qt_msgboxex_icon_label")
    #movie = QMovie('gui/loading_cat.gif')
    #setattr(msg, 'icon_label', movie)
    #icon_label.setMovie(movie)
    #movie.start()
    if language == "de":
        msg.setText("Die KI arbeitet, ein bisschen Geduld bitte.")
        msg.setWindowTitle("Nur eine Minute...")
    else:
        msg.setText("AI is working really hard on your request")
        msg.setWindowTitle("Just a minute...")
    msg.setModal(False)
    msg.show()

def msg_close():
    msg.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    msg_wait("de")
    sys.exit(app.exec())