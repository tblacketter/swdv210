import db
from objects import PlayerList
from objects import Player
from ui import POSITIONS, displayGreeting, displayLineup


def addPlayer(players:PlayerList):
    firstName = input("First name: ")
    lastName = input("Last name: ")
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

    db.addToDB(players.numOfPlayers() + 1, firstName, lastName, position, bats, hits)
    print(f"{firstName} {lastName} was added")

def removePlayer(players:PlayerList):
    while True:
        try:
            userInput = int(input("Enter the id of the player you want to remove from the lineup: "))
            for player in players:
                if player.playerID == userInput:
                    print(f"{player.fullName()} was deleted") 
            db.deletePlayer(userInput)
            break
        except:
            print("Please enter a valid number")
        

def movePlayer(players:PlayerList):
    while True:
        try:
            currentIndex = int(input("Current lineup number: ")) - 1
            print(currentIndex)
            if currentIndex >= players.numOfPlayers() or currentIndex < 0:
                print("Please enter a valid player number")
            else:
                playerToMove = players.retrievePlayer(currentIndex)
                print(f"{playerToMove.fullName()} was selected")
                destination = int(input("New lineup number: ")) - 1
                if destination >= players.numOfPlayers() or destination < 0:
                    print("Please enter a valid player number")
                else:
                    players.movePlayer(currentIndex, destination)
                    print(f"{playerToMove.fullName()} was moved")
                    break
        except:
            print("Please enter a valid lineup number")


def editPlayerPosition(players:PlayerList):
    while True:
        try:
            userInput = int(input("Player ID: ")) 
            for player in players:
                if player.playerID == userInput:
                    currentPlayer = player
            print(f"{currentPlayer.fullName()} was selected current position is {currentPlayer.position}")
            while True:
                position = input("New position: ")
                if POSITIONS.count(position) == 0:
                    print("Invalid position. Try again.")
                    print("POSITIONS")
                    print(POSITIONS)
                else:
                    db.editPlayerPosition(userInput, position)
                    print(f"{currentPlayer.fullName()}'s position was changed")
                    break
            break
        except:
            print("Please enter a valid lineup number")

def editPlayersStats(players:PlayerList):
        while True:
            try:
                userInput = int(input("Player ID: ")) 
                for player in players:
                    if player.playerID == userInput:
                        currentPlayer = player
                print(f"You selected {currentPlayer.fullName()}  AB={currentPlayer.bats} H={currentPlayer.hits}")
                while True:
                    bats = getNumOfBats()
                    hits = getNumOfHits()

                    if hits > bats:
                        print("You cant have more hits than bats...")
                    else:
                        db.editPlayerStats(userInput, bats, hits)
                        print(f"{currentPlayer.fullName()} was updated")
                        break
                break
            except:
                print("Please enter a valid lineup number")

def displayPositions():
    print("POSITIONS")
    string = ", ".join(POSITIONS)
    print(string)

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
    db.connect()
    displayGreeting()

    while True:
        players:list = PlayerList(db.getPlayers())
        print()
        userChoice = input("Menu option: ")

        if userChoice == "1":
            displayLineup(players)

        elif userChoice == "2":
            addPlayer(players)
        
        elif userChoice == "3":
            removePlayer(players)

        elif userChoice == "4":
            movePlayer(players)  

        elif userChoice == "5":
            editPlayerPosition(players)
                 
        elif userChoice == "6":
            editPlayersStats(players)   

        elif userChoice == "7":
            print("Bye!")
            db.close()
            exit()

        else:
            print("Not a valid option. Please try again")



if __name__ == "__main__":
    main()