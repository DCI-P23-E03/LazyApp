from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Window_4_Output(object):
    def setupUi(self, Window_4_Output):
        Window_4_Output.setObjectName("Window_4_Output")
        Window_4_Output.resize(1000, 800)
        Window_4_Output.setStyleSheet("\n""background-color: rgb(220, 138, 221);")
        self.centralwidget = QtWidgets.QWidget(parent=Window_4_Output)
        self.centralwidget.setObjectName("centralwidget")

        # headline
        self.headline_Window4_Output = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.headline_Window4_Output.setGeometry(QtCore.QRect(0, 50, 1000, 60))
        self.headline_Window4_Output.setAutoFillBackground(True)
        self.headline_Window4_Output.setStyleSheet("color: rgb(255, 255, 255);")
        self.headline_Window4_Output.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.headline_Window4_Output.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.headline_Window4_Output.setLineWidth(0)
        self.headline_Window4_Output.setObjectName("headline_Window4_Output")

        # buttons
        self.next_button_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_button_4.setGeometry(QtCore.QRect(650, 705, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.next_button_4.setFont(font)
        self.next_button_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.next_button_4.setObjectName("next_button_4")
        self.back_button_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_button_4.setGeometry(QtCore.QRect(150, 705, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.back_button_4.setFont(font)
        self.back_button_4.setStyleSheet(("color: rgb(255, 255, 255);"))
        self.back_button_4.setObjectName("back_button_4")

        # set explanations - Application Letter
        self.textBrowser_Application_Letter = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_Application_Letter.setGeometry(QtCore.QRect(450, 250, 491, 131))
        self.textBrowser_Application_Letter.setAutoFillBackground(True)
        self.textBrowser_Application_Letter.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBrowser_Application_Letter.setFrameStyle(0)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(18)
        self.textBrowser_Application_Letter.setFont(font)
        self.textBrowser_Application_Letter.setObjectName("textBrowser_Application_Letter")
        
        # explanation Cheat Sheet
        self.textBrowser_Cheat_Sheet = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_Cheat_Sheet.setGeometry(QtCore.QRect(450, 400, 491, 131))
        self.textBrowser_Cheat_Sheet.setAutoFillBackground(True)
        self.textBrowser_Cheat_Sheet.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBrowser_Cheat_Sheet.setFrameStyle(0)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(16)
        self.textBrowser_Cheat_Sheet.setFont(font)
        self.textBrowser_Cheat_Sheet.setObjectName("textBrowser_Cheat_Sheet")

        # explanation CV Improvements
        self.textBrowser_CV_Improvements = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_CV_Improvements.setGeometry(QtCore.QRect(450, 550, 491, 131))
        self.textBrowser_CV_Improvements.setAutoFillBackground(True)
        self.textBrowser_CV_Improvements.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBrowser_CV_Improvements.setFrameStyle(0)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(16)
        self.textBrowser_CV_Improvements.setFont(font)
        self.textBrowser_CV_Improvements.setObjectName("textBrowser_CV_Improvements")

        # Checkboxes
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(16)
        self.checkBox_Application_letter = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_Application_letter.setGeometry(QtCore.QRect(100, 250, 300, 30))
        self.checkBox_Application_letter.setObjectName("checkBox_Application_letter")
        self.checkBox_Application_letter.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_Application_letter.setFont(font)

        self.checkBox_Cheat_Sheet = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_Cheat_Sheet.setGeometry(QtCore.QRect(100, 400, 300, 30))
        self.checkBox_Cheat_Sheet.setObjectName("checkBox_Cheat_Sheet")
        self.checkBox_Cheat_Sheet.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_Cheat_Sheet.setFont(font)

        self.checkBox_CV_Improvements = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_CV_Improvements.setGeometry(QtCore.QRect(100, 550, 300, 30))
        self.checkBox_CV_Improvements.setObjectName("checkBox_CV_Improvements")
        self.checkBox_CV_Improvements.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_CV_Improvements.setFont(font)

        Window_4_Output.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Window_4_Output)
        self.statusbar.setObjectName("statusbar")
        Window_4_Output.setStatusBar(self.statusbar)

        self.retranslateUi(Window_4_Output)
        QtCore.QMetaObject.connectSlotsByName(Window_4_Output)


    def retranslateUi(self, Window_4_Output):
        _translate = QtCore.QCoreApplication.translate
        Window_4_Output.setWindowTitle(_translate("MainWindow4_Output", "LazyApp"))
        self.headline_Window4_Output.setHtml(_translate("MainWindow4_Output", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 0 px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:700; font-color: white\">What do you need today?</span></p></body></html>"))

        self.next_button_4.setText(_translate("MainWindow4_Output", "NEXT ->"))
        self.back_button_4.setText(_translate("MainWindow4_Output", "<- BACK"))
        self.textBrowser_Application_Letter.setHtml(_translate("MainWindow4_Output", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 0; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">Based on your input AI will construct an application letter that is suited for your dream job. You will be able to copy the text, as well as export as PDF later on.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>"))
        self.textBrowser_Cheat_Sheet.setHtml(_translate("MainWindow4_Output", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 0px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">Preparing for a Job Interview can be time consuming. Be lazy with us and get the most important pointers for your interview. You will be able to export this as PDF as well.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>"))
        self.textBrowser_CV_Improvements.setHtml(_translate("MainWindow4_Output", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 0 px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">Want to increase your chances of being considered for the position you're applying for?<br>Let AI give you some pointers on how your CV might be better targetted to the job you are applying for.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>"))
        self.checkBox_Application_letter.setText(_translate("MainWindow4_Output", "Application letter"))
        self.checkBox_Cheat_Sheet.setText(_translate("MainWindow4_Output", "Cheat Sheet"))
        self.checkBox_CV_Improvements.setText(_translate("MainWindow4_Output", "CV Improvements"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window_4_Output = QtWidgets.QMainWindow()
    ui = Ui_Window_4_Output()
    ui.setupUi(Window_4_Output)
    Window_4_Output.show()
    sys.exit(app.exec())
