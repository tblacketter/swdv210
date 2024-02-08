#!/usr/bin/env python3
import csv
import pickle

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")  
      
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
  
    return gallons_used

def write_trips(tripList: []):
    with open("trips7_2.bin", "wb") as file:
        pickle.dump(tripList, file)

def read_trips()->[]:

    try:
        with open("trips7_2.bin", "rb") as file:
            tripList = pickle.load(file)
        
        return tripList
    except:
        return []

    
def list_trips(tripList: []):
    print("Distance,\tGallons,\tMPG")
    for list in tripList:
        print(f"{list[0]}\t\t{list[1]}\t\t{list[2]}")

def main():

    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    more = "y"
    while more.lower() == "y":

        tripList = read_trips()
        list_trips(tripList)
        

        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)

        tripList.append([miles_driven, gallons_used, mpg])

        write_trips(tripList)

        print(f"Miles Per Gallon:\t{mpg}")
        print()
        
        more = input("More entries? (y or n): ")
    
    print("Bye! \n")

if __name__ == "__main__":
    main()

