from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Window_10_JobAd_de(object):
    def setupUi(self, Window_10_JobAd_de):
        Window_10_JobAd_de.setObjectName("Window_10_JobAd_de")
        Window_10_JobAd_de.resize(1000, 800)
        Window_10_JobAd_de.setStyleSheet("background-color: rgb(67,110,238);")
        self.centralwidget = QtWidgets.QWidget(parent=Window_10_JobAd_de)
        self.centralwidget.setObjectName("centralwidget")

        # headline
        self.headline_3 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.headline_3.setGeometry(QtCore.QRect(0, 50, 1000, 60))
        self.headline_3.setAutoFillBackground(True)
        self.headline_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.headline_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.headline_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.headline_3.setLineWidth(0)
        self.headline_3.setObjectName("headline_3")

        # NEXT BUTTON and BACK BUTTON
        self.next_button_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_button_3.setGeometry(QtCore.QRect(650, 705, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.next_button_3.setFont(font)
        self.next_button_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.next_button_3.setObjectName("next_button_3")
        self.back_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(150, 705, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.back_button.setObjectName("back_button")

        # Input field for Job Advertisement
        self.jobTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.jobTextEdit.setGeometry(QtCore.QRect(50, 139, 900, 350))
        self.jobTextEdit.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            'font: 12pt "Ubuntu";\n'
            "\n"
            "color: rgb(67,110,238);"
        )
        self.jobTextEdit.setOverwriteMode(True)
        self.jobTextEdit.setBackgroundVisible(True)
        self.jobTextEdit.setCenterOnScroll(False)
        self.jobTextEdit.setObjectName("plainTextEdit")
        self.jobTextEdit.canPaste()

        # Input field for special request
        self.specialrequest = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.specialrequest.setGeometry(QtCore.QRect(50, 500, 900, 150))
        self.specialrequest.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            'font: 12pt "Ubuntu";\n'
            "\n"
            "color: rgb(67,110,238);"
        )
        self.specialrequest.setOverwriteMode(True)
        self.specialrequest.setBackgroundVisible(True)
        self.specialrequest.setCenterOnScroll(False)
        self.specialrequest.setObjectName("plainTextEdit")
        self.specialrequest.canPaste()

        Window_10_JobAd_de.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Window_10_JobAd_de)
        self.statusbar.setObjectName("statusbar")
        Window_10_JobAd_de.setStatusBar(self.statusbar)

        self.retranslateUi(Window_10_JobAd_de)
        QtCore.QMetaObject.connectSlotsByName(Window_10_JobAd_de)

    def retranslateUi(self, Window_10_JobAd_de):
        _translate = QtCore.QCoreApplication.translate
        Window_10_JobAd_de.setWindowTitle(_translate("Window_10_JobAd_de", "LazyApp"))
        self.headline_3.setHtml(
            _translate(
                "Window_10_JobAd_de",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:26pt;">Für welchen Job möchtest du dich bewerben?</span></p></body></html>',
            )
        )
        self.next_button_3.setText(_translate("Window_10_JobAd_de", "VOR ->"))
        self.jobTextEdit.setPlainText(
            _translate(
                "Window_10_JobAd_de",
                "Bitte kopiere hier die Anzeige für deinen Traumjob hinein.",
            )
        )
        self.specialrequest.setPlainText(
            _translate(
                "Window_3_JobAd_en",
                "Schreibe hier alle besonderen Wünsche auf, die du für dein Anschreiben hast. (optional)",
            )
        )
        self.back_button.setText(_translate("Window_10_JobAd_de", "<- ZURÜCK"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Window_10_JobAd_de = QtWidgets.QMainWindow()
    ui = Ui_Window_10_JobAd_de()
    ui.setupUi(Window_10_JobAd_de)
    Window_10_JobAd_de.show()
    sys.exit(app.exec())
