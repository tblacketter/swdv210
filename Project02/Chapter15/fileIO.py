import csv
from objects import Player
from objects import PlayerList

def writeToFile(players: PlayerList):
    
    tempList = []

    for player in players:
        playerList = []
        playerList.append(player.firstName)
        playerList.append(player.lastName)
        playerList.append(player.position)
        playerList.append(player.bats)
        playerList.append(player.hits)
        tempList.append(playerList)

    with open("players.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(tempList)

def readFromFile()->list:
    players = []
    try:
        with open("players.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                player = Player(row[0], row[1], row[2], row[3], row[4])
                players.append(player)         
        return players
    except FileNotFoundError:
        print("Players file wasn't found so it was created")
        with open("players.csv", "w", newline="") as file:
            return players
        
