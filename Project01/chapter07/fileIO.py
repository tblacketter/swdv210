import csv

def writeToFile(players: list):
    with open("players.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(players)

def readFromFile()->list:
    players = []
    try:
        with open("players.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                players.append(row)         
        return players
    except FileNotFoundError:
        print("Players file wasn't found so it was created")
        with open("players.csv", "w", newline="") as file:
            return players
        
