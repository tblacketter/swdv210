from dataclasses import dataclass

@dataclass
class Player:
    firstName:str
    lastName:str 
    position:str
    bats:int
    hits:int
    
    def __init__(self, firstName, lastName, position, bats, hits):
        self.firstName = firstName
        self.lastName = lastName
        self.position = position
        self.bats = bats
        self.hits = hits
    
    def calculateBattingAverage(self)->float:
        return round(float(self.hits)/float(self.bats), 3)

    def editPlayer(self, bats, hits):
        self.bats = bats
        self.hits = hits

    def fullName(self)->str:
        return f"{self.firstName} {self.lastName}"
    
    def changePosition(self, position:str):
        self.position = position




@dataclass
class PlayerList:
    playerList:Player

    def __init__(self, players:list):
        self.playerList = []
        for player in players:
            self.playerList.append(player)

    def __iter__(self):
        for player in self.playerList:
            yield player

    def addPlayer(self, player:Player):
        self.playerList.append(player)

    def removePlayer(self, index:int):
        self.playerList.pop(index)

    def movePlayer(self, indexToMove:int, destination:int):
        playerToMove = self.playerList.pop(indexToMove)
        self.playerList.insert(destination, playerToMove)

    def retrievePlayer(self, indexOfPlayer)->Player:
        return self.playerList[indexOfPlayer]

    def editPlayer(self, indexOfPlayerToEdit:int, bats:int, hits:int):
        player = self.playerList[indexOfPlayerToEdit]
        player.editPlayer(bats, hits)

    def editPlayerPosition(self, indexOfPlayerToEdit:int, position:str):
        player = self.playerList[indexOfPlayerToEdit]
        player.changePosition(position)

    def numOfPlayers(self)->int:
        return len(self.playerList)