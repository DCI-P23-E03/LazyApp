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
from PyQt6.QtWidgets import QMessageBox
from datetime import datetime
import PyPDF2
from prompting import LetterPrompt, CheatSheetPrompt, CvPointersPrompt
#from ai_example2_Class import ChatGPTChat


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
        
       


        # export application letter to pdf button
        if hasattr(current_ui, 'Appl_letter_export_button'):
            current_ui.Appl_letter_export_button.clicked.connect(self.export_to_pdf)

        # export cheat sheet to pdf button
        if hasattr(current_ui, 'Cheat_Sheet_export_button'):
            current_ui.Cheat_Sheet_export_button.clicked.connect(self.export_to_pdf)

        # export cv pointers to pdf button
        if hasattr(current_ui, 'cv_pointers_export_button'):
            current_ui.cv_pointers_export_button.clicked.connect(self.export_to_pdf)



    # Define function to go to the next window
    def next_window(self):
        self.current_window = (self.current_window + 1) % len(self.ui_windows)
        self.setup_current_window()
    
    
    # Define function to go to the next window 4 and store input
    def next_window_plus_input(self):
        '''stores the content of input field in variable before moving on to the next window'''
        current_ui = self.ui_windows[self.current_window]
        global job_adv
        job_adv = current_ui.jobTextEdit.toPlainText()
        print(job_adv)
        self.next_window()
        return job_adv

    # Define function to browse for CV
    def cv_browseFile(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName()[0]
        if not filepath:
            QtWidgets.QMessageBox.warning(self, "Missing Information", "Please select a CV.")
        print(filepath)
        pdf_file = open(filepath, 'rb') # open PDF file

        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to store the content
        global cv
        cv = ""

        # Loop through each page and extract text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            cv += page.extract_text()

        # Close the PDF file
        pdf_file.close()
        # Print or do something with the extracted content
        #print(pdf_content)
        return cv

    # Define function to go to the next window and store date
    def next_window_plus_inputPage(self):
        '''stores the date when moving on to the next window'''
        current_ui = self.ui_windows[self.current_window]
        #showing a pop up window if user did not fill the required info
        if current_ui.button_availibility_date.date() == datetime.today()  or not current_ui.radioButton_fullTime.isChecked() and not current_ui.radioButton_partTime.isChecked():
            QMessageBox.warning(self, "Warning", "Please fill in all the required information.")
        else:
            self.next_window

        # starting date for new job
        global date
        date = current_ui.button_availibility_date.date()
        if date == datetime.today():
            date = "immediately"
        print(date)

        #Salary input, if empty or not filled in set to "appropriate"
        global salary
        salary = current_ui.textEdit_annuaSalary.toPlainText()
        if salary == "ANNUAL SALARY" or salary == "":
            salary = "appropriate"
        # print(salary)
        # stores the state of radio buttons when clicking the next button
        global hours
        if current_ui.radioButton_fullTime.isChecked():
            hours = "full-time"
        elif current_ui.radioButton_partTime.isChecked():
            hours = "part-time"
        else:
            hours = "full-time" # default option
        # print(availability)
        global word_amount
        word_amount = current_ui.slider_wordAmount.value()
        # round to nearest 50 words
        word_amount = round(word_amount/25)*25
        # print(word_amount)
        global ai_behaviour
        ai_behaviour = float(current_ui.slider_AiBehaviour.value()/100)
        # round to nearest 0.1
        ai_behaviour = format(round(ai_behaviour/0.1)*0.1, '.1f')
        ai_behaviour = float(ai_behaviour)
        # get rid of trailing zeros
        print(ai_behaviour)
        self.next_window()

        return date, salary, hours, word_amount, ai_behaviour
      

    # Define function to go to next window plus checkboxes
    def next_window_plus_checkboxes(self):
        '''stores the state of checkboxes when clicking the next button'''
        current_ui = self.ui_windows[self.current_window]
        #showing a pop up window if any of the checkboxes is not checked
        if not current_ui.checkBox_Application_letter.isChecked() and not current_ui.checkBox_Cheat_Sheet.isChecked() and not current_ui.checkBox_CV_Improvements.isChecked():
            QMessageBox.warning(self, "Warning", "Please select at least one option.")
        
        else:
            self.next_window
        
        global application_letter_checked
        application_letter_checked = current_ui.checkBox_Application_letter.isChecked()
        global cheat_sheet_checked
        cheat_sheet_checked = current_ui.checkBox_Cheat_Sheet.isChecked()
        global cv_improvements_checked
        cv_improvements_checked = current_ui.checkBox_CV_Improvements.isChecked()
        # print(application_letter_checked)
        # print(cheat_sheet_checked)
        # print(cv_improvements_checked)
        self.instantiate_prompts()
        # self.instantiate_ai()
        self.next_window()
        return application_letter_checked, cheat_sheet_checked, cv_improvements_checked

    # instantiate Prompt Classes LetterPrompt, CheatSheetPrompt, CvPointersPrompt
    def instantiate_prompts(self):
        global letter
        letter = ""
        global cheat_sheet
        cheat_sheet = ""
        global cv_pointers
        cv_pointers =""
        if application_letter_checked:
            letter_prompt = LetterPrompt(cv, job_adv , salary_expt = salary, availability = date, hours = hours, max_length = word_amount, language = "en")
            letter = letter_prompt.prompt()
        if cheat_sheet_checked:
            cheat_sheet_prompt = CheatSheetPrompt(job_adv, language="en")
            if not application_letter_checked:
                cheat_sheet = cheat_sheet_prompt.prompt()
            else:
                cheat_sheet = cheat_sheet_prompt.follow_up()
        if cv_improvements_checked:
            cv_pointers_prompt = CvPointersPrompt(job_adv, cv, language="en") 
            if not application_letter_checked and not cheat_sheet_checked:
                cv_pointers = cv_pointers_prompt.prompt()
            else:
                cv_pointers = cv_pointers_prompt.follow_up()
        global prompts
        #prompts = [letter, cheat_sheet, cv_pointers]
        prompts = letter + cheat_sheet + cv_pointers
        print(prompts)
        return prompts
    
    # pass prompts to chat gpt
    def instantiate_ai(self):
        chat_gpt = ChatGPTChat(temperature = ai_behaviour)
        chat_gpt.chat_interface(prompts)
   
    # Define function to export to pdf for Letter, CV Pointers, Cheat Sheet 
    def export_to_pdf(self):
        current_ui = self.ui_windows[self.current_window]
        if hasattr(current_ui, 'Appl_letter_export_button'):
            content = current_ui.Appl_letter_space.toPlainText()
        if hasattr(current_ui, 'cv_pointers_export_button'):
            content = current_ui.cv_pointers_space.toPlainText()
        elif hasattr(current_ui, 'Cheat_Sheet_export_button'):
            content = current_ui.Cheat_Sheet_space.toPlainText()
        #opening a file dialog to prompt the user to choose a location to save the PDF file
        if content:
            filePath, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save as PDF", "", "PDF Files (*.pdf);;All Files (*)")
            if filePath:
                if not filePath.lower().endswith('.pdf'):
                    filePath += '.pdf'
                doc = QTextDocument()
                doc.setPlainText(content)
                printer = QPrinter()
                printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
                printer.setOutputFileName(filePath)
                doc.print(printer)
                print("Exported as PDF.")


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


# Define function to run the application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())