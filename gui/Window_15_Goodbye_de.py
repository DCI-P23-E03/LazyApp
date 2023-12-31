from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Window_15_Goodbye_de(object):
    def setupUi(self, Window_15_Goodbye_de):
        Window_15_Goodbye_de.setObjectName("Window_15_Goodbye_de")
        Window_15_Goodbye_de.resize(1000, 800)
        Window_15_Goodbye_de.setStyleSheet("background-color: rgb(67,110,238);")
        self.centralwidget = QtWidgets.QWidget(parent=Window_15_Goodbye_de)
        self.centralwidget.setObjectName("centralwidget")
        self.goodbye_text_1 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.goodbye_text_1.setGeometry(QtCore.QRect(0, 270, 1001, 51))
        self.goodbye_text_1.setAutoFillBackground(True)
        self.goodbye_text_1.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.goodbye_text_1.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.goodbye_text_1.setLineWidth(0)
        self.goodbye_text_1.setObjectName("goodbye_text")
        # EXIT BUTTON
        self.exit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(410, 440, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.exit_button.setObjectName("exit_button")
        self.goodbye_text__2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.goodbye_text__2.setGeometry(QtCore.QRect(0, 140, 1001, 121))
        self.goodbye_text__2.setAutoFillBackground(True)
        self.goodbye_text__2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.goodbye_text__2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.goodbye_text__2.setLineWidth(0)
        self.goodbye_text__2.setObjectName("goodbye_text__2")
        self.start_button_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start_button_2.setGeometry(QtCore.QRect(411, 522, 200, 50))
               
        self.goodbye_text__3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.goodbye_text__3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.goodbye_text__3.setGeometry(QtCore.QRect(0, 650, 1001, 50))
        self.goodbye_text__3.setStyleSheet("background-color: rgb(67,110,238); color:#324990; font-size:18pt;")
        self.goodbye_text__3.setObjectName("goodbye_text__3")

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(220, 138, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(220, 138, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(220, 138, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active,
            QtGui.QPalette.ColorRole.PlaceholderText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive,
            QtGui.QPalette.ColorRole.WindowText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(220, 138, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive,
            QtGui.QPalette.ColorRole.ButtonText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(220, 138, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(220, 138, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive,
            QtGui.QPalette.ColorRole.PlaceholderText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled,
            QtGui.QPalette.ColorRole.WindowText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(220, 138, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled,
            QtGui.QPalette.ColorRole.ButtonText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(220, 138, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(220, 138, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled,
            QtGui.QPalette.ColorRole.PlaceholderText,
            brush,
        )
        self.start_button_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.start_button_2.setFont(font)
        self.start_button_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.start_button_2.setObjectName("start_button_2")
        Window_15_Goodbye_de.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Window_15_Goodbye_de)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        Window_15_Goodbye_de.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Window_15_Goodbye_de)
        self.statusbar.setObjectName("statusbar")
        Window_15_Goodbye_de.setStatusBar(self.statusbar)

        self.retranslateUi(Window_15_Goodbye_de)
        QtCore.QMetaObject.connectSlotsByName(Window_15_Goodbye_de)

    def retranslateUi(self, Window_15_Goodbye_de):
        _translate = QtCore.QCoreApplication.translate
        Window_15_Goodbye_de.setWindowTitle(
            _translate("Window_15_Goodbye_de", "LazyApp")
        )
        self.goodbye_text_1.setHtml(
            _translate(
                "Window_15_Goodbye_de",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:28pt; color:#324990;">Viel Glück und danke, dass du mit uns faul warst.</span></p></body></html>',
            )
        )
        self.exit_button.setText(_translate("Window_15_Goodbye_de", "FERTIG"))
        self.goodbye_text__2.setHtml(
            _translate(
                "Window_15_Goodbye_de",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:72pt; font-weight:704; color:#ffffff;">TSCHÖÖ!</span></p></body></html>',
            )
        )
        self.start_button_2.setText(_translate("Window_15_Goodbye_de", "NOCHMAL"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window_15_Goodbye_de = QtWidgets.QMainWindow()
    ui = Ui_Window_15_Goodbye_de()
    ui.setupUi(Window_15_Goodbye_de)
    Window_15_Goodbye_de.show()
    sys.exit(app.exec())
