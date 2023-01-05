#!/usr/bin/env python

'''Basic tests of the optac module'''

import pytest
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QMessageBox,
    QAction,
    QMenu,
    QMainWindow,
    QTextEdit,
    QLineEdit,
    QGridLayout,
    QLabel,
)
# from PyQt5 import QtCore, QtWidgets
# from app import App
from PyQt5 import QtTest
from app2 import main_GUI
import time
from pytestqt.plugin import QtBot


def divide(x, y):
    return x / y


def test_raises():
    with pytest.raises(ZeroDivisionError):
        divide(3, 0)


# @pytest.fixture
# def app(qtbot):
#     test_app = App()
#     qtbot.addWidget(test_app)
#     return test_app


# @pytest.mark.parametrize(
#     'func, set, attr, expected',
#     [('app.spin.setValue', 34, 'app.label.text()', 'Value : 34'),
#      ('app.spin.setValue', 9, 'app.label.text()', 'Value : 9'),
#      ])
# def test_update_func(app, func, set, attr, expected):
#     eval(func + '(set)')
#     time.sleep(0.1)
#     assert eval(attr) == expected


# @pytest.mark.parametrize(
#     'func, set, attr, expected',
#     [('test_app.spin.setValue', 34, 'test_app.label.text()', 'Value : 34'),
#      ('test_app.spin.setValue', 9, 'test_app.label.text()', 'Value : 9'),
#      ])
# def test_update_f(qtbot, func, set, attr, expected):
#     app = QtWidgets.QApplication([])
#     test_app = App()
#     qtbot.addWidget(test_app)
#     eval(func + '(set)')
#     time.sleep(0.1)
#     assert eval(attr) == expected


@pytest.fixture(scope='module')
def app(qapp, request):
    result = QtBot(qapp)
    with capture_exceptions() as exceptions:
        yield result
    print("  TEARDOWN qtbot")


@pytest.fixture(scope="module")
def Viewer(request):
    print("  SETUP GUI")
    app, imageViewer = main_GUI()
    qtbotbis = QtBot(app)
    QtTest.QTest.qWait(int(0.5*100))
    return app, imageViewer, qtbotbis


def test_app2(Viewer):
    app, imageViewer, qtbot = Viewer
    imageViewer.msgbox.setText('bla')
    assert imageViewer.msgbox.toPlainText() == 'bla'
