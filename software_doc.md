# Software Documentation
### Genius German App 
### Capstone Project
### by Louise Schmidtgen
### Supervisor Dr. Mystkowski
### Gardner-Webb University
### April 2022
#

![alt text](images/GGA_logo.png "Title")
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

    This function creates the Mysql database. It creates 3 tables, User, Learnset and Word. 

DB.**insert_user**(username, userpassword)

    This function inserts a new user into the User table with the given input.

        Args:
            username (str): name of the new user
            userpassword (str): password of the new user

DB.**return_user_id**(username, userpassword)

    This function returns the user id of the given username and password. If user does not exist returns empty cursor

        Args:
            username (str): name of the new user
            userpassword (str): password of the new user

        Returns:
            list: [(userid,)]

DB.**delete_user**(userid)

    This function deletes the user from user table given its id.

        Args:
            userid (int): id of the user

DB.**insert_learnset**(learnsetname, userid)

    This function insert a learnset into the learnset table with the given input.

        Args:
            learnsetname (str): name associated with learnset
            userid (int): id of the user that owns the learnset

DB.**get_ls_id**(learnsetname, userid)

    This function retrieves the id of the learnset given its name and the userid

        Args:
            learnsetname (str): name associated with learnset
            userid (int): id of the user that owns the learnset

        Returns:
            list: [(learnsetid,)]

DB.get_learnsets(userid)

    This function gets all learnset associated with a given user.

        Args:
            userid (int): id of the user that owns the learnset

        Returns:
            list: format: [(4, 'animals', 2), (5, 'food', 2)]first is learnset id, learnset name, userid

DB.**delete_learnset**(learnsetid)

    This function deletes a given learnset from the learnset table.

        Args:
            learnsetid (int): unique identifier of a learnset

DB.**insert_word**(learnsetId, wordEngl, wordGer, wordImg)

    This function inserts a word into the word table given its input

        Args:
            learnsetId (int): unique identifier of a learnset    
            wordEngl (str): word in english
            wordGer (str): word in german
            word_image (_type_): image associated with word

DB.**get_words**(learnsetid)

    This function gets all words associated to a given learnset

        Args:
            learnsetId (int): unique identifier of a learnset

        Returns:
            list: words format: [(1, 1, 'Cat', 'Katze', '/images/cat.png')] 
                >wordid, learnsetid, wordEngl, wordGer, wordimg

DB.**delete_word**(wordid)

    This function deletes a word from words.

        Args:
            wordid (int): unique identifier of a word

# Class: User
*The user class holds the users learnsets and words. When words or learnsets are added the changes are made in this class and written into the database once the user logs out.*

This function has the following attributes:
- userID (int): unique identifier for user
- username (str): name of user
- password (str): password of user
- favorites_learnset (learnset object): learnset that has all favorite words.
- learnset_list (list): collection of learnset objects. 
- newlearnsetID (int): Tracks current new id. It's negative to signal that it is not in the database yet.
- newwordID (int): Tracks current new id. It's negative to signal that it is not in the database yet.

The class has the following functions

User.**add_learnsets**(learnset)

    This function adds learnset to users learnset list

        Args:
            learnset (learnset object): learnset

User.**delete_learnset**(learnset)

    Deletes a learnset if possible

        Args:
            learnset (learnset object):

        Returns:
            Boolean: successful/unsuccesful in removing learnset

User.**check_learnset_is_unique**( learnsetname)

    This function checks wether learnset nae is taken already
        Args:
            learnsetname (str): name of learnset

        Returns:
            Boolean: True means name is unique, False means the opposite

User.**set_up_default_user**()

    This function sets the user up as a default user that has default learnsets with words.

# Class: Learnset

*This class holds all information on a Learnset and can add and remove words.*

This function has the following attributes:
- learnsetID (int): unique identifier of learnset
- learnset_name (str): name of learnset
- wordlist (list, optional): collection of words in learnset.
- popup (PopUp GUI Object)

The class has the following functions:

Learnset.**return_shuffled_words_in_learnset**()

    Returns:
        wordlist: list of word objects in this learnset    

Learnset.**add_word_to_learnset**(word)

    Adds a word to the learnset

        Args:
            word (Word Object)

Learnset.**remove_word_from_learnset**(word)

    Function tries to remove a word from learnset.

        Args:
            word (word object)

        Returns:
            Boolean: wether removal was successful or not

# Class: Word

*The Word class holds a words translations, id and image*

This function has the following attributes:
- wordID(int): unique identifier of a word
- wordEngl (str): word in english
- wordGer (str): word in german
- word_image (str): image associated with word
- isfavorite (boolean): indicates wether a word is favorite or not

# Class Login Logout Controller
*This class does all processing regarding login logout and sign up*

This function has the following attributes:
- signup(Signup GUI object)
- login_gui(Login GUI object)
- popup (Popup GUI object)
- database_manager(Database Manager object)
- user (User object)

The class has the following functions:

LoginOutController.**create_sign_up_gui**()

    This function creates the Sign up GUI

LoginOutController.**write_new_user_to_database**(username, password, repeatpassword)

    This function first checks that the info fits in the databse allocated space. Then it checks if the passwords match. If they do it checks wether the user already exists in db. If it does not it creates a new user and pushes the new user to the database. The function creates pop ups if the passwords don't match ot the sign in info is not unique.

        Args:
            username (str): name of the user
            password (str): password of the user
            repeatpassword (str): password of the user

LoginOutController.**create_login_gui**()

    This function creates the Login GUI.

LoginOutController.**get_user_id**(username, password)

    Given the input this function asks the database manager to return the userid. If there is none it returns -1.

        Args:
            username (str): name of the user
            password (str): password of the user

        Returns:
            int: userid

LoginOutController.**handle_login_request**(self, username, password)

    This function checks the login info and decides what to do with it. If it is incorrect it creates a popup. If user exists in database it calls a function that creates a user object based on the database.

        Args:
            username (str): name of the user
            password (str): password of the user

LoginOutController.**create_user_from_database**(userid, username, password)

    This function builds a user object after the data held on the user in the database.

        Args:
            userid (int): unique identifier of user
            username (str): name of the user
            password (str): password of the user

        Returns:
            user object    

LoginOutController.**create_dashboard_controller**()

    This function creates the Dashboard Controller and opens its GUI.

LoginOutController.**push_changes_to_database**(new_user)

    This function takes a user object and compares the changes in the object to the user data it finds in the database.  Based on what is in the database it makes changes by adding or removing words, learnsets or the user. A negative index stands for an object being new and needs to be added in the database. Now the object is assigned a positive ID which is generated by the database. If a object is in the database but not in the user object it gets deleted in the database.

        Args:
            new_user (user object): holds users learsets and words

        Returns:
            new_user (user object): holds users learsets and words

LoginOutController.**delete_account**(user)

    This function deletes a user and its data in the database. It first deletes words then learnset and lastly the user, to avoid dependency problems.

        Args:
            user (user object): holds users learsets and words

LoginOutController.**close_app**()

    This function closes the Application

# Class: Login GUI

*This Class implements the Login GUI.*

This function has the following attributes:
- login_out_controller(Login Logout Controller object)

The class has the following functions:

LogInGUI**createMainFrame**()

    This function builds the GUI using Form Layout.

LogInGUI**handle_close_window**()
    
    This function invokes close function in login logout controller.

LogInGUI**handle_login_event**()

    This function invokes handle_login_request function in login logout controller.

LogInGUI**handle_sign_up_event**()

    This function invokes create_sign_up_gui function in login logout controller.

# Class: SignUp GUI

*This Class implements the Login GUI.*

This function has the following attributes:
- login_out_controller(Login Logout Controller object)

The class has the following functions:

SignupGUI**createMainFrame**()

    This function builds the GUI using Form Layout.

SignupGUI**handle_close_window**()
    
    This function invokes close function in login logout controller.

SignupGUI**handle_sign_up_event**()

    This function invokes write_new_user_to_database function in login logout controller.

# Class: Dashboard Controller

*This function is linked to many different GUIs that the user can navigate to. This Controller mainly invokes functions in other controllers or GUIs to create GUIs or pass on the control*

This function has the following attributes:
- user (User object)
- login_out_controller(Login Logout Controller object)
- popup (Popup GUI object)
- mapgui(Map GUI object)
- holiday_controller(Holiday Controller object)
- translator_controller(Translator Controller object)
- dashboardgui(Dashboard GUI object)
- learnset_controller(Learnset Controller object)

The class has the following functions:

DashboardController**logout_processing**()

    This function invokes push_changes_to_database function in login logout controller.

DashboardController**popup_account_deletion**()

    This function creates popup GUI with prompt asking about confirming account deletion.

DashboardController**delete_account_processing**()

    This function invokes delete_account function in login logout controller.

DashboardController**open_map**()

    This function opens Map GUI.

DashboardController**open_translator**()

    This function opens Translator GUI

DashboardController**open_learnsets**()

    This function calls learnset controller to create learnset Menu GUI.

DashboardController**open_german_holidays**()

    This function calls holiday controller to open Holiday GUI.

DashboardController**open_login**()

    This function calls Login Logout Controller to create the Login GUI.

DashboardController**create_dashboard_gui**()
    This function creates the dasboard GUI.

# Class: Dashboard GUI

*This Class implements the Dashboard GUI.*

This function has the following attributes:
- dashboard_controller(Dashboard Controller object)

The class has the following functions:

DashboardGUI**createMainFrame**()

    This function builds the GUI using Grid Layout.

DashboardGUI**log_out_event**()
    
    This function invokes logout_processing function in dashboard controller.

DashboardGUI**delete_account_event**()

    This function invokes popup_account_deletion function in dashboard controller.

DashboardGUI**handle_map**()
    
    This function invokes open_map function in dashboard controller.

DashboardGUI**handle_translator**()

    This function invokes open_translator function in dashboard controller.

DashboardGUI**handle_learnsets**()
    
    This function invokes open_learnsets function in dashboard controller.

DashboardGUI**handle_german_holidays**()

    This function invokes open_german_holidays function in dashboard controller.

# Class: Translator Controller

*This Class handels the Translator GUI and calls to the Google API class.*

This function has the following attributes:
- dashboard_controller(Dashboard Controller object)
- translator_gui(Translator GUI Object)
- google_api(Google Api Object)

The class has the following functions:

Translator_Controller**get_e2g_tranlation**()
    
    This function translates an English word to German

        Args:
            engl_word (str): Users input that needs to be translated.

        Returns:
            str: The German translation of the Word.

Translator_Controller**get_g2e_tranlation**()

    This function translates an German word to English

        Args:
            ger_word (str): Users input that needs to be translated.

        Returns:
            str: The English translation of the Word.

Translator_Controller**create_translator_gui**()

    This function creates the translator GUI

Translator_Controller**close_translator**()

    This function unvokes create dashboard gui in the dashboard controller.

# Class: Google API

*This class makes the API calls to Google API to translate a word from English to German and vice versa.*

This function has the following attributes:
- popup (Popup GUI object)

The class has the following functions:

GoogleAPI**get_e2g_translation**(engl_word)

    This function calls the translate function to translate its input
        Args:
            engl_word (str): Users input that needs to be translated.

        Returns:
            str: The German translation of the Word.

GoogleAPI**get_g2e_translation**(ger_word)

    This function calls the translate function to translate its input

        Args:
            ger_word (str): Users input that needs to be translated.

        Returns:
            str: The English translation of the Word.

GoogleAPI**translate**(word, source_lang, target_lang)

    This function calls Google API to translate a Word from a given source language to a target language.

        Args:
            word (str): word that should be translated
            source_lang (str): has either value ger/en
            target_lang (str): has either value ger/en
        Returns:
            str: The translation of the Word.

# Class: Translator GUI

*This Class implements the Translator GUI.*

This function has the following attributes:
- translator_controller(Translator Controller object)

The class has the following functions:

TranslatorGUI**createMainFrame**()

    This function builds the GUI using Grid Layout.

TranslatorGUI**handle_close_window**()
    
    This function invokes close_translator function in translator controller.

TranslatorGUI**handle_e2g_translation**()

    This function gets word, calls translator controller to translate it and displays the translation.

TranslatorGUI**handle_g2e_translation**()

    This function gets word, calls translator controller to translate it and displays the translation.

# Class: Map GUI

*This Class implements the Map GUI.*

This function has the following attributes:
- dashboard_controller(Dashboard Controller object)

The class has the following functions:

MapGUI**createMainFrame**()

    This function builds the GUI using Grid Layout.

MapGUI**handle_close_window**()
    
    This function invokes create_dashboard_gui function in dashboard controller.


# Class: German Holidays Controller

*This Class holds information on German Holidays and displays popUps with info on holidays.*

This function has the following attributes:
- dashboard_controller(Dashboard Controller object)
- holiday_gui(Holiday GUI Object)
- holidaysdict(dictionary) has holidays as keys and list of holiday info as value.

The class has the following functions:

GermanHolidaysController**display_pop_up_with_info_on_holiday**(holiday)

    This function looks up the info on a given holiday in its dictornary and displays it in a Popup GUI.

        Args:
            holiday (str): name of holiday

GermanHolidaysController**create_holidays_gui**()

    This function invokes display_pop_up_with_info_on_holiday function in the holiday controller
        
        Args:
            holiday (str): name of holiday

GermanHolidaysController**create_dashboard_gui**

    This function calls the dashboard controller to create the dashboard GUI.

# Class: Holidays GUI

*This Class implements the German Holidays GUI.*

This function has the following attributes:
- holiday_controller(German HOliday Controller object)

The class has the following functions:

GermanHolidaysGUI**createMainFrame**()

    This function builds the GUI using Grid Layout.

GermanHolidaysGUI**handle_close_window**()
    
    This function invokes create_dashboard_gui function in holiday controller.

# Class: Learnset Controller

*This Class handles everything that has to do with learnsets, this includes adding words, learnsets, adding words to favorites, deleting words from learnsets, opening learnsets in study/quiz mode.*

This function has the following attributes:
- user_object(User Object)
- ls_menu_gui(Learnset Menu GUI Object)
- ls_quiz_gui(Learnset Quiz GUI Object)
- ls_study_gui(Learnset Study GUI Object)
- add_word_gui(Learnset Quiz GUI Object)
- add_learnset_gui(Add Learnset GUI Object)
- popup(Popup GUI Object)
- dashboard_controller(Dashboard Controller object)

The class has the following functions:

LearnsetController**create_word**(wordEngl, wordGer, word_image, learnset)

    Creates a word if given info is correct and adds it to learnset
        creates a popup gui to inform about success/no success.

        Args:
            wordEngl (str): word in english
            wordGer (str): word in german
            word_image (str): image associated with word
            learnset (learnset object): learnset object that holds all info on learnset
            wordID (int, optional): unique identifier of word. 

LearnsetController**add_word_to_learnset**(new_word, learnset)

    This function adds a given word to a given learnset

        Args:
            new_word (word object): holds all info on a word
            learnset (learnset object): holds all info on learnset

LearnsetController**add_word_to_favorites**(word)

    adds a word to favorites

        Args:
            word (word object): holds all info on a word

LearnsetController**remove_word_from_favorites**(word)

    removes a word from favorites

        Args:
            word (word object): holds all info on a word

LearnsetController**remove_word_from_learnset**(word, learnset)

    removes a word from learnset

        Args:
            word (word object): holds all info on word
            learnset (learnset object): holds all info on learnset

        Returns:
            Boolean: success/unsuccessful in removing word.

LearnsetController**add_learnset**(name)

    adds a learnset under a new name if name is not already used.

        Args:
            name (str): name of new learnset

LearnsetController**delete_learnset**(learnset)

    This function delets a given learnset

        Args:
            learnset_obj (learnset object): a learnset groups words together under a topic

LearnsetController**open_learnset_study_mode_gui**(learnset_obj)

    This function opens a given learnset in a learnset study GUI.

        Args:
            learnset_obj (learnset object): a learnset groups words together under a topic

LearnsetController**open_learnset_quiz_mode_gui**(learnset_obj)

    This function opens a given learnset in a learnset quiz GUI.

        Args:
            learnset_obj (learnset object): a learnset groups words together under a topic

LearnsetController**open_add_word_gui**(learnset_obj)

    This function opens the add word GUI.

        Args:
            learnset_obj (learnset object): a learnset groups words together under a topic

LearnsetController**open_add_learnset_gui**()

    This function opens the add learnset GUI."""

LearnsetController**create_learnset_menu_gui**()

    This function opens the le menu GUI.

LearnsetController**open_dashboard**()

    This function invokes create_dashboard_gui method of the dashboard controller

# Class: Learnset Menu GUI

*This Class implements the Learnset Menu GUI.*

This function has the following attributes:
- user_object(User Object)
- learnset_controller(Learnset Controller object)

The class has the following functions:

LSMenuGUI**createMainFrame**()

    This function builds the GUI using Grid Layout.

LSMenuGUI**handle_submit_event**()

    This function invokes open_learnset_study_mode_gui or open_learnset_quiz_mode_gui function in learnset controller depending on which mode is selected in the mode menu.

LSMenuGUI**handle_add_learnset_event**()
    
    This function invokes open_dashboard function in learnset controller.    

LSMenuGUI**handle_close_window**()
    
    This function invokes open_dashboard function in learnset controller.

# Class: Add Learnset GUI

*This Class implements the Add Learnset GUI.*

This function has the following attributes:
- learnset_controller(Learnset Controller object)

The class has the following functions:

AddLearnsetGUI**createMainFrame**()

    This function builds the GUI using Grid Layout.

AddLearnsetGUI**handle_add_learnset_event**()
    
    This function invokes add learnset function in the learnset controller.

AddLearnsetGUI**handle_close_window**()
    
    This function invokes create_learnset_menu_gui function in learnset controller.

# Class: Learnset Quiz Mode

*This Class implements the Learnset Quiz GUI.*

This function has the following attributes:
- learnset_controller(Learnset Controller object)

The class has the following functions:

LSQuizGUI**createMainFrame**()

    This function builds the GUI using Grid Layout.

LSQuizGUI**handle_add_word_to_favorites**()
    
    This function calls add_word_to_favorites method in learnset_controller.

LSQuizGUI**update**()
    
    This function updates the last word displayed to the new word. I also updates the percentage of correct answers vs incorrect ones.

LSQuizGUI**handle_next_event**()

    This function updates current word to be the next word in the wordlist if there is one else it displays an error message.

LSQuizGUI**create_popup**()
    
    This function creates a popUp GUI with an error message.

LSQuizGUI**handle_close_window**()
    
    This function destroys the current window and opens the learnset menu GUI.

LSQuizGUI**handle_check_event**()

    This function checks wether the user has entered the correct translation and opens a pop up indicating the answer was correct or incorrect.

# Class: Learnset Study Mode

*This Class implements the Learnset Study GUI.*

This function has the following attributes:
- learnset_controller(Learnset Controller object)

The class has the following functions:

LSStudyGUI**createMainFrame**()

    This function builds the GUI using Grid Layout.

LSStudyGUI**handle_add_word_to_favorites**()
    
    This function calls add_word_to_favorites method in learnset_controller.

LSStudyGUI**handle_add_word_event**()
    
    This function calls open_add_word_gui method in learnset_controller.

LSStudyGUI**handle_delete_word**()
    
    This function calls remove_word_from_learnset method in learnset_controller. If there is no word left in the learnset it sets the current word to the default word

LSStudyGUI**handle_previous_event**()
    
    This function updates current word to be the previous word in the wordlist if there is one, else it displays an error message.

LSStudyGUI**update**()
    
    This function updates the last word displayed to the new word. I also updates the percentage of correct answers vs incorrect ones.

LSStudyGUI**handle_next_event**()

    This function updates current word to be the next word in the wordlist if there is one, else it displays an error message.

LSStudyGUI**create_popup**()
    
    This function creates a popUp GUI with an error message.

LSStudyGUI**handle_close_window**()
    
    This function destroys the current window and opens the learnset menu GUI.

# Class: Add Word GUI

*This Class implements the Add Word GUI.*

This function has the following attributes:
- learnset_controller(Learnset Controller object)
- learnset(Learnset Object)

The class has the following functions:

AddWordGUI**createMainFrame**()

    This function builds the GUI using Grid Layout.

AddWordGUI**get_image**()
    
    This function lets the user select a image in a file dialog.

AddWordGUI**handle_add_word_event**()
    
    This function gets the user input and tries to create a word and add it to the learnset.

AddWordGUI**handle_close_window**()
    
    This function hides the current window.

# Class: Pop Up GUI
*This Class implements the Pop Up GUI.*

This function has the following attributes:
- NA

The class has the following functions:

PopUpGUI**createPopUp**()

    This function creates a pop up GUI with a given message

        Args:
            message (str): a message
            title (str, optional): title of the window. Defaults to "Pop Up".

PopUpGUI**create_yes_no_pop_up**()
    
    This function creates a pop up GUI with a given message. The user clicks either yes or no.
        If the user clicks yes the delete_account_processing in the dashboard_obj is invoked.

        Args:
            message (str): a message
            dashboard_obj (Dashboard Object):
            title (str, optional): title of the window. Defaults to "Pop Up".
