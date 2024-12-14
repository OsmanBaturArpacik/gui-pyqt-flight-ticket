from PyQt5.QtWidgets import QMainWindow
from ui.form.logged_in_dashboard import Ui_logged_in_dashboard_window
from ui.controller.DbManager import DBManager

class MainWindow(QMainWindow, Ui_logged_in_dashboard_window):
    def __init__(self, main_controller):
        super().__init__()
        self.setupUi(self)

        self.main_controller = main_controller

        self.db = DBManager
        self.db.connect()

        self.logout_btn.clicked.connect(self.on_clicked_logout)

    def initialize_nick(self):
        user = self.main_controller.get_current_user()

        if user:
            self.nickname_label.setText(user.name)
        else:
            print("User bulunamadı.")


    def on_clicked_logout(self):
        self.hide()
        self.main_controller.create_user(None, None)
        self.main_controller.show_dashboard()
