
#Function for displaying the menu
def displayGreeting():
    dashes = "*" * 100

    print(f"{dashes}")
    print("Baseball Team Manager")
    displayMenu()
    print(f"{dashes}")



def calculateBattingAverage():
    print("Calcualting batting average...")
    numOfBats = int(input("Official number of at bats: "))
    numOfHits = int(input("Number of hits: "))
    battingAverage = round((numOfHits/numOfBats), 3)
    print(f"batting average is {battingAverage}")

def displayMenu():
    print("Menu Options")
    print("1 - Calcualtae batting average")
    print("2 - Exit Program")

def main():
    displayGreeting()

    while True:
        print()
        userChoice = input("Menu option: ")

        if userChoice == "1":
            calculateBattingAverage()
        elif userChoice == "2":
            print("Bye!")
            exit()
        else:
            print("Not a valid option. Please try again")
            print()
            displayMenu()



if __name__ == "__main__":
    main()