DEALER_PREP = 1250
DESTINATION_CHARGE = 500
CLEANING_CHARGE = 750
TAX_RATE = 0.15
LICENCE_RATE = 0.075

base_car_amount = float(input("Enter the base amount of the car: $"))

car_tax = base_car_amount*TAX_RATE
licence = base_car_amount*LICENCE_RATE

final_amount = DEALER_PREP + DESTINATION_CHARGE + CLEANING_CHARGE + car_tax + licence + base_car_amount


print("The final amount is $", str(final_amount), sep="")
