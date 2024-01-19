# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t\t"))
price_per_gallon = float(input("Enter the price of a gallon of gas:\t"))

# calculate miles per gallon
#mpg = miles_driven / gallons_used
mpg = round(miles_driven / gallons_used, 1)
total_cost = round(gallons_used * price_per_gallon, 2)
cost_per_mile = round(total_cost/miles_driven, 2)
            
# format and display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}")
print()
print(f"Total cost of gas:\t\t{total_cost}")
print()
print(f"Cost per mile:\t\t{cost_per_mile}")
print()
print("Bye!")