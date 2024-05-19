from abc import ABC
from exceptions import LowFuelError
from exceptions import NotEnoughFuel



class Vehicle(ABC):
    weight: int = 100
    fuel: int = 20
    fuel_consumption: int = 10
    started: bool = False
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self):
        if self.fuel == 0:
            raise LowFuelError
        else:
            self.started = True


    def move(self, distance):
        distance_consumption = (distance / 100) * self.fuel_consumption
        if self.fuel > distance_consumption:
            self.fuel -= distance_consumption
        else:
            raise NotEnoughFuel

def main():
    vehicle = Vehicle()
    print(vehicle.started)
    vehicle.fuel = 0
    print(vehicle.fuel)
    vehicle.start()

if __name__ == '__main__':
    main()
