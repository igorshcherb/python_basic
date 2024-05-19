"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02 import base
from homework_02 import engine

class Car(Vehicle):
    engine: base.Engine

    def set_engine(self, engine: engine.Engine):
        self.engine = engine

def main():
    car = Car(100, 20, 2)
    print(car)

if __name__ == '__main__':
    main()