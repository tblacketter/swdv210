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