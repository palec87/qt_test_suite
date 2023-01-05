#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, QObject, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class Example(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI(self)

    def initUI(self, MainWindow):
        # centralwidget
        MainWindow.resize(346, 193)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # The Action to quit
        self.toolb_action_Exit = QAction(QIcon("exit.png"), "Exit", self)
        self.toolb_action_Exit.setShortcut("Ctrl+Q")
        self.toolb_action_Exit.triggered.connect(self.close)

        # The Button
        self.btn_prt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_prt.setGeometry(QtCore.QRect(120, 20, 89, 25))
        self.btn_prt.clicked.connect(lambda: self.doPrint())
        self.btn_quit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_quit.setGeometry(QtCore.QRect(220, 20, 89, 25))
        self.btn_quit.clicked.connect(lambda: self.close())

        # The textEdit
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 60, 321, 81))

        # Show the frame
        MainWindow.setCentralWidget(self.centralwidget)
        # self.show()

    def doPrint(self):
        print("TEST doPrint")

    def closeEvent(self, event):
        # Ask a question before to quit.
        self.replyClosing = QMessageBox.question(
            self,
            "Message",
            "Are you sure to quit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if self.replyClosing == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main_GUI():
    app = QApplication(sys.argv)
    imageViewer = Example()
    imageViewer.show()
    return app, imageViewer


if __name__ == "__main__":
    app, imageViewer = main_GUI()
    rc = app.exec_()
    print("App end is exit code {}".format(rc))
    sys.exit(rc)
