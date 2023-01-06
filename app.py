#!/usr/bin/env python

'''
Simple app with one spinbox based on 
https://www.geeksforgeeks.org/pyqt5-qspinbox-widget/
'''

from PyQt5 import QtWidgets
import sys


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()

        self.setGeometry(100, 100, 600, 400)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        self.spin = QtWidgets.QSpinBox(self)
        self.spin.setGeometry(100, 100, 100, 40)
        self.spin.valueChanged.connect(self.show_result)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(100, 200, 200, 40)

    def show_result(self):
        self.label.setText("Value : " + str(self.spin.value()))
        print(self.label.text())


def main_GUI():
    app = QtWidgets.QApplication(sys.argv)
    imageViewer = App()
    imageViewer.show()
    return app, imageViewer


if __name__ == '__main__':
    app, imageViewer = main_GUI()
    rc = app.exec_()
    print("App end is exit code {}".format(rc))
    sys.exit(rc)
