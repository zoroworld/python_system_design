from abc import ABC, abstractmethod
from .parking_spot_type import SpotType
from .vehicle import Vehicle
from .vehicle_type import VehicleType

class ParkingSpot(ABC):
    def __init__(self, spot_id: str, spot_type: SpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_occupied = False
        self.vehicle: Vehicle | None = None  # parked vehicle

    def assign_vehicle(self, vehicle: Vehicle) -> bool:
        """Assign vehicle to this spot if free"""
        if not self.is_occupied and self.can_fit_vehicle(vehicle):
            self.is_occupied = True
            self.vehicle = vehicle
            return True
        return False

    def remove_vehicle(self):
        """Remove vehicle and free the spot"""
        self.is_occupied = False
        self.vehicle = None

    def can_fit_vehicle(self, vehicle: Vehicle) -> bool:
        """Check if this spot type is suitable for the given vehicle"""
        if vehicle.vtype == VehicleType.BIKE and self.spot_type == SpotType.SMALL:
            return True
        if vehicle.vtype == VehicleType.CAR and self.spot_type == SpotType.MEDIUM:
            return True
        if vehicle.vtype == VehicleType.TRUCK and self.spot_type == SpotType.LARGE:
            return True
        return False

    def free(self):
        """Alias for remove_vehicle"""
        self.remove_vehicle()

    @abstractmethod
    def cost(self) -> int:
        pass


class SmallSpot(ParkingSpot):
    def __init__(self, spot_id: str):
        super().__init__(spot_id, SpotType.SMALL)

    def cost(self):
        return 30


class MediumSpot(ParkingSpot):
    def __init__(self, spot_id: str):
        super().__init__(spot_id, SpotType.MEDIUM)

    def cost(self):
        return 80


class LargeSpot(ParkingSpot):
    def __init__(self, spot_id: str):
        super().__init__(spot_id, SpotType.LARGE)

    def cost(self):
        return 120
