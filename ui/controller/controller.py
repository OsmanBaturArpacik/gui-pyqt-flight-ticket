from PyQt5.QtWidgets import QApplication, QStackedWidget
from ui.controller.dashboard_controller import MainWindow as dashboard_controller
from ui.controller.login_controller import MainWindow as login_controller
import sys

class MainController:
    def __init__(self):
        self.login_controller = login_controller(self)
        self.dashboard_controller = dashboard_controller(self)

    def show_login(self):
        self.login_controller.show()

    def show_dashboard(self):
        self.dashboard_controller.show()

    def run(self):
        self.show_dashboard()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainController()
    main.run()
    # window = MainWindow()
    # window.show()
    sys.exit(app.exec_())