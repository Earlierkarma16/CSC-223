class ParkedCar:
    def __init__(self, make, model, color, license_number):
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self.__minutes_parked = 60

    @property
    def minutes_parked(self):
        return self.__minutes_parked

    @minutes_parked.setter
    def minutes_parked(self, minutes):
        if minutes <= 0:
            raise ValueError("Minutes parked must be a positive number.")
        self.__minutes_parked = minutes

    def __str__(self):
        return (f"Car: {self.make} {self.model}\n"
                f"Color: {self.color}\n"
                f"License: {self.license_number}\n"
                f"Minutes Parked: {self.minutes_parked}")
