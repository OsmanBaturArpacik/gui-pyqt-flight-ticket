from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("My PyQt5 Window")
        self.setGeometry(100, 100, 600, 400)

        label = QLabel("Osman", self)
        label2 = QLabel("Batur", self)


        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(label2)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

