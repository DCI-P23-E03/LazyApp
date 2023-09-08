from PyQt6 import QtCore, QtGui, QtWidgets
from Window_1_Start import Ui_Window_1_Start
from Window_2_Input import Ui_Window_2_Input
import sys


class Ui_Main_App_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Window_1_Start()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self.start_button_clicked)

    def start_button_clicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window_2_Input()
        self.ui.setupUi(self.window)
        self.hide()
        self.window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Ui_Main_App_Window()
    main_window.show()

    sys.exit(app.exec())
