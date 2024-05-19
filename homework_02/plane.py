"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02 import base
from homework_02 import exceptions

class Plane(base.Vehicle):
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
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        cargo_before = self.cargo
        self.cargo = 0
        return cargo_before