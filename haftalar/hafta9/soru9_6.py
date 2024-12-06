from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('Butona tiklama')
		self.setGeometry(700, 400, 350, 250) # xy width height


		btn = QPushButton("Tikla bana",self)
		btn.resize(120, 40)
		btn.clicked.connect(self.btnOnClicked)

		self.setCentralWidget(btn)


	def btnOnClicked(self):
		print('Butona Tiklandi')




if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())