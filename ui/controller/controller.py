from PyQt5.QtWidgets import QApplication
from ui.controller.dashboard_controller import MainWindow as dashboard_controller
from ui.controller.login_controller import MainWindow as login_controller
from ui.controller.logged_in_dashboard_controller import MainWindow as logged_in_dashboard_controller
from ui.controller.ticket_info_controller import MainWindow as ticket_info_controller
from ui.model.user_model import UserModel

class MainController:
    def __init__(self):
        self.app = QApplication([])

        # controller initialize
        self.login_controller = login_controller(self)
        self.dashboard_controller = dashboard_controller(self)
        self.logged_in_dashboard_controller = logged_in_dashboard_controller(self)
        self.ticket_info_controller = ticket_info_controller(self)



        # model initialize
        self.current_user = None


    # show methods
    def show_login(self):
        self.login_controller.show()

    def show_dashboard(self):
        self.dashboard_controller.show()

    def show_logged_in_dashboard(self):
        self.logged_in_dashboard_controller.initialize_nick()
        self.logged_in_dashboard_controller.show()

    def show_ticket_info(self):
        self.ticket_info_controller.show()

    # model methods
    def create_user(self, email, name):
        self.current_user = UserModel(email, name)

    def get_current_user(self):
        return self.current_user



    # run method
    def run(self):
        self.show_dashboard()
        return self.app.exec_()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main = MainController()
#     main.run()
#     sys.exit(app.exec_())