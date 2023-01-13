import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMessageBox,
    QMainWindow,
    QTextEdit,
    QLineEdit,
    QGridLayout,
    QLabel,
)


class mainwindow(QMainWindow):
    def __init__(self, parent=None):
        super(mainwindow, self).__init__(parent)
        # super().__init__()

        self.createUI()

    def createUI(self):
        mymenubar = self.menuBar()
        filemenu = mymenubar.addMenu("File")
        filemenu.addAction("help")
        filemenu.addAction("exit")

        contactlabel = QLabel("Contact:", self)
        contacttextedit = QLineEdit(self)
        countlabel = QLabel("Count:")
        counttextedit = QLineEdit()
        msglabel = QLabel("Your message here:")
        self.msgbox = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(contactlabel, 1, 0)
        grid.addWidget(contacttextedit, 1, 1)

        grid.addWidget(countlabel, 2, 0)
        grid.addWidget(counttextedit, 2, 1)

        grid.addWidget(msglabel, 3, 0)
        grid.addWidget(self.msgbox, 3, 1, 5, 1)

        # self.setLayout(grid)
        central_widget = QWidget()
        central_widget.setLayout(grid)
        self.setCentralWidget(central_widget)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Whatsapp Message Sender")
        self.show()

    # def closeEvent(self, event):
    #     # Ask a question before to quit.
    #     self.replyClosing = QMessageBox.question(
    #         self,
    #         "Message",
    #         "Are you sure to quit?",
    #         QMessageBox.Yes | QMessageBox.No,
    #         QMessageBox.No,
    #     )

    #     if self.replyClosing == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()


def main_GUI():
    app = QApplication(sys.argv)
    imageViewer = mainwindow()
    imageViewer.show()
    return app, imageViewer


if __name__ == "__main__":
    app, imageViewer = main_GUI()
    rc = app.exec_()
    print("App end is exit code {}".format(rc))
    sys.exit(rc)
