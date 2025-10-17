class ParkingMeter:
    def __init__(self, minutes_purchased=60):
        self.__minutes_purchased = minutes_purchased
        self.minutes_purchased = minutes_purchased # Use setter for validation

    @property
    def minutes_purchased(self):
        return self.__minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, minutes):
        if minutes <= 0:
            raise ValueError("Minutes purchased must be a positive number.")
        self.__minutes_purchased = minutes
