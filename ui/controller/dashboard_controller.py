from PyQt5.QtWidgets import QMainWindow
from ui.form.dashboard import Ui_dashboard_window
from ui.controller.DbManager import DBManager

class MainWindow(QMainWindow, Ui_dashboard_window):
	def __init__(self, main_controller):
		super().__init__()
		self.setupUi(self)

		self.main_controller = main_controller
		self.db = DBManager
		self.db.connect()

		self.login_btn.clicked.connect(self.on_clicked_login)
		self.search_pnr_btn.clicked.connect(self.on_clicked_check_pnr)

	def on_clicked_login(self):
		self.hide()
		self.main_controller.show_login()
		# email = self.lineEdit.text()
		# password = self.lineEdit_2.text()
		# user = self.user_collection.find({"email": email, "password": password})
		# print(user)
		# print("aaaaaa")

	def on_clicked_check_pnr(self):
		isExist = self.main_controller.ticket_info_controller.is_pnr_exist(self.pnr_ln.text())
		if isExist is not None:
			# Todo:
			# pnr nesnesi olustur main icinde
			# sonra pnr nesnesi olusunca load_pnr gibi bir seyle labelları düzelt easy man
			self.hide()
			self.main_controller.show_ticket_info()
		else:
			print("pop up")


