# Imported Modules
import sqlite3
import os
import time

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
        userid INTEGER NOT NULL,
        cardid TEXT NOT NULL,
        type TEXT NOT NULL,
        amount INTEGER,
        currencytype TEXT,
        occurrence NUMERIC DEFAULT (datetime('now', 'localtime')),
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

    # Populates the Account Table With Few Preset Data.
    cur.execute("INSERT INTO Account (cardid, username, accounttype, balance, currencytype) VALUES ('372995442619905', 'Ahmed Saeed', 'Saving', 6589.00, 'L.E.');")
    cur.execute("INSERT INTO Account (cardid, username, accounttype, balance, currencytype) VALUES ('5504981108311326', 'Mohammed Khalid', 'Checking', 51000.00, 'L.E.');")
    cur.execute("INSERT INTO Account (cardid, username, accounttype, balance, currencytype) VALUES ('4445544517086312', 'Osama Khalid', 'Saving', 9000.00, 'L.E.');")
    cur.execute("INSERT INTO Account (cardid, username, accounttype, balance, currencytype) VALUES ('377557997331297', 'Hatiem Yasser', 'Checking', 289.00, 'L.E.');")
    cur.execute("INSERT INTO Account (cardid, username, accounttype, balance, currencytype) VALUES ('4445572056242236', 'Samir Ganim', 'Saving', 7900.00, 'L.E.');")
    cur.execute("INSERT INTO Account (cardid, username, accounttype, balance, currencytype) VALUES ('372995442619905', 'Ahmed Saeed', 'Checking', 500.00, 'L.E.');")

    # Populates the Transactions Table With Few Preset Data.
    # Preset Values for Card 1
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (1, '372995442619905', 'deposit', 10000, 'L.E.','2019-12-06 09:08:11')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (1, '372995442619905', 'withdraw', 5000, 'L.E.','2019-12-08 13:30:33')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (1, '372995442619905', 'withdraw', 5000, 'L.E.','2019-12-08 20:40:12')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (1, '372995442619905', 'deposit', 9500, 'L.E.','2019-12-09 03:11:11')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (1, '372995442619905', 'withdraw', 2911, 'L.E.','2019-12-10 16:22:10')")
    # Preset Values For Card 2
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (2, '5504981108311326', 'deposit', 11000, 'L.E.','2019-12-04 10:15:45')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (2, '5504981108311326', 'deposit', 12000, 'L.E.','2019-12-05 14:54:33')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (2, '5504981108311326', 'withdraw', 1000, 'L.E.','2019-12-06 09:08:11')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (2, '5504981108311326', 'deposit', 20000, 'L.E.','2019-12-07 11:30:33')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (2, '5504981108311326', 'deposit', 18000, 'L.E.','2019-12-08 14:22:47')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (2, '5504981108311326', 'withdraw', 5000, 'L.E.','2019-12-09 13:30:33')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (2, '5504981108311326', 'withdraw', 8000, 'L.E.','2019-12-10 14:33:10')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (2, '5504981108311326', 'deposit', 4000, 'L.E.','2019-12-11 19:22:12')")
    # Preset Values For Card 3
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (3, '4445544517086312', 'deposit', 6000, 'L.E.','2019-12-04 10:15:45')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (3, '4445544517086312', 'deposit', 2000, 'L.E.','2019-12-05 14:54:33')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (3, '4445544517086312', 'withdraw', 3000, 'L.E.','2019-12-08 14:22:47')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (3, '4445544517086312', 'withdraw', 1000, 'L.E.','2019-12-10 14:33:10')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (3, '4445544517086312', 'deposit', 5000, 'L.E.','2019-12-11 19:22:12')")
    # Preset Values For Card 4
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (4, '4445544517086312', 'deposit', 700, 'L.E.','2019-12-04 10:15:45')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (4, '4445544517086312', 'deposit', 2800, 'L.E.','2019-12-05 14:54:33')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (4, '4445544517086312', 'withdraw', 1200, 'L.E.','2019-12-08 14:22:47')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (4, '4445544517086312', 'withdraw', 1800, 'L.E.','2019-12-10 14:33:10')")
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (4, '4445544517086312', 'withdraw', 311, 'L.E.','2019-12-11 19:22:12')")
    # Preset Values For Card 5
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype, occurrence) VALUES (5, '4445572056242236', 'deposit', 7900, 'L.E.','2019-12-06 03:11:11')")

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

def RecordTrans(cardid, accountType, type, amount):
    # Method Description:
    """ Records the transaction in the database """
    # Initializes Connection and Cursor
    dbConnection = CreateConnection()
    cur = dbConnection.cursor()
    # Get the user's id and currencytype
    cur.execute("SELECT id, currencytype FROM Account WHERE cardid = ? AND accounttype = ?", (cardid, accountType))
    id, currency = cur.fetchone()
    # Insert the transaction into the database
    cur.execute("INSERT INTO Transactions (userid, cardid, type, amount, currencytype) VALUES (?, ?, ?, ?, ?)", (id, cardid, type, amount, currency))
    # Commits/Saves the changes to the database
    dbConnection.commit()
    # Closes Both the unused Connection and Cursor
    cur.close()
    dbConnection.close()
    pass

#RecordTrans('377557997331297', 'Checking', 'deposit', 220)

def TransCheck(cardid, accountType):
    # Method Description:
    """ Checks the transaction history of an account """
    # Initializes Connection and Cursor
    dbConnection = CreateConnection()
    cur = dbConnection.cursor()
    # Get the user's id and currencytype
    cur.execute("SELECT id, currencytype FROM Account WHERE cardid = ? AND accounttype = ?", (cardid, accountType))
    id, currency = cur.fetchone()
    # Retrieve the transaction history from the database
    cur.execute("SELECT t.type, t.amount, t.currencytype, t.occurrence FROM Transactions t INNER JOIN Account a ON a.id = t.userid WHERE userid = ? ORDER BY occurrence DESC LIMIT 10;", (id, ))
    # Store the matching rows in a dictionary
    result = cur.fetchall()
    # Commits/Saves the changes to the database
    dbConnection.commit()
    # Closes Both the unused Connection and Cursor
    cur.close()
    dbConnection.close()
    return result
