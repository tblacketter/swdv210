import csv
import sqlite3
from objects import Player
from objects import PlayerList
from contextlib import closing


conn = None

def connect():
    global conn
    if not conn:
        conn = sqlite3.connect("Project02/Chapter17/playersDB.db")
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def makePlayer(row):
    return Player(row["playerID"], row["batOrder"], row["firstName"], row["lastName"], row["position"], row["atBats"], row["hits"])

def makePlayerList(results):
    playerList = []
    for row in results:
        playerList.append(makePlayer(row))
    return playerList

def getPlayers():
    query = '''SELECT * FROM Player'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()
    return makePlayerList(results)

def addToDB(batOrder, firstName, lastName, position, bats, hits):
    sql = '''INSERT INTO Player (batOrder, firstName, lastName, position, atBats, hits)
               VALUES(?, ?, ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (batOrder, firstName, lastName, position, bats, hits))
        conn.commit()

def deletePlayer(playerID):
    sql = '''DELETE FROM Player WHERE playerID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (playerID,))
        conn.commit()

def editPlayerPosition(playerID, positon):
    sql = '''UPDATE Player 
             SET position = ?
             WHERE playerID =?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (positon, playerID))
        conn.commit()

def editPlayerStats(playerID, bats, hits):
    sql = '''UPDATE Player 
             SET atBats = ?, hits = ?
             WHERE playerID =?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (bats, hits, playerID,))
        conn.commit()        

def updateBatOrder(oldBatOrder, newBatOrder):
    sql = '''UPDATE Player 
             SET batOrder = ?
             WHERE batOrder = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (newBatOrder, oldBatOrder))
        conn.commit()     

        