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

		button = QPushButton("&Ok",self)
		button2 = QPushButton("&Cancel",self)

		grid = QGridLayout()
		grid.addWidget(usernameLabel ,0 ,0)
		grid.addWidget(usernameText ,0,1 ,1,2)
		grid.addWidget(usernamePassLabel ,1 ,0)
		grid.addWidget(usernamePassText ,1,1 ,1,2)
		grid.addWidget(button ,2,1)
		grid.addWidget(button2 ,2,2)
		self.setLayout(grid)



if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exit(app.exec_())