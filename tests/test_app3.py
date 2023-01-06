#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import pytest
from PyQt5 import QtCore, QtGui, QtTest, QtWidgets
from PyQt5.QtCore import QCoreApplication, QObject, Qt
from PyQt5.QtWidgets import *
from pytestqt.plugin import QtBot

from app3 import main_GUI


@pytest.fixture(scope="module")
def qtbot_session(qapp, request):
    print("  SETUP qtbot")
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


def test_interface(Viewer):
    print("  beginning ")
    app, imageViewer, qtbot = Viewer
    assert imageViewer.textEdit.toPlainText() == ''
