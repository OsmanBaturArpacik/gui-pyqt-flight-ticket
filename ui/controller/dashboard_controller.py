
import pymongo as m
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from ui.form.dashboard import Ui_MainWindow as ui_dashboard

class MainWindow(QMainWindow, ui_dashboard):
	def __init__(self, main_controller):
		super().__init__()
		self.setupUi(self)
		# self.pushButton.clicked.connect(self.onClicked)
		self.pushButton.clicked.connect(self.on_clicked_login)

		self.main_controller = main_controller

		#mongo
		self.client = m.MongoClient("mongodb://localhost:27017")
		self.db = self.client["test"]
		self.user_collection = self.db["user"]

	def on_clicked_login(self):
		self.hide()
		self.main_controller.show_login()
		# email = self.lineEdit.text()
		# password = self.lineEdit_2.text()
		# user = self.user_collection.find({"email": email, "password": password})
		# print(user)
		# print("aaaaaa")




# if __name__ == '__main__':
# 	app = QApplication(sys.argv)
# 	window = MainWindow()
# 	window.show()
# 	sys.exit(app.exec_())
