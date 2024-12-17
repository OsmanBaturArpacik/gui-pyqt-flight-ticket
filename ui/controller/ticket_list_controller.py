from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from ui.form.ticket_list import Ui_ticket_list_window
from ui.controller.DbManager import DBManager


class MainWindow(QMainWindow, Ui_ticket_list_window):
    def __init__(self, main_controller):
        super().__init__()
        self.setupUi(self)

        self.main_controller = main_controller
        self.db = DBManager
        self.db.connect()

        self.continue_btn.clicked.connect(self.on_clicked_continue)
        self.tableWidget.cellClicked.connect(self.row_selected)

        self.flight_list = None

    def on_clicked_continue(self):
        self.hide()
        self.main_controller.show_dashboard()
    #  TODO:   choose ticket sayfasına git bilet seç

    def row_selected(self, row, column):
        row_data = []
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, col)
            row_data.append(item.text() if item else "")
        print(f"Seçilen Satır Verileri: {row_data}")
        self.company_ln.setText(row_data[0])
        self.from_ln.setText(row_data[1])
        self.destination_ln.setText(row_data[2])
        self.departure_date_ln.setText(row_data[3])
        self.arrival_date_ln.setText(row_data[4])
        self.seat_num_ln.setText(row_data[5])
        self.price_ln.setText(row_data[6])

    def load_data(self):
        for flight in self.flight_list:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

            self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(flight["airline"]))
            self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(flight["from"]))
            self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(flight["to"]))
            self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(flight["departure_date"]))
            self.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(flight["arrival_date"]))
            self.tableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(str(flight["available_seats"])))
            self.tableWidget.setItem(row_position, 6, QtWidgets.QTableWidgetItem(f"{flight['price']} TL"))

