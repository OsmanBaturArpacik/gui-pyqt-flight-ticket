from PyQt5.QtWidgets import QMainWindow
from ui.form.login import Ui_login_window
from ui.controller.DbManager import DBManager

class MainWindow(QMainWindow, Ui_login_window):
    def __init__(self, main_controller):
        super().__init__()
        self.setupUi(self)

        self.main_controller = main_controller

        self.db = DBManager
        self.db.connect()

        self.login_btn.clicked.connect(self.on_clicked_login)


    def on_clicked_login(self):
        email = self.email_ln.text()
        password = self.password_ln.text()

        self.email_ln.clear()
        self.password_ln.clear()

        user = self.db._user_collection.find_one({"email": email, "password": password})

        if user is not None:
            self.main_controller.create_user(email, user["name"])
            self.hide()
            self.main_controller.show_logged_in_dashboard()
        else:
            pass
            # popup