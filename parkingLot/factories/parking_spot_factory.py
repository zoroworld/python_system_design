from models.parking_spot import SmallSpot, MediumSpot, LargeSpot
from models.vehicle import Vehicle
from models.vehicle_type import VehicleType
from models.parking_spot_type import SpotType

class ParkingSpotFactory:
    def create_spot(self, vehicle: Vehicle, spot_id: str):
        if vehicle.vtype == VehicleType.BIKE:
            return SmallSpot(spot_id)
        elif vehicle.vtype == VehicleType.CAR:
            return MediumSpot(spot_id)
        elif vehicle.vtype == VehicleType.TRUCK:
            return LargeSpot(spot_id)
        else:
            raise ValueError("Unknown vehicle type")
