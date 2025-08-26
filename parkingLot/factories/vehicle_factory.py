from models.vehicle_type import VehicleType
from models.vehicle import Car, Bike, Truck, Vehicle


class VehicleFactory:
    @staticmethod
    def create_vehicle(vtype: VehicleType, number: str) -> Vehicle:
        if vtype == VehicleType.CAR:
            return Car(number)
        elif vtype == VehicleType.BIKE:
            return Bike(number)
        elif vtype == VehicleType.TRUCK:
            return Truck(number)
        else:
            raise ValueError(f"🚨 Unknown VehicleType: {vtype}")
