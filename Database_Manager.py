from __future__ import print_function
import sys
import mysql.connector
from mysql.connector import errorcode

import os


# This class creates and maintains the Genius German database with methods: 
# connect_to_db, 
class DB():
    def __init__(self):
        #creates db if necessary
        #get db name from environment 
        try:
            self.DB_NAME = str(os.getenv('DB_NAME'))
            
        except Exception as e:
            print("Check that MySQL database name is provided in main.py .")
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Exception: ", e)
            sys.exit(1)
        
        self.createDatabaseManager() 
        

    '''
    Intent: Connects to SQL database, returns cursor and cnx (connection) to database.
    * Cursor interacts with the MySQL server and executes operations on the database.  
    * Preconditions: myuser, mypassword, myhost (and db if given) variables to have valid values for the root 
    * user of a given MySQL server or a given database.
    * Postconditions:
    * Post0. The connection to a database db is established (if db is not None) 
    * Post1. The connection to a MySQL server is established (if db is None)
    '''
    def connect_to_db(self, db = None):
        try:
            myuser = str(os.getenv('SQLUser'))
            mypassword = str(os.getenv('SQLPassword')) 
            myhost = str(os.getenv('SQLHost'))
        except Exception as e:
            print("Check that MySQL database user, password and host are provided in main.py .")
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Exception: ", e)
        if db:
            cnx = mysql.connector.connect(
            user=myuser, 
            password=mypassword,
            host=myhost,
            database=db)
            self.cursor = cnx.cursor()
            return self.cursor, cnx            
        else:
            cnx = mysql.connector.connect(
            user=myuser, 
            password=mypassword,
            host=myhost)
            self.cursor = cnx.cursor()
            return self.cursor, cnx
        
    '''
    Intent: Creates database and tables in that database.
    * Preconditions: 
    * Connection to database is established.
    * Tables User and Stock are already formatted and ready to be created.
    * Postconditions:
    * Post0. Database is created successfully if database does not exist already.
    * Post1. Tables are created successfully if tables do not exist already.
    * Post2. Failed creating database and error is thrown if database can not be created.
    * Post3. Failed creating tables and error is thrown if tables can not be created.
    '''
    def createDatabaseManager(self):
        '''
        Intent: Creates the database 
        * Preconditions: 
        * DB_name variable is created and set to correct database name.
        * Postconditions:
        * Post0. Database GeniusFinanceDB is created successfully if no exception is thrown.
        * post1. if exception (mysql.connector.Error) is thrown, database can not created
        '''
        def create_database(cursor):
            
            try:
                cursor.execute(f"CREATE DATABASE {self.DB_NAME} DEFAULT CHARACTER SET 'utf8'")
            except mysql.connector.Error as err:
                print(f"Failed creating database: {err}")
                sys.exit(1)

        TABLES = {}
        TABLES['User'] = (
            "CREATE TABLE `User` ("
            "  `userId` int(11) NOT NULL AUTO_INCREMENT,"
            "  `username` varchar(40)  NOT NULL,"
            "  `userpassword` varchar(15) NOT NULL,"
            "  PRIMARY KEY (`userId`)"
            ") ENGINE=InnoDB")

        TABLES['Learnset'] = (
            "CREATE TABLE `Learnset` ("
            "  `learnsetId` int(11) NOT NULL AUTO_INCREMENT,"
            "  `learnsetName` varchar(20) NOT NULL,"
            "  `userId` int(11) NOT NULL,"
            "  PRIMARY KEY (`learnsetId`), FOREIGN KEY (`userId`) REFERENCES `User` (`userId`) "
            ") ENGINE=InnoDB")

        TABLES['Word'] = (
            "CREATE TABLE `Word` ("
            "  `wordId` int(11) NOT NULL  AUTO_INCREMENT,"            
            "  `learnsetId` int(11) NOT NULL,"
            "  `wordEngl` varchar(25) NOT NULL,"
            "  `wordGer` varchar(25) NOT NULL,"
            "  `wordImg` varchar(450) NOT NULL,"
            "  PRIMARY KEY (`wordId`), FOREIGN KEY (`learnsetId`) REFERENCES `Learnset` (`learnsetId`) "
            ") ENGINE=InnoDB")
                    
        #connect to mysql server as root user
        cursor, cnx = self.connect_to_db()
       

        #check if database name already exists otherwise create it 
        try:
            cursor.execute(f"USE {self.DB_NAME}")
            
        except mysql.connector.Error as err:
            print(f"Database { self.DB_NAME} does not exists.")
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor)
                print(f"Database { self.DB_NAME} created successfully.")
                cnx.database =  self.DB_NAME
                
            else:
                print(err)
                sys.exit(1) #not 0 is abnormal termination

        #specify table description for the table 
        
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                
                else:
                    print(err.msg)
            else:
                print("OK")

        
        cursor.close()
        cnx.close()

   
    '''
    Intent: Query User data from database. Return a list of all User data from database
    * Preconditions: 
    * cursor is connected to correct database (GeniusFinanceDB)
    * User table already exists.
    * Postconditions:
     * Post0. Selects all data from the User table if connection to database if successful.
    * Post1. Displays None if connection to database is not successful.
    '''
    #Table 1: User
    def insert_user(self, username, userpassword):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"INSERT INTO User"
                    "(username, userpassword) "
                    "VALUES (%s, %s)")
        data = (username, userpassword)
        cursor.execute(query, data)
        cnx.commit()
        
    def return_user_id(self, username, userpassword):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"SELECT userId FROM User WHERE username = '{username}' AND userpassword = '{userpassword}'")
        cursor.execute(query)
        #cnx.commit()
        return [i for i in cursor] 
        #if does not exit returns [] else returns [(userid,)]
        
    def delete_user(self, userid ):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"DELETE FROM User WHERE userId = '{userid}'")
        #query = (f"DELETE FROM User INNER JOIN Learnset ON User.UserID = Learnset.UserID INNER JOIN Word ON Learnset.LearnsetID = Word.LearnsetID WHERE userId = '{userid}'")
        #SELECT User.UserID FROM ([User] INNER JOIN Learnset ON User.UserID = Learnset.UserID) INNER JOIN Word ON Learnset.LearnsetID = Word.LearnsetID;
        cursor.execute(query)
        cnx.commit()    
        
    #Table2: Learnset
    def insert_learnset(self, learnsetname, userid):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"INSERT INTO Learnset"
                    "(learnsetName, userId) "
                    "VALUES (%s, %s)")
        data = (learnsetname, userid)
        cursor.execute(query,data)
        cnx.commit()  
        
    def get_ls_id(self, learnsetname, userid):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"SELECT learnsetId FROM Learnset WHERE userId = '{userid}' AND learnsetName='{learnsetname}' ")
        cursor.execute(query)
        #cnx.commit()
        return [i for i in cursor]        
    
    def get_learnsets(self, userid):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"SELECT * FROM Learnset WHERE userId = '{userid}'")
        cursor.execute(query)
        #cnx.commit()
        return [i for i in cursor]
    
    def delete_learnset(self, learnsetid):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"DELETE FROM Learnset WHERE learnsetId = '{learnsetid}'")
        cursor.execute(query)
        cnx.commit()
    
    #Table3: Words
    def insert_word(self, learnsetId, wordEngl, wordGer, wordImg):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"INSERT INTO Word"
                    "(learnsetId, wordEngl, wordGer, wordImg) "
                    "VALUES (%s, %s, %s, %s)")
        data = (learnsetId, wordEngl, wordGer, wordImg)
        cursor.execute(query,data)
        cnx.commit()    
    
    def get_words(self, learnsetid):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"SELECT * FROM Word WHERE learnsetId = '{learnsetid}'")
        cursor.execute(query)
        #cnx.commit()
        return [i for i in cursor]        
        
    def delete_word(self, wordid ):
        print(f"Deleting word {wordid}")
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"DELETE FROM Word WHERE WordId = '{wordid}'")
        cursor.execute(query)
        cnx.commit()


    