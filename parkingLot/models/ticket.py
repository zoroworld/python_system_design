import uuid, time
from .vehicle import Vehicle
from .parking_spot import ParkingSpot

class Ticket:
    def __init__(self, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = str(uuid.uuid4())[:8]
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = time.time()
        self.exit_time = None
        self.fee = 0

    def close_ticket(self):
        self.exit_time = time.time()
        duration = (self.exit_time - self.entry_time) / 60  # minutes
        self.fee = round(duration * self.spot.cost(), 2)
        return self.fee
