import sys
#Creates a variable for each type of car rental

rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")

#Creates inputs for the customer based on type of car rental

if rentalCode == "B" or rentalCode == "D":
  rentalPeriod = int(input("Number of Days Rented:\n"))
else:
  rentalPeriod = int(input("Number of Weeks Rented:\n"))

#Pricing based on each type of rental

budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00

#Creates each base charge for each type of rental

if rentalCode == "B":
  baseCharge = rentalPeriod * budget_charge
elif rentalCode == "D":
  baseCharge = rentalPeriod * daily_charge
elif rentalCode == "W":
  baseCharge = rentalPeriod * weekly_charge
  
#Creates inputs for starting, ending, and total milage for the rental 

odoStart = int(input("Starting Odometer Reading:\n"))

odoEnd = int(input("Ending Odometer Reading:\n"))

totalMiles = int(odoEnd) - int(odoStart)

#Creates the milage charge for each type of rental

if rentalCode == "B":
  mileCharge = 0.25 * totalMiles
elif rentalCode == "D":
  averageDayMiles = int(totalMiles) / int(rentalPeriod)
  if averageDayMiles <= 100:
    totalMiles = 0
  elif averageDayMiles > 100:
    extraMiles = averageDayMiles - 100
  mileCharge = 0.25 * extraMiles
elif rentalCode == "W" and averageDayMiles > 900:
  mileCharge = rentalPeriod * 100
elif rentalCode == "W" and averageDayMiles <= 900:
  mileCharge = 0

#Gives a variable for the amount due for the customer

amtDue = int(baseCharge) + int(mileCharge)

#Prints out the final rental summary for the customer  

print("Rental Summary")
print("Rental Code: " + str(rentalCode))
print("Rental Period: " + str(rentalPeriod))
print("Starting Odometer: " + str(odoStart))
print("Ending Odometer: " + str(odoEnd))
print("Miles Driven: " + str(totalMiles))
print("Amount Due: " + str(amtDue))