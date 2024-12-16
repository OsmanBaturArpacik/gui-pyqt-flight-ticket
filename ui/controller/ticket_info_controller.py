from PyQt5.QtWidgets import QMainWindow
from ui.form.ticket_info import Ui_ticket_info_window
from ui.controller.DbManager import DBManager


class MainWindow(QMainWindow, Ui_ticket_info_window):
    def __init__(self, main_controller):
        super().__init__()
        self.setupUi(self)

        self.main_controller = main_controller
        self.db = DBManager
        self.db.connect()

        self.continue_btn.clicked.connect(self.on_clicked_continue)

    def on_clicked_continue(self):
        self.hide()
        user = self.main_controller.current_user

        if user is not None:
            self.main_controller.show_logged_in_dashboard()
        else:
            self.main_controller.show_dashboard()


    def on_clicked_check_pnr(self):
        self.hide()
        self.main_controller.show_ticket()


    def load_data(self):
        ticket = self.main_controller.current_ticket
        passenger = ticket.passenger_details
        if ticket is not None:
            self.name_ln.setText(passenger.name)
            self.surname_ln.setText(passenger.surname)
            self.email_ln.setText(passenger.email)
            self.age_ln.setText(str(passenger.age))
            self.gender_cmbx.setCurrentText(passenger.gender)
            self.seat_num_ln.setText(passenger.seat)

            # PNR bilgisi
            self.pnr_num_ln.setText(ticket.pnr)
