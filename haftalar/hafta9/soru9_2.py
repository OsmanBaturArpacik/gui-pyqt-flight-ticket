from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setWindowTitle('Hafta 9')
		self.setGeometry(300, 300, 250, 150)

		usernameLabel = QLabel("&Username",self)
		usernameText = QLineEdit(self)
		usernameLabel.setBuddy(usernameText)

		usernamePassLabel = QLabel("&Password",self)
		usernamePassText = QLineEdit(self)
		usernamePassLabel.setBuddy(usernamePassText)

		vbox = QVBoxLayout()
		vbox.addWidget(usernameLabel)
		vbox.addWidget(usernameText)
		vbox.addWidget(usernamePassLabel)
		vbox.addWidget(usernamePassText)
		self.setLayout(vbox)



if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())