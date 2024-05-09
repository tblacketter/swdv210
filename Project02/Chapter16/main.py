import db as file
from datetime import datetime
from datetime import timedelta
from objects import Player
from objects import PlayerList
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

    newPlayer = Player(firstName, lastName, position, bats, hits)
    print(f"{newPlayer.fullName()} was added")
    players.addPlayer(newPlayer)

def removePlayer(players:PlayerList):
    while True:
        try:
            userInput = int(input("Enter the number of the player you want to remove from the lineup: "))
            if userInput > 0 and userInput <= players.numOfPlayers():
                deletedPlayer = players.retrievePlayer(userInput-1)
                players.removePlayer(userInput-1)
                print(f"{deletedPlayer.fullName()} was deleted")
                break
            else:
                print("Please enter a valid player number")
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
            userInput = int(input("Lineup number: ")) - 1
            if userInput >= players.numOfPlayers() or userInput < 0:
                print("Please enter a valid player number")
            else:
                player = players.retrievePlayer(userInput)
                print(f"{player.fullName()} was selected current position is {player.position}")
                while True:
                    position = input("New position: ")
                    if POSITIONS.count(position) == 0:
                        print("Invalid position. Try again.")
                        print("POSITIONS")
                        print(POSITIONS)
                    else:
                        players.editPlayerPosition(userInput, position)
                        print(f"{player.fullName()}'s position was changed")
                        break
                break
        except:
            print("Please enter a valid lineup number")

def editPlayersStats(players:PlayerList):
        while True:
            try:
                userInput = int(input("Lineup number: ")) - 1
                if userInput > players.numOfPlayers() or userInput < 0:
                    print("Please enter a valid player number")
                else:
                    player = players.retrievePlayer(userInput)
                    print(f"You selected {player.fullName()}  AB={player.bats} H={player.hits}")
                    while True:
                        bats = getNumOfBats()
                        hits = getNumOfHits()

                        if hits > bats:
                            print("You cant have more hits than bats...")
                        else:
                            players.editPlayer(userInput, bats, hits)
                            print(f"{player.fullName()} was updated")
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

    players:list = PlayerList(file.readFromFile())

    displayGreeting()

    while True:
        print()
        userChoice = input("Menu option: ")

        if userChoice == "1":
            displayLineup(players)

        elif userChoice == "2":
            addPlayer(players)
            file.writeToFile(players)
        
        elif userChoice == "3":
            removePlayer(players)
            file.writeToFile(players)

        elif userChoice == "4":
            movePlayer(players)
            file.writeToFile(players)

        elif userChoice == "5":
            editPlayerPosition(players)
            file.writeToFile(players)
        
        elif userChoice == "6":
            editPlayersStats(players)
            file.writeToFile(players)

        elif userChoice == "7":
            file.writeToFile(players)
            print("Bye!")
            exit()

        else:
            print("Not a valid option. Please try again")



if __name__ == "__main__":
    main()