import pymongo as m

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
import sys
from login import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.onClicked)

	def onClicked(self):
		email = self.lineEdit.text()
		password = self.lineEdit_2.text()
		check_user(email, password)
		print("aaaaaa")

db = None
user_collection = None

def check_user(email, password):
	global user_collection
	user = user_collection.find({"email": email, "password": password})
	print(user)



def connect_db():
	global db
	global user_collection
	myClient = m.MongoClient("mongodb://localhost:27017")
	print(myClient.list_database_names())
	dblist = myClient.list_database_names()
	if "test" in dblist:
		print("exist")

	db = myClient["test"]
	user_collection = db["user"]
	print(db.list_collection_names())





if __name__ == '__main__':
	connect_db()
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
