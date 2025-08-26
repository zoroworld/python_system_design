from .parking_floor import ParkingFloor
from .gate import EntryGate, ExitGate
from .vehicle import Vehicle

class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.floors: list[ParkingFloor] = []
        self.entry_gates: list[EntryGate] = []
        self.exit_gates: list[ExitGate] = []

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def add_entry_gate(self, gate: EntryGate):
        self.entry_gates.append(gate)

    def add_exit_gate(self, gate: ExitGate):
        self.exit_gates.append(gate)

    def find_spot_for_vehicle(self, vehicles: Vehicle):
        for floor in self.floors:
            for spot in floor.spots.values():
                if not spot.is_occupied and spot.can_fit_vehicle(vehicles):
                    return spot, floor   # ✅ return both spot and floor
        return None, None
