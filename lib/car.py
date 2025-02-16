from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, wheel_size, wheel_number):
        # Car inherits from Vehicle and calls the parent constructor.
        super().__init__(wheel_size, wheel_number)

    def go(self):
        # Overriding the go method to make a different "vroom" sound.
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
