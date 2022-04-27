
from Word import Word
from Learnset import Learnset

class User():
    def __init__(self, userID, username, password, favorites_learnset, learnset_list=[]):
        """User Object keeps track of user data

        Args:
            pop_up_gui (popup obj): 
            userID (int): unique identifier for user
            username (str): name of user
            password (str): password of user
            favorites_learnset (learnset object): learnset that has all favorite words.
            learnset_list (list, optional): collection of learnset objects. Defaults to [].
        """
        self.userID = userID
        self.username = username
        self.password = password
        self.favorites_learnset = favorites_learnset 
        self.learnset_list = learnset_list #+ [self.favorites_learnset]
        self.newlearnsetID = -2 #-1 is for favorites learnset
        self.newwordID = -1 #-1 is for favorites learnset
        if self.userID <0:
            self.set_up_default_user()    
                 
    def ___str__(self):
        return str(self.learnset_list)
    
    def print_learnsets(self):
        """Debugging function. Prints all ls by their name"""
        for ls in self.learnset_list:
            print(ls.learnset_name)  
                
    def add_learnset(self, learnset):
        """add learnset to user

        Args:
            learnset (learnset object): learnset
        """
        self.learnset_list.append(learnset)
        
        
    def delete_learnset(self, learnset):
        """Deletes a learnset if possible

        Args:
            learnset (learnset object):

        Returns:
            Boolean: successful/unsuccesful in removing learnset
        """
        #can't delete Favorites learnset
        if learnset.learnset_name =="Favorites":
            return False
        #try to delete learnset
        try:
            self.learnset_list.remove(learnset)
            del learnset
            
            return True
        except:
            print(f"Could not remove {learnset.learnset_name}")
            return False
        
    def check_learnset_is_unique(self, learnsetname):
        """checks wether learnset nae is taken already
        Args:
            learnsetname (str): name of learnset

        Returns:
            Boolean: True means name is unique, False means the opposite
        """
        for learnset in self.learnset_list:
            if learnset.learnset_name == learnsetname:
                return False
        return True
    
    def set_up_default_user(self):
        """This function sets the user up as a default user
        that has default learnsets with words.
        """
        #Set up Animals
        cat = Word(self.newwordID, "the fat cat", "die fette Katze", 'images\myanimals\cat.JPG')
        self.newwordID -=1
        chameleon = Word(self.newwordID, "the chameleon", "das Chamäleon", 'images\myanimals\chameleon.jpg')
        self.newwordID -=1 
        deer = Word(self.newwordID, "the deer", "das Reh", 'images\myanimals\deer.jpg')
        self.newwordID -=1  
        dog = Word(self.newwordID, "the dog", "der Hund", 'images\myanimals\dog.JPG')
        self.newwordID -=1
        myelephant = Word(self.newwordID, "the elephant", "der Elephant", 'images\myanimals\elephant.jpg')
        self.newwordID -=1 
        frog = Word(self.newwordID, "the frog", "der Frosch", 'images\myanimals\myfrog.jpg')
        self.newwordID -=1          
        horse = Word(self.newwordID, "the horse", "das Pferd", 'images\myanimals\horse.jpg')
        self.newwordID -=1
        mouse = Word(self.newwordID, "the mouse", "die Maus", 'images\myanimals\mouse.jpg')
        self.newwordID -=1 
        panda = Word(self.newwordID, "the panda", "der Panda", 'images\myanimals\panda.jpg')
        self.newwordID -=1  
        sheep = Word(self.newwordID, "the sheep", "das Schaf", 'images\myanimals\sheep.jpg')
        self.newwordID -=1
        squirrel = Word(self.newwordID, "the squirrel", "das Eichhörnchen", 'images\myanimals\squirrel.jpg')
        self.newwordID -=1 
        tiger = Word(self.newwordID, "the tiger", "der Tiger", 'images\myanimals\mytiger.jpg')
        self.newwordID -=1          
        zebra = Word(self.newwordID, "the zebra", "das Zebra", 'images\myanimals\zebra.jpg')
        self.newwordID -=1         
        # List of words 
        animal_words = [cat, chameleon, deer, dog, myelephant, frog, horse, mouse, panda, sheep, squirrel, tiger, zebra]
        #Animal Learnset     
        animals_learnset = Learnset(self.newlearnsetID, "Animals", animal_words)
        self.newlearnsetID -=1
        
        
        #Food
        apple = Word(self.newwordID, "the apple", "der Apfel", 'images\myfood\myapple.jpg')
        self.newwordID -=1
        beer = Word(self.newwordID, "the beer", "das Bier", 'images\myfood\mybeer.jpg')
        self.newwordID -=1 
        bread = Word(self.newwordID, "the bread", "das Brot", 'images\myfood\mybread.jpg')
        self.newwordID -=1  
        cake = Word(self.newwordID, "the cake", "der Kuchen", 'images\myfood\cake.jpg')
        self.newwordID -=1
        cheese = Word(self.newwordID, "the cheese", "der Käse", 'images\myfood\cheese.jpg')
        self.newwordID -=1 
        drinks = Word(self.newwordID, "the drinks", "die Getränke", 'images\myfood\drinks.jpg')
        self.newwordID -=1          
        fish = Word(self.newwordID, "the fish", "der Fisch", 'images\myfood\myfish.jpg')
        self.newwordID -=1
        food = Word(self.newwordID, "the food", "das Essen", 'images\myfood\myfood.jpg')
        self.newwordID -=1 
        fruit = Word(self.newwordID, "the fruit", "das Obst", 'images\myfood\myfruit.jpg')
        self.newwordID -=1  
        juice = Word(self.newwordID, "the juice", "der Saft", 'images\myfood\juice.jpg')
        self.newwordID -=1
        meat = Word(self.newwordID, "the meat", "das Fleisch", 'images\myfood\meat.jpg')
        self.newwordID -=1 
        milk = Word(self.newwordID, "the milk", "die Milch", 'images\myfood\milk.jpg')
        self.newwordID -=1          
        noodles = Word(self.newwordID, "the noodles", "die Nudeln", 'images\myfood\mynoodles.jpg')
        self.newwordID -=1     
        soup = Word(self.newwordID, "the soup", "die Suppe", 'images\myfood\soup.jpg')
        self.newwordID -=1
        strawberry = Word(self.newwordID, "the strawberry", "die Erdbeere", 'images\myfood\strawberry.jpg')
        self.newwordID -=1 
        vegetables = Word(self.newwordID, "the vegetables", "das Gemüse", 'images\myfood\myvegetables.jpg')
        self.newwordID -=1          
        water = Word(self.newwordID, "the water", "das Wasser", 'images\myfood\water.jpg')
        self.newwordID -=1 
             
        # List of words 
        food_words = [cake, cheese, drinks, juice, meat, milk, apple, beer, bread, fish, food, fruit, noodles, soup, strawberry, vegetables, water]
        #Food Learnset     
        foods_learnset = Learnset(self.newlearnsetID, "Food", food_words)
        self.newlearnsetID -=1
        
        
        
        #Color
        black = Word(self.newwordID, "black", "schwarz", 'images\color\myblack.png')
        self.newwordID -=1
        blue = Word(self.newwordID, "blue", "blau", 'images\color\myblue.png')
        self.newwordID -=1 
        brown = Word(self.newwordID, "brown", "braun", 'images\color\mybrown.png')
        self.newwordID -=1  
        colors = Word(self.newwordID, "the colors", "die Farben", 'images\color\colors.jpg')
        self.newwordID -=1
        green = Word(self.newwordID, "green", "grün", 'images\color\green.jpg')
        self.newwordID -=1 
        orange = Word(self.newwordID, "orange", "orange", 'images\color\orange.jpg')
        self.newwordID -=1          
        pink = Word(self.newwordID, "pink", "pink", 'images\color\pink.jpg')
        self.newwordID -=1
        red = Word(self.newwordID, "red", "rot", 'images\color\myred.png')
        self.newwordID -=1 
        white = Word(self.newwordID, "white", "weiß", 'images\color\white.jpg')
        self.newwordID -=1  
        yellow = Word(self.newwordID, "yellow", "gelb", 'images\color\yellow.png')
        self.newwordID -=1
        
        # List of words 
        color_words = [black, blue, brown, colors, green, orange, pink, red, white, yellow]
        #Colors Learnset     
        colors_ls = Learnset(self.newlearnsetID, "Colors", color_words)
        self.newlearnsetID -=1
        
               
        
        #Numbers
        one = Word(self.newwordID, "one", "eins", 'images\mynumbers\one.png')
        self.newwordID -=1
        two = Word(self.newwordID, "two", "zwei", 'images\mynumbers\mytwo.jpg')
        self.newwordID -=1 
        three = Word(self.newwordID, "three", "drei", 'images\mynumbers\mythree.jpg')
        self.newwordID -=1  
        four = Word(self.newwordID, "four", "vier", 'images\mynumbers\myfour.jpg')
        self.newwordID -=1
        five = Word(self.newwordID, "fünf", "five", 'images\mynumbers\myfive.jpg')
        self.newwordID -=1 
        six = Word(self.newwordID, "six", "sechs", 'images\mynumbers\six.png')
        self.newwordID -=1          
        seven = Word(self.newwordID, "seven", "sieben", 'images\mynumbers\seven.jpg')
        self.newwordID -=1
        eight = Word(self.newwordID, "eight", "acht", 'images\mynumbers\eight.jpg')
        self.newwordID -=1 
        nine = Word(self.newwordID, "nine", "neun", 'images\mynumbers\mynine.jpg')
        self.newwordID -=1  
        ten = Word(self.newwordID, "ten", "zehn", 'images\mynumbers\myten.jpg')
        self.newwordID -=1
        numbers = Word(self.newwordID, "the numbers", "die Zahlen", 'images\mynumbers\mynumbers.jpg')
        self.newwordID -=1
        
        # List of words 
        numbers_words = [one, two, three, four, five, six, seven, eight, nine, ten, numbers]
        #numbers Learnset     
        numbers_ls = Learnset(self.newlearnsetID, "Numbers", numbers_words)
        self.newlearnsetID -=1
        
        learnsets = [foods_learnset, animals_learnset, numbers_ls, colors_ls]
        
        #append all learnsets
        self.learnset_list += learnsets
          