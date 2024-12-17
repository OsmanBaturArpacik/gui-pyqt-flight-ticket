from PyQt5.QtWidgets import QMainWindow, QCheckBox
from ui.form.ticket_choose import Ui_ticket_choose_window
from ui.controller.DbManager import DBManager


class MainWindow(QMainWindow, Ui_ticket_choose_window):
    def __init__(self, main_controller):
        super().__init__()
        self.setupUi(self)

        self.main_controller = main_controller
        self.db = DBManager
        self.db.connect()

        self.buy_ticket_btn.clicked.connect(self.on_clicked_buy)

        self.load_data()

    def on_clicked_buy(self):
        self.hide()
        self.main_controller.show_dashboard()

    def on_clicked_any_checkbox(self):
        """
        When any checkbox is clicked:
        - Print the seat number of the selected checkbox.
        - Disable all other checkboxes except the selected one.
        """
        # Loop through all attributes to find checkboxes
        for seat_row in range(1, 7):  # Rows 1 to 6
            for seat_col in ["a", "b", "c", "d", "e", "f"]:  # Columns A to F
                checkbox_name = f"checkbox_{seat_col}{seat_row}"
                if hasattr(self, checkbox_name):
                    checkbox = getattr(self, checkbox_name)
                    if isinstance(checkbox, QCheckBox):
                        # Check if this checkbox is checked
                        if checkbox.isChecked():
                            # Print the seat number
                            seat_number = f"{seat_col.upper()}{seat_row}"
                            print(f"Seçilen koltuk: {seat_number}")
                            # TODO: seat_num_ln içine yaz ve bu seçilen eğer uncheck yapılırsa da her şeyi geri aktif et içinde text yazılanlar hariç seat_num_ln'ı da clearla

                            # Disable all other checkboxes
                            self.disable_other_checkboxes(checkbox_name)
                            return
    # disable all checkbox except one

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

    def load_data(self):
        """
        Load ticket data for a specific flight, disable reserved seats,
        and mark them with passenger gender initials.
        """
        # Fetch reserved tickets for the given flight_id
        reserved_tickets = self.db._ticket_collection.find({"flight_id": "675ab979d77e01216927072b"})

        # Loop through tickets and process reserved seats
        for ticket in reserved_tickets:
            # Tüm checkbox'lara tıklama eventi bağla
            for seat_row in range(1, 7):  # Rows 1 to 6
                for seat_col in ["a", "b", "c", "d", "e", "f"]:  # Columns A to F
                    checkbox_name = f"checkbox_{seat_col}{seat_row}"
                    if hasattr(self, checkbox_name):
                        checkbox = getattr(self, checkbox_name)
                        if isinstance(checkbox, QCheckBox):
                            checkbox.clicked.connect(self.on_clicked_any_checkbox)

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

            print(f"Seat {seat} marked as reserved ({gender_initial}).")
    # seatleri seçeceksin önceden pasife alacaksın falan karmaşık algoritma