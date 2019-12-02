# Imported Modules
import sqlite3
import os

# Name and Path of the Database File, (Since there is no path, it will be root of the project!)
DbFile = "PyATM.db"

def CreateConnection():
    # Method Description:
    """ Create a Connection to the Database File """
    # If the database file does not exist, it calls CreateDatabase function!
    if not os.path.exists("PyATM.db"): 
        CreateDatabase()
        PopulateDatabase()
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
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userid INTEGER,
        username TEXT,
        accounttype TEXT,
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

def PopulateDatabase():
    # Method Description:
    """ Populates the database with some PreDefined Data """
    # Initializes Connection and Cursor
    dbConnection = sqlite3.connect(DbFile)
    cur = dbConnection.cursor()
    # Populates the Account Table With Few Presets Data.
    cur.execute("INSERT INTO Account (userid, username, accounttype, balance, currencytype) VALUES (123456, 'Ahmed Saeed', 'Saving', 6589.00, 'L.E.');")
    cur.execute("INSERT INTO Account (userid, username, accounttype, balance, currencytype) VALUES (234567, 'Mohammed Khalid', 'Checking', 51000.00, 'L.E.');")
    cur.execute("INSERT INTO Account (userid, username, accounttype, balance, currencytype) VALUES (345678, 'Osama Khalid', 'Saving', 9000.00, 'L.E.');")
    cur.execute("INSERT INTO Account (userid, username, accounttype, balance, currencytype) VALUES (456789, 'Hatiem Yasser', 'Checking', 289.00, 'L.E.');")
    cur.execute("INSERT INTO Account (userid, username, accounttype, balance, currencytype) VALUES (567890, 'Samir Ganim', 'Saving', 7900.00, 'L.E.');")
    cur.execute("INSERT INTO Account (userid, username, accounttype, balance, currencytype) VALUES (123456, 'Ahmed Saeed', 'Checking', 500.00, 'L.E.');")
    # Commits/Saves the changes to the database
    dbConnection.commit()
    # Closes Both the unused Connection and Cursor
    cur.close()
    dbConnection.close()
    pass

def BalanceCheck(userID, accountType):
    # Method Description:
    """ Checks the balance of the given user's account """
    # Initializes Connection and Cursor
    dbConnection = CreateConnection()
    cur = dbConnection.cursor()
    # Gets the balance of the user with the use of the his userID (ID on his card), and accountType
    cur.execute("SELECT balance FROM Account WHERE userid = ? AND accounttype = ?", (userID, accountType))
    # Since there is 1 column and 1 row, The following code will give us directly a float value, instead of a 1x1 list
    balance = cur.fetchone()[0]
    # Closes Both the unused Connection and Cursor
    cur.close()
    dbConnection.close() 
    return balance

def UpdateBalance(newBalance, userID, accountType):
    # Method Description:
    """ Updates the balance of the given user's account """
    # Initializes Connection and Cursor
    dbConnection = CreateConnection()
    cur = dbConnection.cursor()
    # Update the balance to the new value using 3 variables, newBalance, userID and accountType
    cur.execute("UPDATE Account SET balance = ? WHERE userid = ? AND accounttype = ?", (newBalance, userID, accountType))
    # Commits/Saves the changes to the database
    dbConnection.commit()
    # Closes Both the unused Connection and Cursor
    cur.close()
    dbConnection.close()
    pass