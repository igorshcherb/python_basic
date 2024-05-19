"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    message = 'Low Fuel Error'
class NotEnoughFuel(Exception):
    message = 'Not Enough Fuel'
class CargoOverload(Exception):
    message = 'Cargo Over load'
