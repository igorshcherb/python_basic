from abc import ABC
from homework_02 import exceptions


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
            raise exceptions.LowFuelError
        else:
            self.started = True


    def move(self, distance):
        distance_consumption = distance * self.fuel_consumption
        if self.fuel >= distance_consumption:
            self.fuel -= distance_consumption
        else:
            raise exceptions.NotEnoughFuel

def main():
    vehicle = Vehicle(100, 20,2)
    # print(vehicle.started)
    # vehicle.fuel = 0
    # print(vehicle.fuel)
    # vehicle.start()
    print(vehicle.fuel)
    vehicle.move(5)
    print(vehicle.fuel)

if __name__ == '__main__':
    main()
