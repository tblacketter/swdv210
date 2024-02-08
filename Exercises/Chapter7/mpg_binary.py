#!/usr/bin/env python3
import csv

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")  
      
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
  
    return gallons_used

def write_trips(tripList: []):
    with open("trips7_2.bin", "a", newline="") as file:
        writer = csv.writer(file, delimiter="\t")
        writer.writerows(tripList)

def read_trips()->[]:
    tempTripList = []
    try:
        with open("trips7_2.bin", "r", newline="") as file:
            reader = csv.reader(file, delimiter="\t")
            for row in reader:
                tempTripList.append(row)
        
        return tempTripList
    except:
        tempTripList = [["Dist", "Gallons", "MPG"]]
        with open("trips7_2.bin", "w", newline="") as file:
            writer = csv.writer(file, delimiter="\t")
            writer.writerows(tempTripList)

        return tempTripList
    
def list_trips(tripList: []):
    for list in tripList:
        tempString = ""
        for x in range(len(list)):
            tempString += (list[x] + "\t")

        print(tempString)

def main():

    tripList = []

    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    more = "y"
    while more.lower() == "y":

        tempTripList = []

        tripList = read_trips()
        list_trips(tripList)
        

        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)

        tempTripList.append([miles_driven, gallons_used, mpg])

        write_trips(tempTripList)

        print(f"Miles Per Gallon:\t{mpg}")
        print()
        
        more = input("More entries? (y or n): ")
    
    print("Bye! \n")

if __name__ == "__main__":
    main()

