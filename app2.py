import sys
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


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

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

    # MODIFYING CLOSE EVENT SO IT ASKS BEFORE EXIT
    # def closeEvent(self, event):
    #     reply = QMessageBox.question(
    #         self, "Message", "quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
    #     )

    #     if reply == QMessageBox.No:
    #         event.ignore()
    #     else:
    #         event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = mainwindow()
    ex.show()
    sys.exit(app.exec())
