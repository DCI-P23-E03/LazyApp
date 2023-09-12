import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox


def msg_wait(language):
    '''Open Message Box''' 

    global msg
    msg = QMessageBox()
    msg.setGeometry(200,200,150,150)
    if language == "de": 
        #msg.setText("Geduld.")
        msg.setWindowTitle("Nur eine Minute...")
    else:
        #msg.setText("Patience.")
        msg.setWindowTitle("Just a minute...")
    msg.show()

def msg_hide():
    msg.hide()
def msg_close():
    '''Close Message Box'''    
    msg.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    msg_wait("en")

    sys.exit(app.exec())