DEALER_PREP = 1250
DESTINATION_CHARGE = 500
CLEANING_CHARGE = 750

base_car_amount = float(input("Enter the base amount of the car: $"))

car_tax = base_car_amount*.15
licence = base_car_amount*.075

final_amount = DEALER_PREP + DESTINATION_CHARGE + CLEANING_CHARGE + car_tax + licence + base_car_amount
final_amount = "$" + str(round(final_amount, 2))


print("The final amount is", final_amount, sep=" ")
