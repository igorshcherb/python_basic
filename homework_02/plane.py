"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload

class Plane(Vehicle):
    cargo: int
    max_cargo: int

    def __init__(self, weight = 100, started = False, fuel = 20, fuel_consumption = 10, max_cargo = 100):
        super().__init__(weight, started, fuel, fuel_consumption)
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