from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Window_7_cv_pointers(object):
    def setupUi(self, Window_7_cv_pointers):
        Window_7_cv_pointers.setObjectName("Window_7_cv_pointers")
        Window_7_cv_pointers.resize(1000, 800)
        Window_7_cv_pointers.setStyleSheet("background-color: rgb(220, 138, 221);")
        self.centralwidget = QtWidgets.QWidget(parent=Window_7_cv_pointers)
        self.centralwidget.setObjectName("centralwidget")
        self.cv_pointers_title = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.cv_pointers_title.setGeometry(QtCore.QRect(0, 50, 1000, 60))
        self.cv_pointers_title.setAutoFillBackground(True)
        self.cv_pointers_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.cv_pointers_title.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.cv_pointers_title.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.cv_pointers_title.setLineWidth(0)
        self.cv_pointers_title.setObjectName("cv_pointers_title")
        # NEXT BUTTON
        self.next_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(650, 705, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.next_button.setFont(font)
        self.next_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.next_button.setObjectName("next_button")
        self.cv_pointers_space = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.cv_pointers_space.setGeometry(QtCore.QRect(50, 139, 900, 491))
        self.cv_pointers_space.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            'font: 12pt "Ubuntu";\n'
            "\n"
            "color: rgb(220, 138, 221);"
        )
        #BACK BUTTON
        self.cv_pointers_space.setPlainText("")
        self.cv_pointers_space.setOverwriteMode(True)
        self.cv_pointers_space.setBackgroundVisible(False)
        self.cv_pointers_space.setCenterOnScroll(False)
        self.cv_pointers_space.setObjectName("cv_pointers_space")
        self.back_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(150, 705, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
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
        # EXPORT BUTTON
        self.export_button.setObjectName("export_button")
        Window_7_cv_pointers.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Window_7_cv_pointers)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        Window_7_cv_pointers.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Window_7_cv_pointers)
        self.statusbar.setObjectName("statusbar")
        Window_7_cv_pointers.setStatusBar(self.statusbar)

        self.retranslateUi(Window_7_cv_pointers)
        QtCore.QMetaObject.connectSlotsByName(Window_7_cv_pointers)

    def retranslateUi(self, Window_7_cv_pointers):
        _translate = QtCore.QCoreApplication.translate
        Window_7_cv_pointers.setWindowTitle(
            _translate("Window_7_cv_pointers", "LazyApp")
        )
        self.cv_pointers_title.setHtml(
            _translate(
                "Window_7_cv_pointers",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:26pt; font-weight:700;">CV Improvements</span></p></body></html>',
            )
        )
        self.next_button.setText(_translate("Window_7_cv_pointers", "NEXT ->"))
        self.back_button.setText(_translate("Window_7_cv_pointers", "<- BACK"))
        self.export_button.setText(_translate("Window_7_cv_pointers", " EXPORT TO PDF"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window_7_cv_pointers = QtWidgets.QMainWindow()
    ui = Ui_Window_7_cv_pointers()
    ui.setupUi(Window_7_cv_pointers)
    Window_7_cv_pointers.show()
    sys.exit(app.exec())
