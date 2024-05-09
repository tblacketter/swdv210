import db as file
from datetime import datetime
from datetime import timedelta
from objects import Player
from objects import PlayerList

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
DASHES = "=" * 100
S1 = "<30"
S2 = ">10"
S3 = "<3"
S4 = "<20"
S5 = "<15"

#Function for displaying the menu
def displayGreeting():

    print(f"{DASHES}")
    print("Baseball Team Manager")
    #print()
    #getDate()
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
    print(f"{'ID':{S3}}{'Bat Order': {S5}}{'Player':{S1}}{'POS':{S2}}{'AB':{S2}}{'H':{S2}}{'AVG':{S2}}")
    print(f"{DASHES}")
    for player in players:
        print(f"{player.playerID:{S3}}{player.batOrder: {S5}}{player.fullName():{S1}}{player.position:{S2}}{player.bats:{S2}}{player.hits:{S2}}{player.calculateBattingAverage():{S2}}")


def displayPositions():
    print("POSITIONS")
    string = ", ".join(POSITIONS)
    print(string)