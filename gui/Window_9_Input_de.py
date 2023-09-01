from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Window_9_Input_de(object):
    
    def setupUi(self, Window_9_Input_de):
        Window_9_Input_de.setObjectName("Window_9_Input_de")
        Window_9_Input_de.resize(1000, 800)
        Window_9_Input_de.setStyleSheet("background-color: rgb(67,110,238);")
        self.centralwidget = QtWidgets.QWidget(parent=Window_9_Input_de)
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
        self.back_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(150, 705, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.back_button.setObjectName("back_button")
        
        # LABEL WORD AMOUNT
        self.label_wordAmount_251 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_wordAmount_251.setGeometry(QtCore.QRect(600, 420, 31, 17))
        self.label_wordAmount_251.setObjectName("label_wordAmount_251")
        self.label_wordAmount_251.setStyleSheet("color: rgb(255, 255, 255);")
        
        # SLIDER WORD AMOUNT values 250-400 in stepsof 25
        self.slider_wordAmount = QtWidgets.QSlider(parent=self.centralwidget)
        self.slider_wordAmount.setGeometry(QtCore.QRect(430, 420, 160, 16))
        self.slider_wordAmount.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_wordAmount.setObjectName("slider_wordAmount")
        self.slider_wordAmount.setStyleSheet("color: rgb(255, 255, 255);")
        self.slider_wordAmount.setMinimum(250)
        self.slider_wordAmount.setMaximum(400)
        self.slider_wordAmount.setSingleStep(25)
        self.slider_wordAmount.setValue(350)
        
        
        # TEXT EDIT ANNUAL SALARY
        self.textEdit_annuaSalary = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_annuaSalary.setGeometry(QtCore.QRect(340, 340, 341, 31))
        self.textEdit_annuaSalary.setStyleSheet("background-color: rgb(255, 255, 255);\n""font: 12pt \"Ubuntu\";\n""\n""color: rgb(67,110,238);")
        self.textEdit_annuaSalary.setObjectName("textEdit_annuaSalary")
        self.textEdit_annuaSalary.setToolTip("Trage hier das Gehalt deiner Träume ein.")
        
        # LABEL AI BEHAVIOUR
        self.label_AiBehaviour_rational = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_AiBehaviour_rational.setGeometry(QtCore.QRect(360, 480, 81, 20))
        self.label_AiBehaviour_rational.setObjectName("label_AiBehaviour_rational")
        self.label_AiBehaviour_rational.setStyleSheet("color: rgb(255, 255, 255);")
        
        # LABEL WORD AMOUNT
        self.label_wordAmount_250 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_wordAmount_250.setGeometry(QtCore.QRect(400, 420, 31, 17))
        self.label_wordAmount_250.setObjectName("label_wordAmount_250")
        self.label_wordAmount = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_wordAmount.setGeometry(QtCore.QRect(480, 400, 61, 20))
        self.label_wordAmount.setObjectName("label_wordAmount")
        self.label_wordAmount_250.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_wordAmount.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_wordAmount.setToolTip("Bestimmt die Länge des Anschreibens.")
    
        
        # SLIDER AI BEHAVIOUR
        self.slider_AiBehaviour = QtWidgets.QSlider(parent=self.centralwidget)
        self.slider_AiBehaviour.setGeometry(QtCore.QRect(430, 480, 160, 20))
        self.slider_AiBehaviour.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_AiBehaviour.setObjectName("slider_AiBehaviour")
        self.label_AiBehaviour = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_AiBehaviour.setGeometry(QtCore.QRect(460, 460, 101, 20))
        self.label_AiBehaviour.setObjectName("label_AiBehaviour")
        self.label_AiBehaviour.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_AiBehaviour.setToolTip("Bestimmt wie kreativ oder rational die AI agiert.")
        self.slider_AiBehaviour.setMinimum(10)
        self.slider_AiBehaviour.setMaximum(90)
        self.slider_AiBehaviour.setSingleStep(10)
        self.slider_AiBehaviour.setValue(50)
        self.slider_AiBehaviour.setStyleSheet("color: rgb(255, 255, 255);")

        # CV BROWSER BUTTON
        self.button_CV_browseFile = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_CV_browseFile.setGeometry(QtCore.QRect(420, 200, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.button_CV_browseFile.setFont(font)
        self.button_CV_browseFile.setObjectName("button_CV_browseFile")
        self.button_CV_browseFile.setStyleSheet("color: rgb(255, 255, 255);")

        # DATE EDIT AVAILABILITY and set date to today
        self.button_availibility_date = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.button_availibility_date.setGeometry(QtCore.QRect(550, 260, 121, 26))
        self.button_availibility_date.setStyleSheet("color: rgb(67,110,238); background-color: rgb(255, 255, 255);")
        self.button_availibility_date.setObjectName("button_availibility_date")
        self.button_availibility_date.setCalendarPopup(True)  # Enable calendar popup
        self.button_availibility_date.setDate(QtCore.QDate.currentDate()) # set date to today
    

        # LABEL AI BEHAVIOUR CREATIVE
        self.label_AiBehaviour_creative = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_AiBehaviour_creative.setGeometry(QtCore.QRect(600, 480, 71, 17))
        self.label_AiBehaviour_creative.setObjectName("label_AiBehaviour_creative")
        self.label_AiBehaviour_creative.setStyleSheet("color: rgb(255, 255, 255);")
        
        # LABEL AVAILABILITY
        self.label_availabilty = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_availabilty.setGeometry(QtCore.QRect(350, 260, 200, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_availabilty.setFont(font)
        self.label_availabilty.setObjectName("label_availabilty")
        self.label_availabilty.setStyleSheet("color: rgb(255, 255, 255);")
        
        # RADIO BUTTON PART TIME
        self.radioButton_partTime = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_partTime.setGeometry(QtCore.QRect(520, 290, 112, 23))
        self.radioButton_partTime.setObjectName("radioButton_partTime")
        self.radioButton_partTime.setStyleSheet("color: rgb(255, 255, 255);")

        # RADIO BUTTON FULL TIME
        self.radioButton_fullTime = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_fullTime.setGeometry(QtCore.QRect(400, 290, 112, 23))
        self.radioButton_fullTime.setObjectName("radioButton_fullTime")
        self.radioButton_fullTime.setStyleSheet("color: rgb(255, 255, 255);")
        
        Window_9_Input_de.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Window_9_Input_de)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        Window_9_Input_de.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Window_9_Input_de)
        self.statusbar.setObjectName("statusbar")
        Window_9_Input_de.setStatusBar(self.statusbar)

        self.retranslateUi(Window_9_Input_de)
        QtCore.QMetaObject.connectSlotsByName(Window_9_Input_de)

    def retranslateUi(self, Window_9_Input_de):
        _translate = QtCore.QCoreApplication.translate
        Window_9_Input_de.setWindowTitle(_translate("Window_9_Input_de", "LazyApp"))
        self.text_FirstThingFirst.setHtml(_translate("Window_9_Input_de", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">Alles der Reihe nach:</span></p></body></html>"))
        self.button_nextToJobAd.setText(_translate("Window_9_Input_de", "VOR ->"))
        self.back_button.setText(_translate("Window_9_Input_de", "<- ZURÜCK"))
        self.label_wordAmount_251.setText(_translate("Window_9_Input_de", "400"))
        self.textEdit_annuaSalary.setHtml(_translate("Window_9_Input_de", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"    
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#436eee;\">JAHRESGEHALT</span></p></body></html>"))
        self.label_AiBehaviour_rational.setText(_translate("Window_9_Input_de", "RATIONAL"))
        self.radioButton_fullTime.setText(_translate("Window_9_Input_de", "VOLLZEIT"))
        self.label_wordAmount_250.setText(_translate("Window_9_Input_de", "250"))
        self.label_wordAmount.setText(_translate("Window_9_Input_de", "WÖRTER"))
        self.label_AiBehaviour.setText(_translate("Window_9_Input_de", "KI VERHALTEN"))
        self.button_CV_browseFile.setText(_translate("Window_9_Input_de", "CV"))
        self.label_AiBehaviour_creative.setText(_translate("Window_9_Input_de", "KREATIV"))
        self.label_availabilty.setText(_translate("Window_9_Input_de", "VERFÜGBARKEIT"))
        self.radioButton_partTime.setText(_translate("Window_9_Input_de", "TEILZEIT"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window_9_Input_de = QtWidgets.QMainWindow()
    ui = Ui_Window_9_Input_de()
    ui.setupUi(Window_9_Input_de)
    Window_9_Input_de.show()
    sys.exit(app.exec())