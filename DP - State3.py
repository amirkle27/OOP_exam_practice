from abc import ABC, abstractmethod
from typing import override

class ParkingLotState(ABC):
    @abstractmethod
    def handle_state(self, parking_lot):
        pass

class ParkingEmpty(ParkingLotState):
    @override
    def handle_state(self, parking_lot):
        print("Parking Lot is empty, you can park your car")
        parking_lot.state = ParkingOccupied()

class ParkingOccupied(ParkingLotState):
    @override
    def handle_state(self, parking_lot):
        print("Parking Lot is occupied, you have to wait until it clears first")
        parking_lot.state = ParkingClearing()

class ParkingClearing(ParkingLotState):
    @override
    def handle_state(self, parking_lot):
        print("A car is just leaving. Try again momentarily to park your car.")
        parking_lot.state = ParkingEmpty()

class ParkingLot:
    def __init__(self):
        self.state = ParkingOccupied()

    def clear_parking_lot(self):
        self.state.handle_state(self)

    def park_car(self):
        self.state.handle_state(self)

    def status(self):
        if isinstance(self.state, ParkingEmpty):
            print("Status: The parking lot is empty.")
        elif isinstance(self.state, ParkingOccupied):
            print("Status: The parking lot is occupied.")
        elif isinstance(self.state, ParkingClearing):
            print("Status: A car is leaving the lot.")

parking_lot = ParkingLot()

parking_lot.park_car()
parking_lot.clear_parking_lot()
parking_lot.park_car()
parking_lot.park_car()
parking_lot.status()