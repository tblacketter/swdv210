POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
DASHES = "=" * 100
S1 = 20
S2 = ">10"
S3 = "<3"

#Function for displaying the menu
def displayGreeting():

    print(f"{DASHES}")
    print("Baseball Team Manager")
    displayMenu()
    print()
    displayPositions()
    print(f"{DASHES}")

def displayMenu():
    print("Menu Options")
    print("1 - Display Lineup")
    print("2 - Add Player")
    print("3 - Remove Player")
    print("4 - Move Player")
    print("5 - Edit Player Position")
    print("6 - Edit Player Stats")
    print("7 - Exit Program")

# playersList = [[name, position, atBats, Hits], ]

#The list functions

#displays the lineup of the players list
def displayLineup(players:list):
    print(f"{' ':{S3}}{'Player':{S1}}{'POS':{S2}}{'AB':{S2}}{'H':{S2}}{'AVG':{S2}}")
    print(f"{DASHES}")
    for player in players:
        print(f"{player[0] + 1:{S3}}{player[1]:{S1}}{player[2]:{S2}}{player[3]:{S2}}{player[4]:{S2}}{calculateBattingAverage(player[3], player[4]):{S2}}")

def addPlayer(players:list):
    index = len(players)
    name = input("Name: ")
    while True:
        position = input("Position: ")
        if POSITIONS.count(position) == 0:
            print("Invalid position. Try again.")
            print("POSITIONS")
            print(POSITIONS)
        else:
            break

    while True:
        bats = getNumOfBats()
        hits = getNumOfHits()

        if hits > bats:
            print("You cant have more hits than bats...")
        else:
            break

    newPlayer = [index, name, position, bats, hits]
    players.append(newPlayer)

def removePlayer(players:list):
    pass

def movePlayer(players:list):
    pass

def editPlayerPosition(players:list):
    pass

def editPlayersStats(players:list):
    pass

def displayPositions():
    print("POSITIONS")
    string = ", ".join(POSITIONS)
    print(string)

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

    players:list = []

    displayGreeting()

    while True:
        print()
        userChoice = input("Menu option: ")

        if userChoice == "1":
            displayLineup(players)

        elif userChoice == "2":
            addPlayer(players)

        elif userChoice == "7":
            print("Bye!")
            exit()

        else:
            print("Not a valid option. Please try again")



if __name__ == "__main__":
    main()