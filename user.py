import logging

class User():
    def __init__(self, userID, username, password, favorites_learnset=[], learnset_list=[]):
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
        self.learnset_list = learnset_list + [self.favorites_learnset]
        self.newlearnsetID = -2 #-1 is for favorites learnset
        
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
            logging.warn(f"Could not remove {learnset.learnset_name}")
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
                return True
        return False
          