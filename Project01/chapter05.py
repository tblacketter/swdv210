#Function for displaying the menu
def displayGreeting():
    dashes = "*" * 100

    print(f"{dashes}")
    print("Baseball Team Manager")
    displayMenu()
    print(f"{dashes}")

def displayMenu():
    print("Menu Options")
    print("1 - Calcualtae batting average")
    print("2 - Exit Program")

def calculateBattingAverage(bats: int, hits: int) -> int:
    battingAverage = round((bats/hits), 3)
    return battingAverage

def getNumOfHits()->int:
    numOfHits = int(input("Number of hits: "))
    while numOfHits < 0 or numOfHits > 1000:
        print("Hits must be greater than 0 and less than 1000")
        numOfHits = int(input("Number of hits: "))

    return numOfHits

def getNumOfBats()->int:
    numOfBats = int(input("Official number of at bats: "))
    while numOfBats < 0 or numOfBats > 1000:
        print("Bats must be greater than 0 and less than 1000")
        numOfBats = int(input("Number of hits: "))

    return numOfBats

def main():

    displayGreeting()

    while True:
        print()
        userChoice = input("Menu option: ")

        if userChoice == "1":
            print("Calcualting batting average...")
            bats = getNumOfBats()
            hits = getNumOfHits()
            control = 0

            while control == 0:
                if hits > bats:
                    print("You cant have mor hits than bats...")
                    bats = getNumOfBats()
                    hits = getNumOfHits()
                else:
                    control = 1

            average = calculateBattingAverage(bats, hits)
            print(f"batting average is {average}")
        elif userChoice == "2":
            print("Bye!")
            exit()
        else:
            print("Not a valid option. Please try again")



if __name__ == "__main__":
    main()