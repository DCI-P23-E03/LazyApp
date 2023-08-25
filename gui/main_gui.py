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
from PyQt6.QtGui import QTextDocument
from PyQt6.QtPrintSupport import QPrinter


# Create class for the main window
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a list of all the windows
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

        # Set the default value of current window to 0
        self.current_window = 0

        # Setup the current window
        self.setup_current_window()

    # Define function to setup the current window
    def setup_current_window(self):
        # Set the central widget of the window to the current window
        current_ui = self.ui_windows[self.current_window]
        current_ui.setupUi(self)

        # next buttons
        if hasattr(current_ui, 'start_button'):  # Start Page 1
            current_ui.start_button.clicked.connect(self.next_window)
        if hasattr(current_ui, 'button_nextToJobAd'): # Input Page 2
            current_ui.button_nextToJobAd.clicked.connect(self.next_window_plus_inputPage)
        if hasattr(current_ui, 'next_button_3') and hasattr(current_ui, 'jobTextEdit'): # JobAd Page 3
            current_ui.next_button_3.clicked.connect(self.next_window_plus_input)
        if hasattr(current_ui, 'next_button_4'): # Output Page 4
            current_ui.next_button_4.clicked.connect(self.next_window_plus_checkboxes)
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

        # CV browser button
        if hasattr(current_ui, 'button_CV_browseFile'):  # Start Page 1
            current_ui.button_CV_browseFile.clicked.connect(self.cv_browseFile)
        
        # Radio Buttons for Availibility of Part-Time and Full-Time
        if hasattr(current_ui, 'radioButton_fullTime'):
            current_ui.radioButton_fullTime.clicked.connect(self.updateAvailibility)
        if hasattr(current_ui, 'radioButton_partTime'):
            current_ui.radioButton_partTime.clicked.connect(self.updateAvailibility)


        # Word Amount
        if hasattr(current_ui, 'slider_wordAmount'):
            current_ui.slider_wordAmount.valueChanged.connect(self.updateWordAmount)

        if hasattr(current_ui, 'slider_AiBehaviour'):
            current_ui.slider_AiBehaviour.valueChanged.connect(self.update_Ai_Beahviour)

        # export application letter to pdf button
        if hasattr(current_ui, 'Appl_letter_export_button'):
            current_ui.Appl_letter_export_button.clicked.connect(self.export_application_letter_to_pdf)

        # export cheat sheet to pdf button
        if hasattr(current_ui, 'Cheat_Sheet_export_button'):
            current_ui.Cheat_Sheet_export_button.clicked.connect(self.export_cheat_sheet_to_pdf)

        # export cv pointers to pdf button
        if hasattr(current_ui, 'cv_pointers_export_button'):
            current_ui.cv_pointers_export_button.clicked.connect(self.export_cv_pointers_to_pdf)



    # Define function to go to the next window
    def next_window(self):
        self.current_window = (self.current_window + 1) % len(self.ui_windows)
        self.setup_current_window()
    
    
    # Define function to go to the next window and store input
    def next_window_plus_input(self):
        '''stores the content of input field in variable before moving on to the next window'''
        current_ui = self.ui_windows[self.current_window]
        job_adv = current_ui.jobTextEdit.toPlainText()
        print(job_adv)
        self.next_window()
        return job_adv


    # Define function to go to the next window and store date
    def next_window_plus_inputPage(self):
        '''stores the date when moving on to the next window'''
        current_ui = self.ui_windows[self.current_window]
        date = current_ui.button_availibility_date.date()
        salary = int(current_ui.textEdit_annuaSalary.toPlainText())
        self.next_window()
        return date, print(date), salary, print(salary)
    

    # Define function to go to next window plus checkboxes
    def next_window_plus_checkboxes(self):
        '''stores the state of checkboxes when clicking the next button'''
        current_ui = self.ui_windows[self.current_window]
        application_letter_checked = current_ui.checkBox_Application_letter.isChecked()
        cheat_sheet_checked = current_ui.checkBox_Cheat_Sheet.isChecked()
        cv_improvements_checked = current_ui.checkBox_CV_Improvements.isChecked()
        print(application_letter_checked)
        print(cheat_sheet_checked)
        print(cv_improvements_checked)
        self.next_window()
        return application_letter_checked, cheat_sheet_checked, cv_improvements_checked
    
        #self.checkBox_Cheat_Sheet.stateChanged.connect(self.updateCheatSheet)

    # Define function to check Radio Buttons for Availibility of Part-Time and Full-Time
    def updateAvailibility(self):
        '''stores the state of radio buttons when clicking the next button'''
        availibility = None
        current_ui = self.ui_windows[self.current_window]
        if current_ui.radioButton_fullTime.isChecked():
            print("Full-Time")
            availibility = "Full-Time"
            return availibility
        elif current_ui.radioButton_partTime.isChecked():
            print("Part-Time")
            availibility = "Part-Time"
            return availibility
        else:
            print("None")
            availibility = "None"
            return availibility

    # Define function to check Word Amount
    def updateWordAmount(self):
        current_ui = self.ui_windows[self.current_window]
        word_amount = current_ui.slider_wordAmount.value()
        # round to nearest 50 words
        word_amount = round(word_amount/25)*25
        print(word_amount)
        return word_amount
    
    # Define function to check Ai Behaviour
    def update_Ai_Beahviour(self):
        current_ui = self.ui_windows[self.current_window]
        ai_behaviour = float(current_ui.slider_AiBehaviour.value()/100)
        #round to nearest 0.1
        #ai_behaviour = print('%f' % ai_behaviour).rstrip('0').rstrip('.')
        ai_behaviour = format(round(ai_behaviour/0.1)*0.1, '.1f')
        # get rid of trailing zeros
        print(ai_behaviour)
        return ai_behaviour





    # Define function to export application letter to pdf
    def export_application_letter_to_pdf(self):
        current_ui = self.ui_windows[self.current_window]
        if hasattr(current_ui, 'Appl_letter_export_button'):
            content = current_ui.Appl_letter_space.toPlainText()
        #opening a file dialog to prompt the user to choose a location to save the PDF file
        if content:
            filePath, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Application Letter as PDF", "", "PDF Files (*.pdf);;All Files (*)")
            if filePath:
                if not filePath.lower().endswith('.pdf'):
                    filePath += '.pdf'
                doc = QTextDocument()
                doc.setPlainText(content)
                printer = QPrinter()
                printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
                printer.setOutputFileName(filePath)
                doc.print(printer)
                print("Application letter exported as PDF.")


    # Define function to export cheat sheet to pdf
    def export_cheat_sheet_to_pdf(self):
        current_ui = self.ui_windows[self.current_window]
        if hasattr(current_ui, 'Cheat_Sheet_export_button'):
            content = current_ui.Cheat_Sheet_space.toPlainText()
        #opening a file dialog to prompt the user to choose a location to save the PDF file
        if content:
            filePath, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Cheat sheet as PDF", "", "PDF Files (*.pdf);;All Files (*)")
            if filePath:
                if not filePath.lower().endswith('.pdf'):
                    filePath += '.pdf'
                doc = QTextDocument()
                doc.setPlainText(content)
                printer = QPrinter()
                printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
                printer.setOutputFileName(filePath)
                doc.print(printer)
                print("Cheat sheet exported as PDF.")


    # Define function to export cv pointers to pdf
    def export_cv_pointers_to_pdf(self):
        current_ui = self.ui_windows[self.current_window]
        if hasattr(current_ui, 'cv_pointers_export_button'):
            content = current_ui.cv_pointers_space.toPlainText()
        #opening a file dialog to prompt the user to choose a location to save the PDF file
        if content:
            filePath, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save cv pointers as PDF", "", "PDF Files (*.pdf);;All Files (*)")
            if filePath:
                if not filePath.lower().endswith('.pdf'):
                    filePath += '.pdf'
                doc = QTextDocument()
                doc.setPlainText(content)
                printer = QPrinter()
                printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
                printer.setOutputFileName(filePath)
                doc.print(printer)
                print("cv pointers exported as PDF.")


    # Define function to go to the previous window
    def prev_window(self):
        self.current_window = (self.current_window - 1) % len(self.ui_windows)
        self.setup_current_window()

    # Define function to go back to the start
    def back_to_start(self):
        self.current_window = 0
        self.setup_current_window()

    # Define function to exit the application
    def exit(self):
        sys.exit(app.exec())

    # Define function to browse for CV
    def cv_browseFile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()
        return filename #, print(filename)

# Define function to run the application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

   

# collect variables from different parts to run Prompt
    sys.exit(app.exec())