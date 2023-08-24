import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from Window_1_Start import Ui_Window_1_Start
from Window_2_Input import Ui_Window_2_Input
from Window_3_JobAd_en import Ui_Window_3_JobAd_en
from Window_4_Output3 import Ui_Window_4_Output
from Window_5_Appl_letter import Ui_Window_5_Application_Letter
from Window_6_Cheat_Sheet import Ui_Window_6_Cheat_Sheet
from Window_7_cv_pointers import Ui_Window_7_cv_pointers
from Window_8_Goodbye_en import Ui_Window_8_Goodbye_en


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui_windows = [
            Ui_Window_1_Start(),
            Ui_Window_2_Input(),
            Ui_Window_3_JobAd_en(),
            Ui_Window_4_Output(),
            Ui_Window_5_Application_Letter(),
            Ui_Window_6_Cheat_Sheet(),
            Ui_Window_7_cv_pointers(),
            Ui_Window_8_Goodbye_en()
        ]
        self.current_window = 0

        self.setup_current_window()

    def setup_current_window(self):
        current_ui = self.ui_windows[self.current_window]
        current_ui.setupUi(self)

        # next buttons
        if hasattr(current_ui, 'start_button'):  # Start Page 1
            current_ui.start_button.clicked.connect(self.next_window)
        if hasattr(current_ui, 'button_nextToJobAd'): # Input Page 2
            current_ui.button_nextToJobAd.clicked.connect(self.next_window)
        if hasattr(current_ui, 'next_button_3'):      # JobAd Page 3
            current_ui.next_button_3.clicked.connect(self.next_window)
        if hasattr(current_ui, 'next_button_4'): # Output Page 4
            current_ui.next_button_4.clicked.connect(self.next_window)
        if hasattr(current_ui, 'Appl_letter_next_button'): # Appl Page 5
            current_ui.Appl_letter_next_button.clicked.connect(self.next_window)
        if hasattr(current_ui, 'Cheat_sheet_next_button'): # Cheat Sheet Page 6
            current_ui.Cheat_sheet_next_button.clicked.connect(self.next_window)
        if hasattr(current_ui, 'cv_pointers_next_button'): # CV Pointers Page 7
            current_ui.cv_pointers_next_button.clicked.connect(self.next_window)


        # back buttons
        if hasattr(current_ui, 'button_backToWelcomeWindow'):  # Input page
            current_ui.button_backToWelcomeWindow.clicked.connect(self.prev_window)
        if hasattr(current_ui, 'back_button_3'):  # Job Ad page
            current_ui.back_button_3.clicked.connect(self.prev_window)
        if hasattr(current_ui, 'back_button_4'): # Output Page 4
            current_ui.back_button_4.clicked.connect(self.prev_window)
        if hasattr(current_ui, 'Appl_letter_back_button'): #Output Page 5
            current_ui.Appl_letter_back_button.clicked.connect(self.prev_window)
        if hasattr(current_ui, 'Cheat_Sheet_back_button'): # Ouput Page 6
            current_ui.Cheat_Sheet_back_button.clicked.connect(self.prev_window)
        if hasattr(current_ui, 'cv_pointers_back_button'): # Output Page 7
            current_ui.cv_pointers_back_button.clicked.connect(self.prev_window)
        if hasattr(current_ui, 'start_button_2'): # Output Page 8
            current_ui.start_button_2.clicked.connect(self.prev_window)

        # back to the start for second application
        if hasattr(current_ui, 'start_button_2'):
            current_ui.start_button_2.clicked.connect(self.back_to_start)

        # exit button
        if hasattr(current_ui, 'exit_button'):
            current_ui.exit_button.clicked.connect(self.exit)

        

    def next_window(self):
        self.current_window = (self.current_window + 1) % len(self.ui_windows)
        self.setup_current_window()


    def prev_window(self):
        self.current_window = (self.current_window - 1) % len(self.ui_windows)
        self.setup_current_window()


    def back_to_start(self):
        self.current_window = 0
        self.setup_current_window()


    def exit(self):
        sys.exit(app.exec())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
