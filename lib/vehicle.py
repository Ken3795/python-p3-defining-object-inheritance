class Vehicle:
    def __init__(self, wheel_size, wheel_number):
        # The __init__ method initializes the object with attributes.
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        # The go method should return a "vroom" sound.
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        # The fill_up_tank method returns a message.
        return "filling up!"
