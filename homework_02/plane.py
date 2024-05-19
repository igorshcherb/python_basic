"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload

class Plane(Vehicle):
    cargo: int
    max_cargo: int

    def __init__(self, weight = 100, fuel = 20, fuel_consumption = 10, max_cargo = 100):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def load_cargo(self, add_weight):
        if self.cargo + add_weight <= self.max_cargo:
            self.cargo -= add_weight
        else:
            raise CargoOverload('Cargo overload')

    def remove_all_cargo(self):
        cargo_before = self.cargo
        self.cargo = 0
        return cargo_before