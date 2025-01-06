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
        id: str,
        user_id: str,
        flight_id: str,
        pnr: str,
        booking_date: str,
        status: str,
        passenger_details: dict
    ):
        self.id = id
        self.user_id = user_id
        self.flight_id = flight_id
        self.pnr = pnr
        self.booking_date = booking_date
        self.status = status
        self.passenger_details = PassengerDetails(
            name=passenger_details["name"],
            surname=passenger_details["surname"],
            email=passenger_details["email"],
            age=passenger_details["age"],
            gender=passenger_details["gender"],
            seat=passenger_details["seat"]
        )


    def __str__(self):
        passenger_info = f"{self.passenger_details.name} {self.passenger_details.surname}"
        return f"TicketModel(pnr={self.pnr}, status={self.status}, passenger={passenger_info})"