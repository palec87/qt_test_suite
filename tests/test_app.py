#!/usr/bin/env python

'''Basic tests of the optac module'''

import pytest
# from PyQt5 import QtCore, QtWidgets
# from app import App
from PyQt5 import QtTest
from app import main_GUI
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
def app(qapp):
    result = QtBot(qapp)
    return result
    # with capture_exceptions() as exceptions:
    #     yield result
    # print("  TEARDOWN qtbot")


@pytest.fixture(scope="module")
def Viewer():
    print("  SETUP GUI")
    app, imageViewer = main_GUI()
    QtTest.QTest.qWait(int(0.5*100))
    qtbotbis = QtBot(app)
    QtTest.QTest.qWait(int(0.5*100))
    return app, imageViewer, qtbotbis


@pytest.mark.parametrize(
    'set_val, expected',
    [(34, 34), (9, 9),
     ])
def test_app(Viewer, set_val, expected):
    _, imageViewer, _ = Viewer
    QtTest.QTest.qWait(int(0.5*100))
    imageViewer.spin.setValue(set_val)
    QtTest.QTest.qWait(int(0.5*100))
    assert imageViewer.spin.value() == expected
