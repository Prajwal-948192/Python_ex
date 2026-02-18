'''
     get the starting and ending reading of odomter and fuel in the tank before starting the ride and calcualte  mileage
    calcualte the number of stops one need to make while travelling from BLR to GOA with dist of 560KM
'''

ODO_meter1 = int(input( "Please enter the starting reading of car odometer" ))
ODO_meter2 = int(input( "Please enter the ending reading of car odometer" ))
Fuel = float(input( " what the amount of fuel before starting the ride ?" ))
Fuel_tank_capacity = float(input( " what is the fuel tank capacity of your car (liters) ? "))
BLR_GOA_DIST = 560 #km
distance_covered = ODO_meter2 - ODO_meter1
mileage = distance_covered / Fuel
distance_per_tankcapacity = mileage * Fuel_tank_capacity
Total_stops = int(BLR_GOA_DIST / distance_per_tankcapacity)
print( "you have traveled " , distance_covered , "km" , " and your car mileage is " , mileage )
print ( " you can cover the distance of" , distance_per_tankcapacity, "km" , "with" , Fuel_tank_capacity , "liters fuel full tank capacity " )
print( " to travel from Blr to Goa with a distance of 560km, you need to make" , Total_stops , " stops to refuel the full tank " )
