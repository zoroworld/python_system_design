from abc import ABC
from typing import Optional
from .vehicle_type import VehicleType


class Vehicle(ABC):
    def __init__(self, number: str, vtype: VehicleType):
        self.number = number
        self.vtype = vtype
        self.owner: Optional["User"] = None  # Reference to the user who owns this vehicle

    def assign_owner(self, user: "User"):
        self.owner = user


class Car(Vehicle):
    def __init__(self, number: str):
        super().__init__(number, VehicleType.CAR)


class Bike(Vehicle):
    def __init__(self, number: str):
        super().__init__(number, VehicleType.BIKE)


class Truck(Vehicle):
    def __init__(self, number: str):
        super().__init__(number, VehicleType.TRUCK)


