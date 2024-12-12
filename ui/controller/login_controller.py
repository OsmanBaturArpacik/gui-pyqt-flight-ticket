import pymongo as m
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from ui.form.login import Ui_MainWindow as ui_login


class MainWindow(QMainWindow, ui_login):
    def __init__(self, main_controller):
        super().__init__()
        self.setupUi(self)

        self.maincontroller = main_controller

        # mongo
        self.client = m.MongoClient("mongodb://localhost:27017")
        self.db = self.client["test"]
        self.user_collection = self.db["user"]

