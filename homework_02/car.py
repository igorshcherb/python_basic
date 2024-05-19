"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02 import base
from homework_02 import engine

class Car(base.Vehicle):
    engine: engine.Engine

    def set_engine(self, engine):
        self.engine = engine

def main():
    car = Car(100, 20, 2)
    print(car)

if __name__ == '__main__':
    main()