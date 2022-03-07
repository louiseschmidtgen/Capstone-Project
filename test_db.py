from Database_Manager import DB

import os

def test1_create_db():
    return DB()

def test_return_user_id(mydb, username="lulu", userpassword="pw"):
    userid = mydb.return_user_id( username, userpassword)
    print(userid)

def test2_insert_user

def main():
    #set environ
    os.environ['SQLUser']='root'
    os.environ['SQLPassword']= 'Veritas!10'
    os.environ['SQLHost'] = "localhost"
    os.environ['DB_NAME'] ='GeniusGermanDB'
    my_db = test1_create_db()
    test2_return_user_id(my_db)
    
main()