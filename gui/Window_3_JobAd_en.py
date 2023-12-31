from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Window_3_JobAd_en(object):
    def setupUi(self, Window_3_JobAd_en):
        Window_3_JobAd_en.setObjectName("Window_3_JobAd_en")
        Window_3_JobAd_en.resize(1000, 800)
        Window_3_JobAd_en.setStyleSheet("background-color: rgb(220, 138, 221);")
        self.centralwidget = QtWidgets.QWidget(parent=Window_3_JobAd_en)
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

        # NEXT BUTTON
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
            "color: rgb(220, 138, 221);"
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
            "color: rgb(220, 138, 221);"
        )
        self.specialrequest.setOverwriteMode(True)
        self.specialrequest.setBackgroundVisible(True)
        self.specialrequest.setCenterOnScroll(False)
        self.specialrequest.setObjectName("plainTextEdit")
        self.specialrequest.canPaste()


        Window_3_JobAd_en.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Window_3_JobAd_en)
        self.statusbar.setObjectName("statusbar")
        Window_3_JobAd_en.setStatusBar(self.statusbar)

        self.retranslateUi(Window_3_JobAd_en)
        QtCore.QMetaObject.connectSlotsByName(Window_3_JobAd_en)

    def retranslateUi(self, Window_3_JobAd_en):
        _translate = QtCore.QCoreApplication.translate
        Window_3_JobAd_en.setWindowTitle(_translate("Window_3_JobAd_en", "LazyApp"))
        self.headline_3.setHtml(
            _translate(
                "Window_3_JobAd_en",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:26pt;">Which job do you want to apply for?</span></p></body></html>',
            )
        )
        self.next_button_3.setText(_translate("Window_3_JobAd_en", "NEXT ->"))
        self.jobTextEdit.setPlainText(
            _translate(
                "Window_3_JobAd_en",
                "Please copy and paste the advertising for your dream job here.",
            )
        )
        self.specialrequest.setPlainText(
            _translate(
                "Window_3_JobAd_en",
                "Please write down any special requests you may have for your application letter.(optional)",
            )
        )
        self.back_button.setText(_translate("Window_3_JobAd_en", "<- BACK"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Window_3_JobAd_en = QtWidgets.QMainWindow()
    ui = Ui_Window_3_JobAd_en()
    ui.setupUi(Window_3_JobAd_en)
    Window_3_JobAd_en.show()
    sys.exit(app.exec())
