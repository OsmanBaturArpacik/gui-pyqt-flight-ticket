import pymongo as m

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from PyQt5 import QtWidgets

from crud_dashboard import Ui_MainWindow as crud


class MainWindow(QMainWindow, crud):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.load_users()
		# self.update_btn.clicked.connect(self.onClicked)
		self.myClient = m.MongoClient("mongodb://localhost:27017")
		print(self.myClient.list_database_names())
		dblist = self.myClient.list_database_names()
		if "test" in dblist:
			print("exist")

		self.db = self.myClient["test"]
		self.user_collection = self.db["user"]
		print(self.db.list_collection_names())

	def load_users(self):
		# for user in self.user_collection.find():
		#     if "username" in user and "password" in user:
		#         row_position = self.tableWidget.rowCount()
		#         self.tableWidget.insertRow(row_position)
		#         self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(user["username"]))
		#         self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(user["password"]))
		self.tableWidget.setColumnCount(1)  # Ensure there is at least 1 column
		self.tableWidget.setHorizontalHeaderLabels(["Number"])  # Optional: Set column header
		for x in range(100):  # Iterates over the range 0 to 99
			row_position = self.tableWidget.rowCount()  # Get current row count
			self.tableWidget.insertRow(row_position)  # Insert a new row at the end
			self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(x)))  # Insert item in column 0

	def check_user(self,email, password):
		user = self.user_collection.find({"email": email, "password": password})
		print(user)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
