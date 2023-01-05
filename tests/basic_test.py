#!/usr/bin/env python

'''Basic tests of the optac module'''

import pytest
from PyQt5 import QtCore, QtWidgets
from app import App
import time


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


@pytest.mark.parametrize(
    'func, set, attr, expected',
    [('test_app.spin.setValue', 34, 'test_app.label.text()', 'Value : 34'),
     ('test_app.spin.setValue', 9, 'test_app.label.text()', 'Value : 9'),
     ])
def test_update_f(qtbot, func, set, attr, expected):
    test_app = App()
    qtbot.addWidget(test_app)
    eval(func + '(set)')
    time.sleep(0.1)
    assert eval(attr) == expected
