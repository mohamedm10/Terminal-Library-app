import sqlite3
from sqlite3 import Error
import random

###### DB CREATION & CONNECTION FUNC
def connect_db():

    con = sqlite3.connect('library.db')
    return con
# ######

con = connect_db()
# INSERTING A NEW USER 
def add_user(name,contact,user_type):
    cur = con.cursor()
    try:
        cur.execute('INSERT INTO users(name,contact,type) VALUES(?,?,?)',(name,contact,user_type))
        con.commit()
    except Error as e:
        print(e)
# ###########
# ADDING A NEW BOOK
def add_book(name,author,publication_company):
    cur = con.cursor()
    cur.execute('INSERT INTO books(name,author,publication_company) VALUES(?,?,?)',(name,author,publication_company))
    con.commit()
# ###########
# function to get user to borrow id and book id
## ask user his name and return his ID
### ask user book he wants to borrow and check if book is not already borrowed then return book id

# ADDING BORROWER TO BOOK
def register_book(user_id,book_id):
    cur = con.cursor()
    cur.execute("UPDATE books SET rented_date = datetime('now','localtime'), rented_user_id = ? WHERE id = ? ", (user_id,book_id))
    con.commit()
##############

# WHEN A USER RETURNS A BOOK
def return_book(book_id):
    cur = con.cursor()
    cur.execute("UPDATE books SET rented_date = ?, rented_user_id = ? WHERE id = ? ", (None,None,book_id))
    con.commit()
##############

# select users.name from users,books where users.id=books.rented_user_id; ---->>> get user names of user that have borrowed books
# select users.name from users,books where users.type='user'; ---->>> get all users/librarians
# select name from books where rented_user_id IS NULL; ---->>>> get all available books



# if __name__=='__main__':
#     connect_db()
