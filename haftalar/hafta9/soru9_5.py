from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout
import sys

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('label')
		self.setGeometry(700, 400, 250, 150) # xy width height

		label = QLabel("Adinizi giriniz:",self)
		label = QLabel("Adinizi giriniz:",self)
		self.setCentralWidget(label)

		closeBtn = QPushButton(self)
		closeBtn.setShortcut('Ctrl+C')
		closeBtn.resize(100, 50)
		closeBtn.clicked.connect(self.fnClose)


		vbox = QVBoxLayout()


	def fnClose(self):
		print('Butona Tiklandi')




if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())