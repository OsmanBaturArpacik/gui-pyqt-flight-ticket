
class FlightModel:
    def __init__(self, id, company, from_location, destination, departure_date, arrival_date, available_seats, price):
        self.id = id
        self.company = company
        self.from_location = from_location
        self.destination = destination
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.available_seats = available_seats
        self.price = price

    def __repr__(self):
        return (f"FlightModel(company={self.company}, from={self.from_location}, "
                f"destination={self.destination}, departure_date={self.departure_date}, "
                f"arrival_date={self.arrival_date}, seat_num={self.available_seats}, price={self.price})")