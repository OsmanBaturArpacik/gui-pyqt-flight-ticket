from PyQt5.QtWidgets import QMainWindow
from ui.form.dashboard import Ui_dashboard_window
from ui.controller.DbManager import DBManager
from ui.model.ticket_model import TicketModel

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

	def on_clicked_check_pnr(self):
		isExist = self.is_pnr_exist(self.pnr_ln.text())
		self.pnr_ln.clear()
		if isExist is not None:
			self.hide()
			self.main_controller.show_ticket_info()
		else:
			print("cannot find this pnr pop up")


	def on_clicked_check_ticket(self):
		to = self.to_cmbx.currentText()
		fromt = self.from_cmbx.currentText()
		going = self.go_date.text()
		returning = self.return_date.text()
		pass


	def is_pnr_exist(self, pnr):
		pnr = pnr.strip()
		pnr = pnr.upper()
		ticket_info = self.db._ticket_collection.find_one({"pnr": pnr})
		if ticket_info is not None:
			self.main_controller.current_ticket = TicketModel(
				id=ticket_info["_id"],
				user_id=ticket_info["user_id"],
				flight_id=ticket_info["flight_id"],
				pnr=ticket_info["pnr"],
				booking_date=ticket_info["booking_date"],
				status=ticket_info["status"],
				passenger_details=ticket_info["passenger_details"]
			)
		else:
			return None
		return ticket_info