from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QFormLayout, QLabel, QLineEdit, \
	QGridLayout, QVBoxLayout, QHBoxLayout
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

		hboxLayout = QHBoxLayout()
		nameLabel = QLabel("Ad : ", self)
		nameLineEdit = QLineEdit(self)
		hboxLayout.addWidget(nameLabel)
		hboxLayout.addWidget(nameLineEdit)

		layout.addLayout(hboxLayout)

		btn = QPushButton("Kaydet", self)
		layout.addWidget(btn)

		hboxLayout = QHBoxLayout()
		btn2 = QPushButton("btn2", self)
		btn3 = QPushButton("btn3", self)

		hboxLayout.addWidget(btn2)
		hboxLayout.addWidget(btn3)

		layout.addLayout(hboxLayout)

		centralWidget.setLayout(layout)





if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())