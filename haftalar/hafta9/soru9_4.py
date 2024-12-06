from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setWindowTitle('Hafta 9')
		self.setGeometry(700, 400, 250, 150) # xy width height

		self.closeBtn = QPushButton(self)
		self.closeBtn.setShortcut('Ctrl+C')
		self.closeBtn.resize(100, 50)
		self.closeBtn.clicked.connect(self.fnClose)

	def fnClose(self):
		print('Button function closed')
		self.close()



if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())