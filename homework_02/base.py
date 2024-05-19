from abc import ABC
from exceptions import LowFuelError
from exceptions import NotEnoughFuel

class Vehicle(ABC):
    weight: int = 100
    started: bool = False
    fuel: int = 20
    fuel_consumption: int = 10
def __init__(self, weight, started, fuel, fuel_consumption):
    self.weight = weight
    self.started = started
    self.fuel = fuel
    self.fuel_consumption = fuel_consumption

def start(self):
    if not self.started:
        if self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError('Low fuel')
def move(self, distance):
    distance_consumption = (distance / 100) * self.fuel_consumption
    if self.fuel > distance_consumption:
        self.fuel -= distance_consumption
    else:
        raise NotEnoughFuel('Not enough fuel')

