import pymongo as m

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
import sys
from login import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.onClicked)
		#mongo
		self.client = m.MongoClient("mongodb://localhost:27017")
		self.db = self.client["test"]
		self.user_collection = self.db["user"]

	def onClicked(self):
		email = self.lineEdit.text()
		password = self.lineEdit_2.text()
		user = self.user_collection.find({"email": email, "password": password})
		print(user)
		print("aaaaaa")


db = None
user_collection = None






if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
