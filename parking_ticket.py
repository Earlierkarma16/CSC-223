import math

class ParkingTicket:
    def __init__(self, car, officer, illegal_minutes):
        self.car = car
        self.officer_name = officer.name
        self.badge_number = officer.badge_number
        self.illegal_minutes = illegal_minutes
        self.fine = self.calculate_fine()

    def calculate_fine(self):
        if self.illegal_minutes <= 0:
            return 0.0
        
        # $25 for the first hour or part of an hour
        fine = 25.0
        
        # Calculate additional hours
        if self.illegal_minutes > 60:
            additional_minutes = self.illegal_minutes - 60
            additional_hours = math.ceil(additional_minutes / 60)
            fine += additional_hours * 10.0
            
        return fine

    def __str__(self):
        return (f"*** PARKING TICKET ***\n"
                f"{str(self.car)}\n"
                f"Illegally Parked: {self.illegal_minutes} minutes\n"
                f"Fine: ${self.fine:.2f}\n"
                f"Officer: {self.officer_name}, Badge #: {self.badge_number}\n"
                f"**********************")
