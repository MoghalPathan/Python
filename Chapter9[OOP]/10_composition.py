class Engine:

    def start(self):
        print("Engine  Started")


class Car:

    def __init__(self):
        self.engine = Engine()


    def start_car(self):
        self.engine.start()
        print("Car Started")           


c = Car()

c.start_car()