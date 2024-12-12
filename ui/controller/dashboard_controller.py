from PyQt5.QtWidgets import QMainWindow
from ui.form.dashboard import Ui_dashboard_window as Ui_dashboard_window
from ui.controller.DbManager import DBManager

class MainWindow(QMainWindow, Ui_dashboard_window):
	def __init__(self, main_controller):
		super().__init__()
		self.setupUi(self)
		# self.pushButton.clicked.connect(self.onClicked)
		self.login_btn.clicked.connect(self.on_clicked_login)

		self.main_controller = main_controller

		self.db = DBManager()

	def on_clicked_login(self):
		self.hide()
		self.main_controller.show_login()
		# email = self.lineEdit.text()
		# password = self.lineEdit_2.text()
		# user = self.user_collection.find({"email": email, "password": password})
		# print(user)
		# print("aaaaaa")




