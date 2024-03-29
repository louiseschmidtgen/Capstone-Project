from Database_Manager import DB

import os


def test1_create_db():
    return DB()


def test3_insert_user(mydb, username="lulu", userpassword="pw"):
    mydb.insert_user(username, userpassword)


def test4_return_user_id(mydb, username="lulu", userpassword="pw"):
    userid = mydb.return_user_id(username, userpassword)
    print(userid)


def test6_delete_user(my_db, userid):
    my_db.delete_user(userid)


def main():
    # set environ
    os.environ['SQLUser'] = 'root'
    os.environ['SQLPassword'] = 'my-secret-pw'
    os.environ['SQLHost'] = "localhost"
    os.environ['DB_NAME'] = 'GeniusGermanDatabase'
    # SECTION 1 Create DB
    my_db = test1_create_db()
    username = "lolu"
    password = "13"
    userid = 1
    print(my_db.insert_user(username, password))
    # SECTION 2 Test User
    # test3_insert_user(my_db, username, password)
    # test4_return_user_id(my_db, "lulu")
    # delete user, check for user just deleted.
    # test6_delete_user(my_db, userid)
    # test4_return_user_id(my_db, "lulu")

    # SECTION 3 Test Learnset
    # test 7-9:
    # print(my_db.insert_learnset("Fried", userid))
    # my_db.insert_learnset("Food", userid)
    # my_db.insert_learnset("Favorites", userid)
    # print(my_db.get_learnsets(userid))
    # my_db.delete_learnset(4)
    # print(my_db.get_learnsets(userid))

    # SECTION 4 Test Words
    # test 10-12
    # learnsetid = 4
    # my_db.insert_word(learnsetid, "Map", "Karte", "images/MapGer.png")
    # my_db.insert_word(learnsetid, "Map2", "Karte2", "images/MapGer.png")
    # print(my_db.get_words(learnsetid))
    # #my_db.delete_word(1)
    # print(my_db.get_words(learnsetid))


main()
