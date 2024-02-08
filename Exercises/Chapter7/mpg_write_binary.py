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

def main():
    triplist = [["Distance", "Gallons", "MPG"]]
    distanceList = []
    gallonsList = []
    mpgList = []

    # display a welcome message
    print("The Miles Per Gallon program")
    print()


    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)

        mpgList.append(mpg)
        distanceList.append(miles_driven) 
        gallonsList.append(gallons_used)  

        print(f"Miles Per Gallon:\t{mpg}")
        print()
        
        more = input("More entries? (y or n): ")
    
    triplist.append(distanceList)
    triplist.append(gallonsList)
    triplist.append(mpgList)
    print("Bye! \n")
    
    #write the binary file
    with open("trips7_1.bin", "wb") as file:
        pickle.dump(triplist, file)

    #Test that the binary file is readable
    with open("trips7_1.bin", "rb") as file:
        contents = pickle.load(file)
        print(contents)
        


if __name__ == "__main__":
    main()

