import fileIO as file
from datetime import datetime
from datetime import timedelta

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
DASHES = "=" * 100
S1 = 20
S2 = ">10"
S3 = "<3"
S4 = "<20"

#Function for displaying the menu
def displayGreeting():

    print(f"{DASHES}")
    print("Baseball Team Manager")
    print()
    getDate()
    print()
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

def getDate():
    format = "%Y-%m-%d"
    today = datetime.now()
    print(f"{'CURRENT DATE:':{S4}}{today:{format}}")
    while True:
        userInput = input(f"{'GAME DATE:':{S4}}")
        try:
            gameDate = datetime.strptime(userInput, format)
            timeSpan = gameDate - today
            if timeSpan.days > 0:
                print(f"{'DAYS UNTIL GAME:':{S4}}{timeSpan.days}")
                break
            else:
                break
        except Exception as e:
            print("Incorrect date format. Please try again.")
            print(e)



#displays the lineup of the players list
def displayLineup(players:list):
    print(f"{' ':{S3}}{'Player':{S1}}{'POS':{S2}}{'AB':{S2}}{'H':{S2}}{'AVG':{S2}}")
    print(f"{DASHES}")
    count = 1
    for player in players:
        print(f"{count:{S3}}{player["name"]:{S1}}{player["position"]:{S2}}{player["bats"]:{S2}}{player["hits"]:{S2}}{calculateBattingAverage(player["bats"], player["hits"]):{S2}}")
        count += 1

def addPlayer(players:list):
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

    newPlayer = {"name": name, "position": position, "bats": bats, "hits": hits}
    players.append(newPlayer)

def removePlayer(players:list):
    while True:
        try:
            userInput = int(input("Enter the number of the player you want to remove from the lineup: "))
            if userInput > 0 and userInput <= len(players) - 1:
                players.pop(userInput)
            else:
                print("Please enter a valid player number")
        except:
            print("Please enter a valid number")
        

def movePlayer(players:list):
    while True:
        try:
            userInput = int(input("Current lineup number: "))
            if userInput-1 > len(players) or userInput-1 < 0:
                print("Please enter a valid player number")
            else:
                print(f"{players[userInput-1]["name"]} was selected")
                playerToMove = players.pop(userInput-1)
                userInput = int(input("New lineup number: "))
                if userInput-1 > len(players) or userInput-1 < 0:
                    print("Please enter a valid player number")
                else:
                    players.insert(userInput-1, playerToMove)
                    print(f"{players[userInput-1]["name"]} was moved")
                    break
        except:
            print("Please enter a valid lineup number")


def editPlayerPosition(players:list):
    while True:
        try:
            userInput = int(input("Lineup number: "))
            if userInput-1 > len(players) or userInput-1 < 0:
                print("Please enter a valid player number")
            else:
                print(f"{players[userInput-1]["name"]} was selected current position is {players[userInput-1]["position"]}")
                while True:
                    position = input("New position: ")
                    if POSITIONS.count(position) == 0:
                        print("Invalid position. Try again.")
                        print("POSITIONS")
                        print(POSITIONS)
                    else:
                        players[userInput-1]["position"] = position
                        print(f"{players[userInput-1]["name"]}'s position was changed")
                        break
                break
        except:
            print("Please enter a valid lineup number")

def editPlayersStats(players:list):
        while True:
            try:
                userInput = int(input("Lineup number: "))
                if userInput-1 > len(players) or userInput-1 < 0:
                    print("Please enter a valid player number")
                else:
                    print(f"You selected {players[userInput-1]["name"]}  AB={players[userInput-1]["bats"]} H={players[userInput-1]["hits"]}")
                    while True:
                        bats = getNumOfBats()
                        hits = getNumOfHits()

                        if hits > bats:
                            print("You cant have more hits than bats...")
                        else:
                            players[userInput-1]["bats"] = bats
                            players[userInput-1]["hits"] = hits
                            print(f"{players[userInput-1]["name"]} was updated")
                            break
                    break
            except:
                print("Please enter a valid lineup number")

def displayPositions():
    print("POSITIONS")
    string = ", ".join(POSITIONS)
    print(string)

def calculateBattingAverage(bats: int, hits: int) -> int:
    battingAverage = round((int(hits)/int(bats)), 3)
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

    players:list = file.readFromFile()

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