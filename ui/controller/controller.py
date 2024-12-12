from PyQt5.QtWidgets import QApplication
from ui.controller.dashboard_controller import MainWindow as dashboard_controller
from ui.controller.login_controller import MainWindow as login_controller


class MainController:
    def __init__(self):
        self.app = QApplication([])
        self.login_controller = login_controller(self)
        self.dashboard_controller = dashboard_controller(self)

    def show_login(self):
        self.login_controller.show()

    def show_dashboard(self):
        self.dashboard_controller.show()

    def show_logged_in_dashboard(self):
        # self.logged_in_dashboard_controller.show()
        pass

    def run(self):
        self.show_dashboard()
        return self.app.exec_()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main = MainController()
#     main.run()
#     sys.exit(app.exec_())