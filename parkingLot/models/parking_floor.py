from .parking_spot import ParkingSpot

class ParkingFloor:
    def __init__(self, floor_no: int):
        self.floor_no = floor_no
        self.spots: dict[str, ParkingSpot] = {}

    def add_spot(self, spot: ParkingSpot):
        self.spots[spot.spot_id] = spot

    def get_all_spots(self):
        return list(self.spots.values())

    def get_available_spot_for_vehicle(self, vehicle):
        """Return the first free spot that can fit the vehicle"""
        for spot in self.spots.values():
            if not spot.is_occupied and spot.can_fit_vehicle(vehicle):
                return spot
        return None
