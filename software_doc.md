# Software Documentation
### Genius German App 
### Capstone Project
### by Louise Schmidtgen
### Supervisor Dr. Mystkowski
### Gardner-Webb University
### April 2022
#

![alt text](images\GGA_logo.png "Title")
# App Description

The Genius German App was developed to create a learning platform for people interested in learning the German Language and German culture. It supports Learnsets, a Translator, Holiday information and a Map.

# Requirements
This App runs in Python3. The following additional dependencies are needed to run this Application.

- mysql-connector==2.2.9
- mysql-connector-python==8.0.28
- protobuf==3.20.0
- PyQt5==5.15.6
- PyQt5-Qt5==5.15.2
- PyQt5-sip==12.10.0
- PyQt5-stubs==5.15.2.0

# API key
This App is dependent on an API key for the Translator. This key needs to be changed after using the 500 free calls to it in [RapidAPI](https://rapidapi.com/googlecloud/api/google-translate1).  
# Configuring the MySQL server:
- configurations are made in main.py in set_env_variables()
- The MySQL password should be set to the user's password that they set up when downloading MySQL for their machine.
- By default the MySQL user is root and the MySQL host is localhost.
- YOu may also change the database name in the same location

# Source Code
see [Gitlab](https://gitlab.com/g1552/geniusgermanapp/-/tree/louise/dev)

# Genius German App Documentation
1. Database Manager
2. User
3. Learnset
4. Word
5. Login Logout Controller
6. Login GUI
7. Sign Up GUI
8. Dashboard Controller
9. Dashboard GUI
10. Translator Controller
11. Google API
12. Translator GUI
13. Map GUI
14. Holidays Controller
15. Holidays GUI
16. Learnset Controller
17. Learnset Menu GUI
18. Add Learnset
19. Learnset Quiz Mode
20. Learnset Study Mode
21. Add Word
22. Pop Up GUI


# Class: Database Manager
*This class creates and maintains the Genius German App database.*

This function has the following attributes:
- DB_Name: retrieved from global environment

The following functions are provided:

DB.**connect_to_db**(db = None)
    
    Connects to SQL database, returns cursor and cnx (connection) to database. Uses user password and host location from global environment.

DB.**createDatabaseManager**() 
