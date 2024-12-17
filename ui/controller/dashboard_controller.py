from PyQt5.QtWidgets import QMainWindow
from ui.form.dashboard import Ui_dashboard_window
from ui.controller.DbManager import DBManager
from ui.model.ticket_model import TicketModel
from ui.model.user_model import UserModel


class MainWindow(QMainWindow, Ui_dashboard_window):
	def __init__(self, main_controller):
		super().__init__()
		self.setupUi(self)

		# deprecated
		self.return_date.hide()
		self.label_5.hide()

		self.main_controller = main_controller
		self.db = DBManager
		self.db.connect()

		self.left_bar.hide()
		self.logout_btn.hide()

		self.login_btn.clicked.connect(self.on_clicked_login)
		self.logout_btn.clicked.connect(self.on_clicked_logout)

		self.search_pnr_btn.clicked.connect(self.on_clicked_check_pnr)
		self.search_ticket_btn.clicked.connect(self.on_clicked_search_ticket)
		self.auth = False

	def update_ui_on_auth(self):
		if self.auth is not False:
			self.logout_btn.show()
			self.login_btn.hide()

			self.load_data()
			self.left_bar.show()
		else:
			self.logout_btn.hide()
			self.login_btn.show()
			self.left_bar.hide()

	def on_clicked_login(self):
		self.auth = True
		self.hide()
		self.main_controller.show_login()

	def on_clicked_logout(self):
		self.auth = False
		self.hide()
		self.main_controller.current_user = UserModel(None, None)
		self.main_controller.show_dashboard()

	def load_data(self):
		user = self.main_controller.current_user

		if user:
			self.nickname_label.setText(user.name)
		else:
			print("User bulunamadı.")


	def on_clicked_check_pnr(self):
		isExist = self.is_pnr_exist(self.pnr_ln.text())
		self.pnr_ln.clear()
		if isExist is not None:
			self.hide()
			self.main_controller.show_ticket_info()
		else:
			print("cannot find this pnr pop up")

	def on_clicked_search_ticket(self):
		origin = self.from_cmbx.currentText()
		destination = self.to_cmbx.currentText()
		departure_date = self.get_date(self.go_date)
		return_date = self.get_date(self.go_date)
		# print(origin, destination, departure_date, return_date)


		query = {
			"from": origin,
			"to": destination,
			"departure_date": {"$regex": f"^{departure_date}", "$options": "i"},
		}

		flights = list()
		for flight in self.db._flight_collection.find(query):
			# print(flight)
			flights.append(flight)
		self.res()
		if len(flights) != 0:
			self.main_controller.ticket_list_controller.flight_list = flights
			self.hide()
			self.main_controller.show_ticket_list()
		else:
			print("bulunamadi pop up")



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
