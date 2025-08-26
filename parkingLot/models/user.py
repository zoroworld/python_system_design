from abc import ABC
from .vehicle import Vehicle
from .user_type import UserType


class User(ABC):
    def __init__(self, name: str, description: str, phone: str, address: str, utype: UserType):
        self.name = name
        self.description = description
        self.phone = phone
        self.address = address
        self.utype = utype
        self.vehicles = []  # A user can have multiple vehicles

    def add_vehicle(self, vehicle: Vehicle):
        vehicle.assign_owner(self)  # set reverse relation
        self.vehicles.append(vehicle)

    def get_vehicles(self):
        return self.vehicles
