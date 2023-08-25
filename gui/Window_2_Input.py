from PyQt6 import QtCore, QtGui, QtWidgets
import Window_1_Start
import Window_3_JobAd_en
#from main_gui import cv_browsefile


class Ui_Window_2_Input(object):
    
    def setupUi(self, Window_2_Input):
        Window_2_Input.setObjectName("Window_2_Input")
        Window_2_Input.resize(1000, 800)
        Window_2_Input.setStyleSheet("background-color: rgb(220, 138, 221);")
        self.centralwidget = QtWidgets.QWidget(parent=Window_2_Input)
        self.centralwidget.setObjectName("centralwidget")

        # LABEL FIRST THINGS FIRST
        self.text_FirstThingFirst = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.text_FirstThingFirst.setGeometry(QtCore.QRect(0, 50, 1000, 60))
        self.text_FirstThingFirst.setAutoFillBackground(True)
        self.text_FirstThingFirst.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_FirstThingFirst.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.text_FirstThingFirst.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.text_FirstThingFirst.setLineWidth(0)
        self.text_FirstThingFirst.setObjectName("text_FirstThingFirst")
        
        # NEXT BUTTON
        self.button_nextToJobAd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_nextToJobAd.setGeometry(QtCore.QRect(650, 705, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.button_nextToJobAd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_nextToJobAd.setGeometry(QtCore.QRect(650, 705, 200, 50))
        self.button_nextToJobAd.setFont(font)
        self.button_nextToJobAd.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_nextToJobAd.setObjectName("button_nextToJobAd")

        # BACK BUTTON
        self.button_backToWelcomeWindow = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_backToWelcomeWindow.setGeometry(QtCore.QRect(150, 705, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.button_backToWelcomeWindow.setFont(font)
        self.button_backToWelcomeWindow.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_backToWelcomeWindow.setObjectName("button_backToWelcomeWindow")
        
        # LABEL WORD AMOUNT
        self.label_wordAmount_251 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_wordAmount_251.setGeometry(QtCore.QRect(600, 420, 31, 17))
        self.label_wordAmount_251.setObjectName("label_wordAmount_251")
        
        # SLIDER WORD AMOUNT values 250-400 in stepsof 50
        self.slider_wordAmount = QtWidgets.QSlider(parent=self.centralwidget)
        self.slider_wordAmount.setGeometry(QtCore.QRect(430, 420, 160, 16))
        self.slider_wordAmount.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_wordAmount.setObjectName("slider_wordAmount")
        self.slider_wordAmount.setMinimum(250)
        self.slider_wordAmount.setMaximum(400)
        self.slider_wordAmount.setSingleStep(25)
        self.slider_wordAmount.setValue(325)
        
        # TEXT EDIT ANNUAL SALARY
        self.textEdit_annuaSalary = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_annuaSalary.setGeometry(QtCore.QRect(340, 340, 341, 31))
        self.textEdit_annuaSalary.setStyleSheet("background-color: rgb(255, 255, 255);\n""")
        self.textEdit_annuaSalary.setObjectName("textEdit_annuaSalary")
        
        # LABEL AI BEHAVIOUR
        self.label_AiBehaviour_rational = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_AiBehaviour_rational.setGeometry(QtCore.QRect(350, 480, 81, 20))
        self.label_AiBehaviour_rational.setObjectName("label_AiBehaviour_rational")
        
        # LABEL WORD AMOUNT
        self.label_wordAmount_250 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_wordAmount_250.setGeometry(QtCore.QRect(400, 420, 31, 17))
        self.label_wordAmount_250.setObjectName("label_wordAmount_250")
        self.label_wordAmount = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_wordAmount.setGeometry(QtCore.QRect(480, 400, 61, 20))
        self.label_wordAmount.setObjectName("label_wordAmount")
        
        # SLIDER AI BEHAVIOUR
        self.slider_AiBehaviour = QtWidgets.QSlider(parent=self.centralwidget)
        self.slider_AiBehaviour.setGeometry(QtCore.QRect(430, 480, 160, 20))
        self.slider_AiBehaviour.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_AiBehaviour.setObjectName("slider_AiBehaviour")
        self.label_AiBehaviour = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_AiBehaviour.setGeometry(QtCore.QRect(460, 460, 101, 20))
        self.label_AiBehaviour.setObjectName("label_AiBehaviour")
        self.slider_AiBehaviour.setMinimum(10)
        self.slider_AiBehaviour.setMaximum(90)
        self.slider_AiBehaviour.setSingleStep(10)
        self.slider_AiBehaviour.setValue(50)

        # CV BROSWER BUTTON
        self.button_CV_browseFile = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_CV_browseFile.setGeometry(QtCore.QRect(420, 200, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.button_CV_browseFile.setFont(font)
        self.button_CV_browseFile.setObjectName("button_CV_browseFile")

        # DATE EDIT AVAILABILITY and set date to today
        self.button_availibility_date = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.button_availibility_date.setGeometry(QtCore.QRect(520, 260, 121, 26))
        self.button_availibility_date.setStyleSheet("color: rgb(220, 138, 221); background-color: rgb(255, 255, 255);")
        self.button_availibility_date.setObjectName("button_availibility_date")
        self.button_availibility_date.setDate(QtCore.QDate.currentDate()) # set date to today

        # LABEL AI BEHAVIOUR CREATIVE
        self.label_AiBehaviour_creative = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_AiBehaviour_creative.setGeometry(QtCore.QRect(600, 480, 71, 17))
        self.label_AiBehaviour_creative.setObjectName("label_AiBehaviour_creative")
        
        # LABEL AVAILABILITY
        self.label_availabilty = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_availabilty.setGeometry(QtCore.QRect(400, 260, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_availabilty.setFont(font)
        self.label_availabilty.setObjectName("label_availabilty")
        
        # RADIO BUTTON PART TIME
        self.radioButton_partTime = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_partTime.setGeometry(QtCore.QRect(520, 290, 112, 23))
        self.radioButton_partTime.setObjectName("radioButton_partTime")

        # RADIO BUTTON FULL TIME
        self.radioButton_fullTime = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_fullTime.setGeometry(QtCore.QRect(400, 290, 112, 23))
        self.radioButton_fullTime.setObjectName("radioButton_fullTime")
        
        Window_2_Input.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Window_2_Input)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        Window_2_Input.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Window_2_Input)
        self.statusbar.setObjectName("statusbar")
        Window_2_Input.setStatusBar(self.statusbar)

        self.retranslateUi(Window_2_Input)
        QtCore.QMetaObject.connectSlotsByName(Window_2_Input)

    def retranslateUi(self, Window_2_Input):
        _translate = QtCore.QCoreApplication.translate
        Window_2_Input.setWindowTitle(_translate("Window_2_Input", "LazyApp"))
        self.text_FirstThingFirst.setHtml(_translate("Window_2_Input", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">First things first</span></p></body></html>"))
        self.button_nextToJobAd.setText(_translate("Window_2_Input", "NEXT ->"))
        self.button_backToWelcomeWindow.setText(_translate("Window_2_Input", "<- BACK"))
        self.label_wordAmount_251.setText(_translate("Window_2_Input", "400"))
        self.textEdit_annuaSalary.setHtml(_translate("Window_2_Input", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"    
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#dc8add;\">ANNUAL SALARY</span></p></body></html>"))
        self.label_AiBehaviour_rational.setText(_translate("Window_2_Input", "RATIONAL"))
        self.radioButton_fullTime.setText(_translate("Window_2_Input", "FULL-TIME"))
        self.label_wordAmount_250.setText(_translate("Window_2_Input", "250"))
        self.label_wordAmount.setText(_translate("Window_2_Input", "WORDS"))
        self.label_AiBehaviour.setText(_translate("Window_2_Input", "AI BEHAVIOUR"))
        self.button_CV_browseFile.setText(_translate("Window_2_Input", "CV"))
        self.label_AiBehaviour_creative.setText(_translate("Window_2_Input", "CREATIVE"))
        self.label_availabilty.setText(_translate("Window_2_Input", "AVAILABILITY"))
        self.radioButton_partTime.setText(_translate("Window_2_Input", "PART-TIME"))

    #def back and forth buttons
    def next_to_jobad_clicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Window_3_JobAd_en.Ui_Window_3_JobAd_en()
        self.ui.setupUi(self.window)
        #Window_2_Input.hide()
        self.window.show()
    
    # Define function to go back to welcome window
    def back_to_welcome_clicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Window_1_Start.Ui_Window_1_Start()
        self.ui.setupUi(self.window)
        #Window_2_Input.hide()
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window_2_Input = QtWidgets.QMainWindow()
    ui = Ui_Window_2_Input()
    ui.setupUi(Window_2_Input)
    Window_2_Input.show()
    sys.exit(app.exec())