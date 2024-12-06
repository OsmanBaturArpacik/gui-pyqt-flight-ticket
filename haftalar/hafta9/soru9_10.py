from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QFormLayout, QLabel, QLineEdit, QGridLayout
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

		layout = QGridLayout()
		nameLabel = QLabel("Ad : ", self)
		nameLineEdit = QLineEdit(self)
		emailLabel = QLabel("Email : ", self)
		emailLineEdit = QLineEdit(self)

		layout.addWidget(nameLabel ,0,0)
		layout.addWidget(nameLineEdit ,0,1)
		layout.addWidget(emailLabel ,1,0)
		layout.addWidget(emailLineEdit ,1,1)

		btn = QPushButton("Kaydet", self)
		layout.addWidget(btn ,2,1)

		centralWidget.setLayout(layout)





if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())