from PyQt6 import QtCore, QtGui, QtWidgets
from Window_1_Start import Ui_Window_1_Start
from Window_2_Input import Ui_Window_2_Input

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Window 1
    Window_1_Start = QtWidgets.QMainWindow()
    ui = Ui_Window_1_Start()
    ui.setupUi(Window_1_Start)
    Window_1_Start.show()
    











    sys.exit(app.exec())