from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Window_5_Application_Letter(object):
    def setupUi(self, Window_5_Application_Letter):
        Window_5_Application_Letter.setObjectName("Window_5_Application_Letter")
        Window_5_Application_Letter.resize(1000, 800)
        Window_5_Application_Letter.setStyleSheet(
            "background-color: rgb(220, 138, 221);"
        )
        self.centralwidget = QtWidgets.QWidget(parent=Window_5_Application_Letter)
        self.centralwidget.setObjectName("centralwidget")
        self.Appl_letter_title = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.Appl_letter_title.setGeometry(QtCore.QRect(0, 50, 1000, 60))
        self.Appl_letter_title.setAutoFillBackground(True)
        self.Appl_letter_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.Appl_letter_title.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Appl_letter_title.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.Appl_letter_title.setLineWidth(0)
        self.Appl_letter_title.setObjectName("Appl_letter_title")
        self.next_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(650, 705, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)

        # NEXT BUTTON
        self.next_button.setFont(font)
        self.next_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.next_button.setObjectName("next_button")
        self.Appl_letter_space = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.Appl_letter_space.setGeometry(QtCore.QRect(50, 139, 900, 491))
        self.Appl_letter_space.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            'font: 12pt "Ubuntu";\n'
            "\n"
            "color: rgb(220, 138, 221);"
        )
        self.Appl_letter_space.setPlainText("")
        self.Appl_letter_space.setOverwriteMode(False)
        self.Appl_letter_space.setBackgroundVisible(False)
        self.Appl_letter_space.setCenterOnScroll(False)
        self.Appl_letter_space.setObjectName("Appl_letter_space")
        self.back_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(150, 705, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)

        # BACK BUTTON
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.back_button.setObjectName("back_button")
        self.export_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.export_button.setGeometry(QtCore.QRect(400, 650, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.export_button.setFont(font)
        self.export_button.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(255, 137, 243);"
        )
        self.export_button.setObjectName("export_button")
        Window_5_Application_Letter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Window_5_Application_Letter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        Window_5_Application_Letter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Window_5_Application_Letter)
        self.statusbar.setObjectName("statusbar")
        Window_5_Application_Letter.setStatusBar(self.statusbar)

        self.retranslateUi(Window_5_Application_Letter)
        QtCore.QMetaObject.connectSlotsByName(Window_5_Application_Letter)

    def retranslateUi(self, Window_5_Application_Letter):
        _translate = QtCore.QCoreApplication.translate
        Window_5_Application_Letter.setWindowTitle(
            _translate("Window_5_Application_Letter", "LazyApp")
        )
        self.Appl_letter_title.setHtml(
            _translate(
                "Window_5_Application_Letter",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:26pt; font-weight:700;">Application letter</span></p></body></html>',
            )
        )
        self.next_button.setText(_translate("Window_5_Application_Letter", "NEXT ->"))
        self.back_button.setText(_translate("Window_5_Application_Letter", "<- BACK"))
        # EXPORT BUTTON
        self.export_button.setText(
            _translate("Window_5_Application_Letter", " EXPORT TO PDF")
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window_5_Application_Letter = QtWidgets.QMainWindow()
    ui = Ui_Window_5_Application_Letter()
    ui.setupUi(Window_5_Application_Letter)
    Window_5_Application_Letter.show()
    sys.exit(app.exec())
