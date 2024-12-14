from typing import List


class PassengerDetails:
    def __init__(self, name: str, surname: str, email: str, age: int, gender: str, seat: str):
        self.name = name
        self.surname = surname
        self.email = email
        self.age = age
        self.gender = gender
        self.seat = seat


class TicketModel:
    def __init__(
        self,
        _id: str,
        user_id: str,
        flight_id: str,
        pnr: str,
        booking_date: str,
        status: str,
        passenger_details: List[dict]
    ):
        self._id = _id
        self.user_id = user_id
        self.flight_id = flight_id
        self.pnr = pnr
        self.booking_date = booking_date
        self.status = status
        self.passenger_details = [PassengerDetails(**details) for details in passenger_details]

    def __str__(self):
        passenger_info = ", ".join([f"{p.name} {p.surname}" for p in self.passenger_details])
        return f"TicketModel(pnr={self.pnr}, status={self.status}, passengers=[{passenger_info}])"

