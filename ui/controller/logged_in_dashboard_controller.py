# from PyQt5.QtWidgets import QMainWindow
# from ui.form.logged_in_dashboard import Ui_logged_in_dashboard_window as bb
# from ui.form.dashboard import Ui_MainWindow as Ui_logged_in_dashboard_window
# from ui.controller.DbManager import DBManager
# from ui.model.user_model import UserModel
#
# class MainWindow(QMainWindow, Ui_logged_in_dashboard_window):
#     def __init__(self, main_controller):
#         super().__init__()
#         self.setupUi(self)
#
#         self.main_controller = main_controller
#
#         self.db = DBManager
#         self.db.connect()
#
#         self.logout_btn.clicked.connect(self.on_clicked_logout)
#         self.search_pnr_btn.clicked.connect(lambda: self.left_bar.show() if not self.left_bar.isVisible() else self.left_bar.hide())
#         self.left_bar.hide()
#
#
#     def load_data(self):
#         user = self.main_controller.current_user
#
#         if user:
#             self.nickname_label.setText(user.name)
#         else:
#             print("User bulunamadı.")
#
#
#     def on_clicked_logout(self):
#         self.hide()
#         self.main_controller.current_user = UserModel(None, None)
#         self.main_controller.show_dashboard()
