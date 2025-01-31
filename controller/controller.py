from PyQt5.QtWidgets import QApplication
from ui.controller.dashboard_controller import MainWindow as dashboard_controller
from ui.controller.login_controller import MainWindow as login_controller
from ui.controller.ticket_info_controller import MainWindow as ticket_info_controller
from ui.controller.ticket_list_controller import MainWindow as ticket_list_controller
from ui.controller.ticket_choose_controller import MainWindow as ticket_choose_controller

class MainController:
    def __init__(self):
        self.app = QApplication([])

        self.current_user = None
        self.current_ticket = None
        self.current_flight = None
        self.auth = False

        # controller initialize
        self.login_controller = login_controller(self)
        self.dashboard_controller = dashboard_controller(self)
        self.ticket_info_controller = ticket_info_controller(self)
        self.ticket_list_controller = ticket_list_controller(self)
        self.ticket_choose_controller = ticket_choose_controller(self)


    # show methods
    def show_login(self):
        self.login_controller.show()

    def show_dashboard(self):
        self.dashboard_controller.update_ui_on_auth()
        self.dashboard_controller.show()

    def show_ticket_info(self):
        self.ticket_info_controller.load_data()
        self.ticket_info_controller.show()

    def show_ticket_list(self):
        self.ticket_list_controller.load_data()
        self.ticket_list_controller.show()

    def show_ticket_choose(self):
        self.ticket_choose_controller.load_data()
        self.ticket_choose_controller.show()

    # run method
    def run(self):
        self.show_dashboard()
        return self.app.exec_()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main = MainController()
#     main.run()
#     sys.exit(app.exec_())