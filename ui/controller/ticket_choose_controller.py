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
            self.main_controller.show_ticket_info()

    def on_clicked_any_checkbox(self):
        """
        Handle checkbox click events:
        - If a checkbox is checked, disable all others.
        - If unchecked, re-enable all except checkboxes with modified text (reserved seats).
        """
        # Find the clicked checkbox and check its state
        clicked_checkbox = self.sender()  # The checkbox that triggered this function

        if clicked_checkbox.isChecked():  # Checkbox is checked
            # Get the seat number for the selected checkbox
            for seat_row in range(1, 7):  # Rows 1 to 6
                for seat_col in ["a", "b", "c", "d", "e", "f"]:  # Columns A to F
                    checkbox_name = f"checkbox_{seat_col}{seat_row}"
                    if hasattr(self, checkbox_name):
                        checkbox = getattr(self, checkbox_name)
                        if checkbox == clicked_checkbox:
                            seat_number = f"{seat_col.upper()}{seat_row}"
                            # print(f"Seçilen koltuk: {seat_number}")
                            self.seat_num_ln.setText(seat_number)
                            self.disable_other_checkboxes(checkbox_name)
                            return
        else:  # Checkbox is unchecked
            self.reenable_all_checkboxes_except_reserved()
            self.seat_num_ln.clear()

    def disable_other_checkboxes(self, selected_checkbox_name):
        """
        Disable all checkboxes except the selected one.
        """
        for seat_row in range(1, 7):  # Rows 1 to 6
            for seat_col in ["a", "b", "c", "d", "e", "f"]:  # Columns A to F
                checkbox_name = f"checkbox_{seat_col}{seat_row}"
                if hasattr(self, checkbox_name):
                    checkbox = getattr(self, checkbox_name)
                    if isinstance(checkbox, QCheckBox) and checkbox_name != selected_checkbox_name:
                        checkbox.setDisabled(True)  # Disable other checkboxes

    def reenable_all_checkboxes_except_reserved(self):
        """
        Re-enable all checkboxes except the ones with modified text (reserved seats).
        """
        for seat_row in range(1, 7):  # Rows 1 to 6
            for seat_col in ["a", "b", "c", "d", "e", "f"]:  # Columns A to F
                checkbox_name = f"checkbox_{seat_col}{seat_row}"
                if hasattr(self, checkbox_name):
                    checkbox = getattr(self, checkbox_name)
                    if isinstance(checkbox, QCheckBox):
                        # Re-enable only checkboxes that do not have text (reserved seats remain disabled)
                        if checkbox.text() == "":
                            checkbox.setDisabled(False)
                            
    def initial(self):
        # Tüm checkbox'lara tıklama eventi bağla
        for seat_row in range(1, 7):  # Rows 1 to 6
            for seat_col in ["a", "b", "c", "d", "e", "f"]:  # Columns A to F
                checkbox_name = f"checkbox_{seat_col}{seat_row}"
                if hasattr(self, checkbox_name):
                    checkbox = getattr(self, checkbox_name)
                    if isinstance(checkbox, QCheckBox):
                        checkbox.clicked.connect(self.on_clicked_any_checkbox)
    def load_data(self):
        """
        Load ticket data for a specific flight, disable reserved seats,
        and mark them with passenger gender initials.
        """
        # Fetch reserved tickets for the given flight_id
        id = self.main_controller.current_flight.id
        reserved_tickets = self.db._ticket_collection.find({"flight_id": id})

        # Loop through tickets and process reserved seats
        for ticket in reserved_tickets:
            seat = ticket["passenger_details"]["seat"]  # e.g., "A1"
            gender = ticket["passenger_details"]["gender"]  # e.g., "male"
            gender_initial = "M" if gender.lower() == "male" else "F"

            # Match checkbox dynamically based on seat name
            checkbox_name = f"checkbox_{seat.lower()}"  # e.g., "checkbox_a1"

            if hasattr(self, checkbox_name):  # Check if checkbox exists in the UI
                checkbox = getattr(self, checkbox_name)
                if isinstance(checkbox, QCheckBox):  # Ensure it is a checkbox
                    checkbox.setDisabled(True)  # Disable the checkbox
                    checkbox.setText(gender_initial)  # Add gender initial

            # print(f"Seat {seat} marked as reserved ({gender_initial}).")
