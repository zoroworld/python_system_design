from abc import ABC
from .gate_type import GateType
from .ticket import Ticket
from .vehicle import Vehicle



class Gate(ABC):
    def __init__(self, gate_id: str, gate_type: GateType):
        self.gate_id = gate_id
        self.gate_type = gate_type


class EntryGate(Gate):
    def __init__(self, gate_id: str, parking_lot: "ParkingLot"):
        super().__init__(gate_id, GateType.ENTRY)
        self.parking_lot = parking_lot

    def issue_ticket(self, vehicle: Vehicle):
        # Find a free spot
        spot, floor = self.parking_lot.find_spot_for_vehicle(vehicle)
        if not spot:
            print(f"❌ No available spot for {vehicle.vtype.name}")
            return None

        # Assign vehicle to spot
        spot.assign_vehicle(vehicle)

        # Create ticket
        ticket = Ticket(vehicle, spot)
        print(f"🎫 Ticket issued: {ticket.ticket_id}, Vehicle: {vehicle.number}, "
              f"Spot: {spot.spot_id} on Floor {floor.floor_no}")
        return ticket


class ExitGate(Gate):
    def __init__(self, gate_id: str):
        super().__init__(gate_id, GateType.EXIT)

    def close_ticket(self, ticket: Ticket):
        fee = ticket.close_ticket()
        ticket.spot.free()
        print(f"🚗 Vehicle {ticket.vehicle.number} exited. Fee = Rs {fee}. Spot {ticket.spot.spot_id} is now FREE.")
        return fee
