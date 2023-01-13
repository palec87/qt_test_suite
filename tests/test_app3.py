#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from PyQt5 import QtTest
from pytestqt.plugin import QtBot

from app3 import main_GUI


# @pytest.fixture(scope="module")
# def qtbot_session(qapp, request):
#     print("  SETUP qtbot")
#     result = QtBot(qapp)
#     return result
#     # with capture_exceptions() as exceptions:
#     #     yield result
#     # print("  TEARDOWN qtbot")


# @pytest.fixture(scope="module")
# def Viewer(request):
#     print("  SETUP GUI")
#     app, imageViewer = main_GUI()
#     QtTest.QTest.qWait(int(0.5*100))
#     qtbotbis = QtBot(app)
#     QtTest.QTest.qWait(int(0.5*100))
#     return app, imageViewer, qtbotbis


# def test_interface(Viewer):
#     print("  beginning ")
#     app, imageViewer, qtbot = Viewer
#     QtTest.QTest.qWait(int(0.5*100))
#     assert imageViewer.textEdit.toPlainText() == ''
