from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer

# Scenario 1: A Car Is Parked Legally
print("--- Scenario 1: Car Parked Legally ---")
car1 = ParkedCar("Toyota", "Camry", "Red", "XYZ123")
car1.minutes_parked = 30
meter1 = ParkingMeter(40)
officer1 = PoliceOfficer("John Doe", "5678")

ticket1 = officer1.inspect_car(car1, meter1)
if ticket1:
    print(ticket1)
else:
    print(f"No ticket issued. Car is legally parked. ({car1.minutes_parked} mins parked vs {meter1.minutes_purchased} mins purchased)\n")

# Scenario 2: A Car Is Parked Illegally (Less Than an Hour Over Time)
print("--- Scenario 2: Car Parked Illegally (short overstay) ---")
car2 = ParkedCar("Honda", "Accord", "Blue", "ABC987")
car2.minutes_parked = 70
meter2 = ParkingMeter(60)
officer2 = PoliceOfficer("Jane Smith", "1234")

ticket2 = officer2.inspect_car(car2, meter2)
if ticket2:
    print(ticket2)
else:
    print("No ticket issued.\n")

# Scenario 3: A Car Is Parked Illegally (Multiple Hours Over Time)
print("--- Scenario 3: Car Parked Illegally (long overstay) ---")
car3 = ParkedCar("Ford", "Mustang", "Black", "LMN456")
car3.minutes_parked = 190
meter3 = ParkingMeter(60)
officer3 = PoliceOfficer("James Brown", "4321")

ticket3 = officer3.inspect_car(car3, meter3)
if ticket3:
    print(ticket3)
else:
    print("No ticket issued.\n")

# Scenario 4: Multiple Cars in a Parking Lot
print("--- Scenario 4: Multiple Cars in a Parking Lot ---")
officer4 = PoliceOfficer("Sarah Green", "9999")

car_meter_pairs = [
    (ParkedCar("Nissan", "Altima", "White", "JKL321"), ParkingMeter(60)), # Legal
    (ParkedCar("Chevy", "Malibu", "Silver", "QWE789"), ParkingMeter(60)), # Illegal (short)
    (ParkedCar("BMW", "X5", "Black", "BMW999"), ParkingMeter(60)),      # Illegal (long)
    (ParkedCar("Mazda", "3", "Blue", "MAZ321"), ParkingMeter(60))        # Legal
]
car_meter_pairs[0][0].minutes_parked = 60
car_meter_pairs[1][0].minutes_parked = 80
car_meter_pairs[2][0].minutes_parked = 500
car_meter_pairs[3][0].minutes_parked = 45

for car, meter in car_meter_pairs:
    ticket = officer4.inspect_car(car, meter)
    if ticket:
        print(ticket)
    else:
        print(f"Officer {officer4.name} inspected car {car.license_number}. No violation. Car legally parked.\n")
