import pymongo as m

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from PyQt5.uic.properties import QtWidgets

from crud_dashboard import Ui_MainWindow as crud

class MainWindow(QMainWindow, crud):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.load_users()
		self.pushButton.clicked.connect(self.onClicked)


	def load_users(self):
		users = self.collection.find()
		for user in users:
			if "username" in user and "password" in user:
				row_position = self.tableWidget.rowCount()
				self.tableWidget.insertRow(row_position)
				# self.tableWidget.setItem(row_position,0, QTableWidgetItem user["username"])
				# self.tableWidget.setItem(row_position,1, user["password"])
				self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(user["username"]))
				self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(user["password"]))


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
