from PyQt5.QtWidgets import QMainWindow
from ui.form.login import Ui_login_window
from ui.controller.DbManager import DBManager
from ui.model.user_model import UserModel

class MainWindow(QMainWindow, Ui_login_window):
    def __init__(self, main_controller):
        super().__init__()
        self.setupUi(self)

        self.main_controller = main_controller

        self.db = DBManager
        self.db.connect()

        self.login_btn.clicked.connect(self.on_clicked_login)
        self.hide_state = False


    def on_clicked_login(self):
        email = self.email_ln.text()
        password = self.password_ln.text()

        self.res()

        user = self.db._user_collection.find_one({"email": email, "password": password})

        if user is not None:
            self.main_controller.current_user = UserModel(user["_id"],email, user["name"])
            self.main_controller.auth = True
            self.hide()
            if self.hide_state is not False:
                self.hide_state = False
            else:
                self.main_controller.show_dashboard()

        else:
            pass
            # popup