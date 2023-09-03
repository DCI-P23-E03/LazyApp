from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Window_11_Output_de(object):
    def setupUi(self, Window_11_Output_de):
        Window_11_Output_de.setObjectName("Window_11_Output_de")
        Window_11_Output_de.resize(1000, 800)
        Window_11_Output_de.setStyleSheet("\n""background-color: rgb(67,110,238);")
        self.centralwidget = QtWidgets.QWidget(parent=Window_11_Output_de)
        self.centralwidget.setObjectName("centralwidget")

        # headline
        self.headline_Window_11_Output_de = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.headline_Window_11_Output_de.setGeometry(QtCore.QRect(0, 50, 1000, 60))
        self.headline_Window_11_Output_de.setAutoFillBackground(True)
        self.headline_Window_11_Output_de.setStyleSheet("color: rgb(255, 255, 255);")
        self.headline_Window_11_Output_de.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.headline_Window_11_Output_de.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.headline_Window_11_Output_de.setLineWidth(0)
        self.headline_Window_11_Output_de.setObjectName("headline_Window_11_Output_de")

        # buttons
        self.next_button_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_button_4.setGeometry(QtCore.QRect(650, 705, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.next_button_4.setFont(font)
        self.next_button_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.next_button_4.setObjectName("next_button_4")
        self.back_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(150, 705, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet(("color: rgb(255, 255, 255);"))
        self.back_button.setObjectName("back_button")

        # set explanations - Application Letter
        self.textBrowser_Application_Letter = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_Application_Letter.setGeometry(QtCore.QRect(480, 220, 491, 100))
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
        self.textBrowser_Cheat_Sheet.setGeometry(QtCore.QRect(480, 370, 491, 110))
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
        self.textBrowser_CV_Improvements.setGeometry(QtCore.QRect(480, 520, 491, 110))
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
        self.checkBox_Application_letter.setGeometry(QtCore.QRect(150, 220, 300, 30))
        self.checkBox_Application_letter.setObjectName("checkBox_Application_letter")
        self.checkBox_Application_letter.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_Application_letter.setFont(font)

        self.checkBox_Cheat_Sheet = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_Cheat_Sheet.setGeometry(QtCore.QRect(150, 370, 300, 30))
        self.checkBox_Cheat_Sheet.setObjectName("checkBox_Cheat_Sheet")
        self.checkBox_Cheat_Sheet.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_Cheat_Sheet.setFont(font)

        self.checkBox_CV_Improvements = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_CV_Improvements.setGeometry(QtCore.QRect(150, 520, 300, 30))
        self.checkBox_CV_Improvements.setObjectName("checkBox_CV_Improvements")
        self.checkBox_CV_Improvements.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_CV_Improvements.setFont(font)

        Window_11_Output_de.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Window_11_Output_de)
        self.statusbar.setObjectName("statusbar")
        Window_11_Output_de.setStatusBar(self.statusbar)

        self.retranslateUi(Window_11_Output_de)
        QtCore.QMetaObject.connectSlotsByName(Window_11_Output_de)


    def retranslateUi(self, Window_11_Output_de):
        _translate = QtCore.QCoreApplication.translate
        Window_11_Output_de.setWindowTitle(_translate("Window_11_Output_de", "LazyApp"))
        self.headline_Window_11_Output_de.setHtml(_translate("Window_11_Output_de", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 0 px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:700; font-color: white\">Was brauchst du heute?</span></p></body></html>"))

        self.next_button_4.setText(_translate("Window_11_Output_de", "VOR ->"))
        self.back_button.setText(_translate("Window_11_Output_de", "<- ZURÜCK"))
        self.textBrowser_Application_Letter.setHtml(_translate("Window_11_Output_de", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 0; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">Basierend auf deinen Informationen wird die KI ein Anschreiben passend für deinen Traumjob entwerfen.<br>Du kannst den Text kopieren oder als PDF exportieren.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>"))
        self.textBrowser_Cheat_Sheet.setHtml(_translate("Window_11_Output_de", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 0px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">Sich auf ein Bewerbungsgespräch vorbereiten kann sehr zeitaufwändig sein.<br>Sei faul und lass dir die wichtisten Stichpunkte zusammenfassen.<br>Du kannst den Text kopieren oder als PDF exportieren.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>"))
        self.textBrowser_CV_Improvements.setHtml(_translate("Window_11_Output_de", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 0 px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">Willst du deine Chancen auf ein Bewerbungsgespräch verbessern?<br>Lass dir von der KI Verbesserungsvorschläge für deinen Lebenslauf geben.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>"))
        self.checkBox_Application_letter.setText(_translate("Window_11_Output_de", "Anschreiben"))
        self.checkBox_Cheat_Sheet.setText(_translate("Window_11_Output_de", "Spickzettel"))
        self.checkBox_CV_Improvements.setText(_translate("Window_11_Output_de", "CV Verbesserungen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window_11_Output_de = QtWidgets.QMainWindow()
    ui = Ui_Window_11_Output_de()
    ui.setupUi(Window_11_Output_de)
    Window_11_Output_de.show()
    sys.exit(app.exec())