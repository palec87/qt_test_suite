#!/usr/bin/env python

'''
Simple app with one spinbox based on
https://www.geeksforgeeks.org/pyqt5-qspinbox-widget/
'''

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QSpinBox,
    QLabel

)

import sys


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()

        self.setGeometry(100, 100, 600, 400)
        self.UiComponents(self)
        self.show()

    def UiComponents(self, Window):
        self.centralwidget = QWidget(Window)
        self.spin = QSpinBox(self)
        self.spin.setGeometry(100, 100, 100, 40)
        self.spin.valueChanged.connect(self.show_result)
        self.label = QLabel(self)
        self.label.setGeometry(100, 200, 200, 40)

        Window.setCentralWidget(self.centralwidget)

    def show_result(self):
        self.label.setText("Value : " + str(self.spin.value()))
        print(self.label.text())


def main_GUI():
    app = QApplication(sys.argv)
    imageViewer = App()
    imageViewer.show()
    return app, imageViewer


if __name__ == '__main__':
    app, imageViewer = main_GUI()
    rc = app.exec_()
    print("App end is exit code {}".format(rc))
    sys.exit(rc)
