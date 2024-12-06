from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout
import sys

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('layout')
		self.setGeometry(700, 400, 350, 250) # xy width height
		centralWidget = QWidget()
		self.setCentralWidget(centralWidget)
		layout = QVBoxLayout()
		button1 = QPushButton("Button 1", self)
		button2 = QPushButton("Button 2", self)
		button3 = QPushButton("Button 3", self)

		layout.addWidget(button1)
		layout.addWidget(button2)
		layout.addWidget(button3)

		centralWidget.setLayout(layout)


	def btnOnClicked(self):
		print('Butona Tiklandi')




if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())