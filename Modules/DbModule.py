# Imported Modules
import sqlite3
import os

# Name and Path of the Database File, (Since there is no path, it will be root of the project!)
DbFile = "PyATM.db"

def CreateConnection():
    # Method Description:
    """ Create a Connection to the Database File """
    # If the database file does not exist, it calls CreateDatabase function!
    if not os.path.exists("PyATM.db"): CreateDatabase()
    # Initializes and Returns a Database Connection
    return sqlite3.connect(DbFile)

def CreateDatabase():
    # Method Description:
    """ Create a Database File and Structures its Tables """
    # Initializes Both a Connection (Which will create the file), Then a Cursor (Which manipulates the file)
    dbConnection = sqlite3.connect(DbFile)
    cur = dbConnection.cursor()
    # Executes the SQL statements.
    cur.execute(
        """ 
        CREATE TABLE IF NOT EXISTS Account(
        id INTEGER PRIMARY KEY UNIQUE,
        username TEXT,
        acccounttype TEXT,
        balance REAL,
        currencytype TEXT);
        """
    )
    # Commits/Saves the changes to the database
    dbConnection.commit()
    # Closes Both the unused Connection and Cursor
    cur.close()
    dbConnection.close()
    pass

CreateConnection()