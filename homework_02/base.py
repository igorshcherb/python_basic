from abc import ABC
from exceptions import LowFuelError
from exceptions import NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight: int = 100, fuel: int = 20, fuel_consumption: int = 10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started=False


    def start(self):
        if not self.started:
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
