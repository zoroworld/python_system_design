from models.parking_lot import ParkingLot
from models.parking_floor import ParkingFloor
from models.user import User, UserType
from models.gate import Gate, EntryGate, ExitGate
from factories.vehicle_factory import VehicleFactory
from factories.parking_spot_factory import ParkingSpotFactory
from models.parking_spot import SpotType
from models.vehicle_type import VehicleType


def main():
    # 1. Create Parking Lot
    lot = ParkingLot("MyMall Parking")

    # 2. Create Vehicles using Factory
    car = VehicleFactory.create_vehicle(VehicleType.CAR, "DL01AB1234")
    bike = VehicleFactory.create_vehicle(VehicleType.BIKE, "DL02XY5678")
    truck = VehicleFactory.create_vehicle(VehicleType.TRUCK, "DL02XY5689")

    # 3. Add floor with spots using Factory
    floor1 = ParkingFloor(1)
    parking_spot_factory = ParkingSpotFactory()
    floor1.add_spot(parking_spot_factory.create_spot(car, "S1"))  # Bike
    floor1.add_spot(parking_spot_factory.create_spot(bike, "S2"))  # Car
    floor1.add_spot(parking_spot_factory.create_spot(truck, "S3"))  # Truck
    lot.add_floor(floor1)

    # 4. Create User
    user1 = User("Rahul", "Customer", "9876543210", "Delhi", UserType.CUSTOMER)
    user2 = User("amit", "Customer", "9876543280", "Mumbai", UserType.CUSTOMER)

    # 5. add user with vehicle
    user1.add_vehicle(car)
    user2.add_vehicle(bike)

    # 5. Entry Gate
    entry_gate = EntryGate("G1", lot)
    vehicles = [user1.vehicles, user2.vehicles]
    tickets = {}
    for user_vehicles in vehicles:
        for user_vehicle in user_vehicles:
            ticket = entry_gate.issue_ticket(user_vehicle)
            tickets[ticket.ticket_id] = ticket


    # 6. Exit Gate
    see_ticket_to_exit = input("Enter Ticket Id: ")
    print(see_ticket_to_exit)
    if  see_ticket_to_exit in tickets:
        exit_gate = ExitGate("G2")
        ticket = tickets[see_ticket_to_exit]
        exit_gate.close_ticket(ticket)
        del tickets[see_ticket_to_exit]
    else:
        print("❌ Invalid Ticket ID")



if __name__ == "__main__":
    main()