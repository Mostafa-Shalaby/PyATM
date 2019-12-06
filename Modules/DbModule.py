# Imported Modules
import sqlite3
import os

# Name and Path of the Database File, (Since there is no path, it will be in the root of the project!)
DbFile = "PyATM.db"

def CreateConnection():
    # Method Description:
    """ Create a Connection to the Database File """

    # If the database file does not exist, it calls CreateDatabase function!
    if not os.path.exists(DbFile):
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
        cardid TEXT,
        username TEXT,
        accounttype TEXT,
        balance REAL,
        currencytype TEXT);
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userid INTEGER,
        cardid TEXT,
        TYPE TEXT,
        amount INTEGER,
        currencytype TEXT,
        occurrence NUMERIC DEFAULT CURRENT_DATETIME,
        FOREIGN KEY (cardid)
            REFERENCES Account (id));
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
    cur.execute("INSERT INTO Account (cardid, username, accounttype, balance, currencytype) VALUES ('372995442619905', 'Ahmed Saeed', 'Saving', 6589.00, 'L.E.');")
    cur.execute("INSERT INTO Account (cardid, username, accounttype, balance, currencytype) VALUES ('5504981108311326', 'Mohammed Khalid', 'Checking', 51000.00, 'L.E.');")
    cur.execute("INSERT INTO Account (cardid, username, accounttype, balance, currencytype) VALUES ('4445544517086312', 'Osama Khalid', 'Saving', 9000.00, 'L.E.');")
    cur.execute("INSERT INTO Account (cardid, username, accounttype, balance, currencytype) VALUES ('377557997331297', 'Hatiem Yasser', 'Checking', 289.00, 'L.E.');")
    cur.execute("INSERT INTO Account (cardid, username, accounttype, balance, currencytype) VALUES ('4445572056242236', 'Samir Ganim', 'Saving', 7900.00, 'L.E.');")
    cur.execute("INSERT INTO Account (cardid, username, accounttype, balance, currencytype) VALUES ('372995442619905', 'Ahmed Saeed', 'Checking', 500.00, 'L.E.');")

    # Commits/Saves the changes to the database
    dbConnection.commit()

    # Closes Both the unused Connection and Cursor
    cur.close()
    dbConnection.close()
    pass

def BalanceCheck(cardid, accountType):
    # Method Description:
    """ Checks the balance of the given user's account """

    # Initializes Connection and Cursor
    dbConnection = CreateConnection()
    cur = dbConnection.cursor()
    # Gets the balance of the user with the use of the his cardid (ID on his card), and accountType
    cur.execute("SELECT balance, currencytype FROM Account WHERE cardid = ? AND accounttype = ?", (cardid, accountType))
    # The query returns a tuple containing an integer representing the balance and a string representing the currency type
    balance, currency = cur.fetchone()
    # Closes Both the unused Connection and Cursor
    cur.close()
    dbConnection.close()
    return balance, currency

def UpdateBalance(newBalance, cardid, accountType):
    # Method Description:
    """ Updates the balance of the given user's account """
    # Initializes Connection and Cursor
    dbConnection = CreateConnection()
    cur = dbConnection.cursor()
    # Update the balance to the new value using 3 variables, newBalance, cardid and accountType
    cur.execute("UPDATE Account SET balance = ? WHERE cardid = ? AND accounttype = ?", (newBalance, cardid, accountType))
    # Commits/Saves the changes to the database
    dbConnection.commit()
    # Closes Both the unused Connection and Cursor
    cur.close()
    dbConnection.close()
    pass
