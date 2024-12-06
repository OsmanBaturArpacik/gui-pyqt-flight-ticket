from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QFormLayout, QLabel, QLineEdit
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

		layout = QFormLayout()
		nameLabel = QLabel("Ad : ", self)
		nameLineEdit = QLineEdit(self)
		emailLabel = QLabel("Email : ", self)
		emailLineEdit = QLineEdit(self)

		layout.addRow(nameLabel, nameLineEdit)
		layout.addRow(emailLabel, emailLineEdit)

		btn = QPushButton("Kaydet", self)
		layout.addRow(btn)

		centralWidget.setLayout(layout)





if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())