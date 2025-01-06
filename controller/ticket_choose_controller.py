from PyQt5.QtWidgets import QMainWindow, QCheckBox
from ui.form.ticket_choose import Ui_ticket_choose_window
from ui.controller.DbManager import DBManager
from ui.model.ticket_model import TicketModel
import random
import string
from datetime import datetime

class MainWindow(QMainWindow, Ui_ticket_choose_window):
    def __init__(self, main_controller):
        super().__init__()
        self.setupUi(self)

        self.main_controller = main_controller
        self.db = DBManager
        self.db.connect()

        self.buy_ticket_btn.clicked.connect(self.on_clicked_buy)

        self.initial()

    def on_clicked_buy(self):
        if not self.name_ln.text().strip() or not self.surname_ln.text().strip() or not self.email_ln.text().strip() or not self.age_ln.text().strip() or not self.seat_num_ln.text().strip():
            print("pop up bos birakmayin")
        else:
            name = self.name_ln.text()
            surname = self.surname_ln.text()
            email = self.email_ln.text()
            age = self.age_ln.text()
            seat_num = self.seat_num_ln.text()
            gender = self.gender_cmbx.currentText()
            pnr = ''.join(random.choices(string.digits, k=4)) + ''.join(random.choices(string.ascii_uppercase, k=2))
            booking_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            ticket_data = {
                "user_id": self.main_controller.current_user.id,
                "flight_id": self.main_controller.current_flight.id,
                "pnr": pnr,
                "booking_date": booking_date,
                "status": "booked",
                "passenger_details": {
                    "name": name,
                    "surname": surname,
                    "email": email,
                    "age": age,
                    "gender": gender,
                    "seat": seat_num
                }
            }
            inserted_doc = self.db._ticket_collection.insert_one(ticket_data)

            self.main_controller.current_ticket = TicketModel(
                id=inserted_doc.inserted_id,
                user_id=ticket_data["user_id"],
                flight_id=ticket_data["flight_id"],
                pnr=ticket_data["pnr"],
                booking_date=ticket_data["booking_date"],
                status=ticket_data["status"],
                passenger_details=ticket_data["passenger_details"]
            )
            available_seats = self.main_controller.current_flight.available_seats
            self.db._flight_collection.update_one({"_id": self.main_controller.current_flight.id},{"$set": {"available_seats" : int(available_seats - 1)}})

            self.hide()
            self.clear_selections()
            self.main_controller.show_ticket_info()

    def on_clicked_any_checkbox(self):
        clicked_checkbox = self.sender()

        if clicked_checkbox.isChecked():
            for seat_row in range(1, 7):
                for seat_col in ["a", "b", "c", "d", "e", "f"]:
                    checkbox_name = f"checkbox_{seat_col}{seat_row}"
                    if hasattr(self, checkbox_name):
                        checkbox = getattr(self, checkbox_name)
                        if checkbox == clicked_checkbox:
                            seat_number = f"{seat_col.upper()}{seat_row}"
                            # print(f"Seçilen koltuk: {seat_number}")
                            self.seat_num_ln.setText(seat_number)
                            self.disable_other_checkboxes(checkbox_name)
                            return
        else:
            self.reenable_all_checkboxes_except_reserved()
            self.seat_num_ln.clear()

    def disable_other_checkboxes(self, selected_checkbox_name):
        for seat_row in range(1, 7):
            for seat_col in ["a", "b", "c", "d", "e", "f"]:
                checkbox_name = f"checkbox_{seat_col}{seat_row}"
                if hasattr(self, checkbox_name):
                    checkbox = getattr(self, checkbox_name)
                    if isinstance(checkbox, QCheckBox) and checkbox_name != selected_checkbox_name:
                        checkbox.setDisabled(True)

    def reenable_all_checkboxes_except_reserved(self):
        for seat_row in range(1, 7):
            for seat_col in ["a", "b", "c", "d", "e", "f"]:
                checkbox_name = f"checkbox_{seat_col}{seat_row}"
                if hasattr(self, checkbox_name):
                    checkbox = getattr(self, checkbox_name)
                    if isinstance(checkbox, QCheckBox):
                        if checkbox.text() == "":
                            checkbox.setDisabled(False)

    def initial(self):
        for seat_row in range(1, 7):
            for seat_col in ["a", "b", "c", "d", "e", "f"]:
                checkbox_name = f"checkbox_{seat_col}{seat_row}"
                if hasattr(self, checkbox_name):
                    checkbox = getattr(self, checkbox_name)
                    if isinstance(checkbox, QCheckBox):
                        checkbox.clicked.connect(self.on_clicked_any_checkbox)

    def load_data(self):
        id = self.main_controller.current_flight.id
        reserved_tickets = self.db._ticket_collection.find({"flight_id": id})

        for ticket in reserved_tickets:
            seat = ticket["passenger_details"]["seat"]
            gender = ticket["passenger_details"]["gender"]
            gender_initial = "M" if gender.lower() == "male" else "F"

            checkbox_name = f"checkbox_{seat.lower()}"

            if hasattr(self, checkbox_name):
                checkbox = getattr(self, checkbox_name)
                if isinstance(checkbox, QCheckBox):
                    checkbox.setDisabled(True)
                    checkbox.setText(gender_initial)

            # print(f"Seat {seat} marked as reserved ({gender_initial}).")
