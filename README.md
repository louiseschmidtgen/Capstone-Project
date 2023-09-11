# GeniusGermanApp

This Project was the Capstone Project for my Software Engineering class.
Here is a link to my documentation of the project *(It contains all the diagrams you could dream of that took an eternity to draw... if only I knew about Mermaid back then... sigh)*: [GeniusGermanApp](https://docs.google.com/document/d/1XqJAceCnmf6RqE3BI4Zhkrc7axCc2xems4nLynujRto/edit?usp=sharing)

The GeniusGermanApp is a language learning application designed to help users learn and practice German vocabulary and language skills. The app provides a user-friendly graphical user interface (GUI) that allows users to create a user account, log in, access various features, and study German words through interactive learnsets and quizzes.

This project is no eye-candy but I learned a lot since it uses the Google Translate API as and a mySQL database!

## Installation
Prerequisites:
- [Python](https://www.python.org/downloads/) (>=3.8) 
- [Pipenv](https://pypi.org/project/pipenv/)
- [Docker](https://www.docker.com/products/docker-desktop) (running)

To run this App you need to clone the repository and run the following commands in the root directory of the project:

```bash
make build
```

Note: if running on an M1 Mac you need to run the following command instead:
Make yourself a cup of coffee, this will take a while...
```bash
make build-m1
```


## Features

### User Account Management
- Create a User Account with a unique username and password.
- Log into an existing user account with username and password verification.
- Log out of the user account.

### Learnsets and Vocabulary
- Explore various learnsets covering colors, numbers, animals, food, and more.
- Study learnsets in Study Mode with word-image associations.
- Take quizzes in Quiz Mode to test German language knowledge.
- View statistics on learnset performance, including the number of correct and incorrect words.
- Add and delete words to/from learnsets.
- Mark words as favorites for easy access.

### Translation and Language Tools
- Translate German words to English and vice versa using the Google API.
- Display information on German special characters (ä, ö, ü, ß).

### German Holidays and Information
- Learn about German holidays and traditions.
- Access information on specific German holidays with detailed descriptions.

### Map of Germany
- View a Map of Germany within the application.

### Additional Features
- Get information on German cities, tourist attractions, and travel.
- Check the weather for specific cities in Germany.
- Display exchange rates between USD and Euro.
- Add sound and written pronunciation to words in learnsets.
- Reset user passwords in case of forgotten passwords.

## API key
This App is dependent on an API key for the Translator. This key only allows for 500 free calls a month. To get your own new key got to this site and update the key info in main.go [RapidAPI](https://rapidapi.com/googlecloud/api/google-translate1).  

## Screenshots

### Translator Functionality using Google Translate API

![Image](/images/readme/GeniusGermanApp(2).jpg)

### Learnset Menu
![Image](/images/readme/GeniusGermanApp(4).jpg)

### Quiz Mode
![Image](/images/readme/GeniusGermanApp(3).jpg)

### Study Mode
![Image](/images/readme/GeniusGermanApp(5).jpg)

### Log-In Functionality
![Image](/images/readme/GeniusGermanApp.jpg)