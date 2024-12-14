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
        user = self.get_current_user()

        if user is not None:
            self.main_controller.show_logged_in_dashboard()
        else:
            self.main_controller.show_dashboard()

        # self.main_controller.show_login()
        # user içi boş ise dashboard dön

    def is_pnr_exist(self,pnr):
        pnr = pnr.strip()
        pnr = pnr.upper()
        ticket_info = self.db._ticket_collection.find_one({"pnr": pnr})
        return ticket_info

    def on_clicked_check_pnr(self):
        self.hide()
        self.main_controller.show_ticket()
