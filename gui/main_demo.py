import sys
import PyPDF2
import threading
from PyQt6 import QtCore, QtGui, QtWidgets
from Window_1_Start import Ui_Window_1_Start
from Window_2_Input import Ui_Window_2_Input
from Window_3_JobAd_en import Ui_Window_3_JobAd_en
from Window_4_Output3 import Ui_Window_4_Output
from Window_5_Appl_letter import Ui_Window_5_Application_Letter
from Window_6_Cheat_Sheet import Ui_Window_6_Cheat_Sheet
from Window_7_cv_pointers import Ui_Window_7_cv_pointers
from Window_8_Goodbye_en import Ui_Window_8_Goodbye_en
from Window_9_Input_de import Ui_Window_9_Input_de
from Window_10_JobAd_de import Ui_Window_10_JobAd_de
from Window_11_Output_de import Ui_Window_11_Output_de
from Window_12_Appl_letter_de import Ui_Window_12_Application_Letter_de
from Window_13_Cheat_Sheet_de import Ui_Window_13_Cheat_Sheet_de
from Window_14_cv_pointers_de import Ui_Window_14_cv_pointers_de
from Window_15_Goodbye_de import Ui_Window_15_Goodbye_de
from PyQt6.QtGui import QTextDocument
from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtWidgets import QMessageBox
from datetime import datetime
from prompting import LetterPrompt, CheatSheetPrompt, CvPointersPrompt
from ai_example2_Class import ChatGPTChat
from waiting_gif import LoadingGif, waiting_window


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
            Ui_Window_8_Goodbye_en(),
            Ui_Window_9_Input_de(),
            Ui_Window_10_JobAd_de(),
            Ui_Window_11_Output_de(),
            Ui_Window_12_Application_Letter_de(),
            Ui_Window_13_Cheat_Sheet_de(),
            Ui_Window_14_cv_pointers_de(),
            Ui_Window_15_Goodbye_de()
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
        if hasattr(current_ui, 'button_nextToJobAd'): # Input Page 2, Page 9
            current_ui.button_nextToJobAd.clicked.connect(self.next_window_plus_inputPage)
        if hasattr(current_ui, 'next_button_4'): # Output Page 4, Page 11
            current_ui.next_button_4.clicked.connect(self.next_window_plus_checkboxes)
        if hasattr(current_ui, 'next_button'): # Page 1,3,5, 6, 7, 12, 13, 14
            current_ui.next_button.clicked.connect(self.next_window)


        # back buttons
        if hasattr(current_ui, 'back_button'):  # Input page
            current_ui.back_button.clicked.connect(self.prev_window)
        

        # back to the start for second application
        if hasattr(current_ui, 'start_button_2'):
            current_ui.start_button_2.clicked.connect(self.back_to_start)

        # exit button
        if hasattr(current_ui, 'exit_button'):
            current_ui.exit_button.clicked.connect(self.exit)

        # CV browser button
        if hasattr(current_ui, 'button_CV_browseFile'):  # Start Page 1
            current_ui.button_CV_browseFile.clicked.connect(self.cv_browseFile)
        

        # export application letter, cheat sheet and cv improvements to pdf button
        if hasattr(current_ui, 'export_button'):
            current_ui.export_button.clicked.connect(self.export_to_pdf)
        
        # display gpt output
        if (current_ui == self.ui_windows[4] or current_ui == self.ui_windows[11]) and letter_resp:
            current_ui.Appl_letter_space.setPlainText(letter_resp)
        if (current_ui == self.ui_windows[5] or current_ui == self.ui_windows[12]) and cheat_resp:
            current_ui.Cheat_Sheet_space.setPlainText(cheat_resp)
        if (current_ui == self.ui_windows[6] or current_ui == self.ui_windows[13]) and cv_improv_resp:
            current_ui.cv_pointers_space.setPlainText(cv_improv_resp)

    # Define function to go to the next window (including jumps)
    def next_window(self):
        current_ui = self.ui_windows[self.current_window]
        n = 1
        # getting the language information from first window
        if current_ui == self.ui_windows[0]:
            language = self.get_language()
            if language == "de":
                n = 8
        # getting the job_adv from the window
        if hasattr(current_ui, 'jobTextEdit'):
            global job_adv
            job_adv = current_ui.jobTextEdit.toPlainText()
            # print(job_adv)
        # starting at Checkbox Window - move over to right page
        if current_ui == self.ui_windows[3] or current_ui == self.ui_windows[10]:
            if not application_letter_checked and cheat_sheet_checked:
                n = 2
            elif not application_letter_checked and not cheat_sheet_checked:
                n = 3
        # starting at Application letter window - move over to CV Improvements or end
        if current_ui == self.ui_windows[4] or current_ui == self.ui_windows[11]:
            if not cheat_sheet_checked and cv_improvements_checked:
                n = 2
            elif not cheat_sheet_checked and not cv_improvements_checked:
                n = 3
        # start at Cheat Sheet window move over cv improvements to end        
        if (current_ui == self.ui_windows[5] or current_ui == self.ui_windows[12]) and not cv_improvements_checked:
                n = 2
        # if all boxes are checked n =1 and program moves one by one
        self.current_window = (self.current_window + n) % len(self.ui_windows)
        self.setup_current_window()


    # Define function to get language information from start page
    def get_language(self):
        '''grabs the language information from the start page'''
        current_ui = self.ui_windows[self.current_window]
        global language
        language = "en"
        if current_ui.language_deutsch.isChecked():
            language = "de"
        return language

    # Define function to browse for CV
    def cv_browseFile(self):
        global filepath
        filepath = QtWidgets.QFileDialog.getOpenFileName()[0]
        # print(filepath)
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
        # print(pdf_content)
        return cv


    # Define function to go to the next window and store date
    def next_window_plus_inputPage(self):
        '''stores the date when moving on to the next window'''
        current_ui = self.ui_windows[self.current_window]

        # starting date for new job
        global date
        date = current_ui.button_availibility_date.date()
        if date == datetime.today():
            if language == "de":
                date = "sofort"
            else: 
                date = "immediately"
        
        # Salary input, if empty or not filled in set to "appropriate"
        global salary
        salary = current_ui.textEdit_annuaSalary.toPlainText()
        if salary == "ANNUAL SALARY" or salary == "" or salary == "JAHRESGEHALT":
            if language == "de":
                salary = "angemessen"
            else:
                salary = "appropriate"
        # print(salary)

        # stores the state of radio buttons when clicking the next button
        global hours
        if current_ui.radioButton_fullTime.isChecked():
            if language == "de":
                hours = "Vollzeit"
            else:
                hours = "full-time"
        elif current_ui.radioButton_partTime.isChecked():
            if language == "de":
                hours = "Teilzeit"
            else:
                hours = "part-time"
        else:
            if language == "de":
                hours = "Vollzeit"
            else:
                hours = "full-time" # default option
                
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

        try:
            print(cv)
        except NameError:
            if language == "de":
                QMessageBox.warning(self, "Achtung", "Bitte lade einen CV hoch.")
            else:
                QMessageBox.warning(self, "Warning", "Please upload a CV.")
        else:
            self.next_window()

        return date, salary, hours, word_amount, ai_behaviour   

    # Define function to go to next window plus checkboxes
    def next_window_plus_checkboxes(self):
        '''stores the state of checkboxes when clicking the next button'''
        current_ui = self.ui_windows[self.current_window] 
        global application_letter_checked
        application_letter_checked = current_ui.checkBox_Application_letter.isChecked()
        global cheat_sheet_checked
        cheat_sheet_checked = current_ui.checkBox_Cheat_Sheet.isChecked()
        global cv_improvements_checked
        cv_improvements_checked = current_ui.checkBox_CV_Improvements.isChecked()
        # print(application_letter_checked)
        # print(cheat_sheet_checked)
        # print(cv_improvements_checked)
        if not application_letter_checked and not cheat_sheet_checked and not cv_improvements_checked:
            if language == "de":
                QMessageBox.warning(self, "Achtung", "Wähle mindestens eine option.")
            else:
                QMessageBox.warning(self, "Warning", "Please select at least one option.")
        else:
            # start waiting Widgets # gif is not shown here!!!
            
            #open waiting window
            #waitingwindow = QtWidgets.QMainWindow()
            #waiting = LoadingGif()
            #waiting.setupUi(waitingwindow)
            #waitingwindow.show()
            #waiting.startAnimation()
            print("AI is working on your request.")


            # create prompts
            self.instantiate_prompts()

            # let prompts run
            self.instantiate_ai()
            
            #waitingwindow.close()

            # move to next window
            self.next_window()
        return application_letter_checked, cheat_sheet_checked, cv_improvements_checked
    
    


    # instantiate Prompt Classes LetterPrompt, CheatSheetPrompt, CvPointersPrompt
    def instantiate_prompts(self):
        global letter
        letter = ""
        global cheat_sheet
        cheat_sheet = ""
        global cv_pointers
        cv_pointers = ""
        if application_letter_checked:
            letter_prompt = LetterPrompt(cv, job_adv , salary_expt = salary, availability = date, hours = hours, max_length = word_amount, language = language)
            letter = letter_prompt.prompt()
        if cheat_sheet_checked:
            cheat_sheet_prompt = CheatSheetPrompt(job_adv, language)
            # if not application_letter_checked:
            cheat_sheet = cheat_sheet_prompt.prompt()
            # else:
            #  cheat_sheet = cheat_sheet_prompt.follow_up()
        if cv_improvements_checked:
            cv_pointers_prompt = CvPointersPrompt(job_adv, language, cv)
            #if not application_letter_checked and not cheat_sheet_checked:
            cv_pointers = cv_pointers_prompt.prompt()
            #else:
               # cv_pointers = cv_pointers_prompt.follow_up()
        return letter, cheat_sheet, cv_pointers


    # pass prompts to chat gpt
    def instantiate_ai(self):
        chat_gpt = ChatGPTChat(temperature = ai_behaviour)
        global letter_resp
        letter_resp = ""
        global cheat_resp
        cheat_resp = ""
        global cv_improv_resp
        cv_improv_resp = ""


        # run prompts
        if letter:
            letter_resp = "".join(chat_gpt.chat_interface(letter))
        if cheat_sheet:
            cheat_resp = "".join(chat_gpt.chat_interface(cheat_sheet))
        if cv_pointers:
            cv_improv_resp = "".join(chat_gpt.chat_interface(cv_pointers))


        return letter_resp, cheat_resp, cv_improv_resp


    # Define function to export to pdf for Letter, CV Pointers, Cheat Sheet 
    def export_to_pdf(self):
        current_ui = self.ui_windows[self.current_window]
        if current_ui == self.ui_windows[4] or current_ui == self.ui_windows[11]:
            content = current_ui.Appl_letter_space.toPlainText()
        if current_ui == self.ui_windows[5] or current_ui == self.ui_windows[12]:
            content = current_ui.Cheat_Sheet_space.toPlainText()
        if current_ui == self.ui_windows[6] or current_ui == self.ui_windows[13]:
            content = current_ui.cv_pointers_space.toPlainText()
        # opening a file dialog to prompt the user to choose a location to save the PDF file
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
        n = 1
        # going back from CV Pointers
        if self.current_window == 8:
            n = 8
        if self.current_window == 6 or self.current_window == 13:
            if not cheat_sheet_checked and not application_letter_checked:
                n = 3
            elif not cheat_sheet_checked:
                n = 2
        if self.current_window == 5 or self.current_window == 12:
            if not application_letter_checked:
                n = 2     
        self.current_window = (self.current_window - n) % len(self.ui_windows)
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