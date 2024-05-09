import csv

def writeToFile(players: list):
    
    tempList = []

    for player in players:
        playerList = []
        playerList.append(player["name"])
        playerList.append(player["position"])
        playerList.append(player["bats"])
        playerList.append(player["hits"])
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
                tempDict = {}
                tempDict["name"] = row[0]
                tempDict["position"] = row[1]
                tempDict["bats"] = row[2]
                tempDict["hits"] = row[3]
                players.append(tempDict)         
        return players
    except FileNotFoundError:
        print("Players file wasn't found so it was created")
        with open("players.csv", "w", newline="") as file:
            return players
        
