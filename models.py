# to practise how to query sqlite DB using OOP
# 1. creating a new user
# 2. querying a user by his name and getting back all his sql attributes and saving them to the python object attributes.
# 3. when renting a book a person says a book name and then you search if the book is not already rented then if not rented then you update the date he took and his name.

import sqlite3
from sqlite3 import Error

def connect_db():
    conn = sqlite3.connect('library.db')
    return conn

def create_tables():
    conn = connect_db()
    cur = conn.cursor()
    try:
        # cur.execute('DROP TABLE IF EXISTS users')
        # cur.execute('DROP TABLE IF EXISTS books')
        cur.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL, user_type TEXT NOT NULL, fine INTEGER);''')
        cur.execute('''CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, name TEXT NOT NULL, author TEXT NOT NULL, publication_company TEXT, rented_date TEXT, rented_user_id INTEGER, FOREIGN KEY(rented_user_id) REFERENCES users(id));''')
    except Error as e:
        print(e)
    return 
####################################################################################################
class User:
    def __init__(self,name,email,id=None,user_type=None,fine=None):
        self.name = name 
        self.email = email
        self.id = id
        self.user_type = user_type
        self.fine = fine

    # for creating a user object and storing it in sqlite db
    @classmethod
    def create_user(cls,name,email,user_type='user'):
        conn = connect_db()
        cur = conn.cursor()
        try:
            cur.execute('INSERT INTO users(name,email,user_type) VALUES(?,?,?)',(name,email,user_type))
            conn.commit()
        except Error as e:
            print(e)
        return cls(name,email,user_type)
    
    # for creating a librarian
    @classmethod
    def create_librarian(cls,name,email,user_type='librarian'):
        conn = connect_db()
        cur = conn.cursor()
        try:
            cur.execute('INSERT INTO users(name,email,user_type) VALUES(?,?,?)',(name,email,user_type))
            conn.commit()
        except Error as e:
            print(e)
        return cls(name,email,user_type)
    
    # for getting user details and saving them on an object
    @classmethod
    def get_user(cls,name):
        conn = connect_db()
        cur = conn.cursor()
        try:
            cur.execute('SELECT * FROM users WHERE name=?',(name,))
            result = cur.fetchone()
            user = User(result[1],result[2],result[0],result[3],result[4])
            return user
        except Error as e:
            print(e)
            
    # a method to get if user email is in DB and return user object
    @classmethod
    def user_login(cls,email):
        conn = connect_db()
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM users WHERE email=?",(email,))
            result = cur.fetchone()
            if result:
                user = User(result[1],result[2],result[0],result[3])
                return user
            else:
                return None
        except Error as e:
            print(e)

    # add fine method
    @classmethod
    def add_fine(cls,rented_user_id,fine):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute('UPDATE users SET fine = ? WHERE id = ?',(fine,rented_user_id))
        conn.commit()
        return 

##############################################################################################
class Book:
    def __init__(self,name,author,pub_company,id=None,rented_date=None,rented_user_id=None):
        self.name = name
        self.author = author
        self.pub_company = pub_company
        self.id = id
        self.rented_date = rented_date
        self.rented_user_id = rented_user_id

    # for registering new book
    @classmethod
    def new_book(cls,name,author,pub_company):
        conn = connect_db()
        cur = conn.cursor()
        try:
            cur.execute('INSERT INTO books(name,author,publication_company) VALUES(?,?,?)',(name,author,pub_company))
            conn.commit()
            return cls(name,author,pub_company)
        except Error as e:
            print(e)
    
    # book getter
    @classmethod
    def get_book(cls,name):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute('''SELECT id,name,author,publication_company,date(rented_date),rented_user_id FROM books WHERE name = ?''',(name,))
        result = cur.fetchone()
        book = Book(result[1],result[2],result[3],result[0],result[4],result[5])
        return book

    # method to get all the books that have been borrowed
    # select * from books where rented_user_id IS NOT NULL;
    @classmethod
    def getall_books(cls):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute('''SELECT date(rented_date),rented_user_id FROM books WHERE rented_user_id IS NOT NULL''')
        result = cur.fetchall()  
        return result

    # get all available books
    def available_books():
        conn = connect_db()
        cur = conn.cursor()
        cur.execute('''SELECT * FROM books WHERE rented_user_id IS NULL''')
        result = cur.fetchall()
        books = [book[1] for book in result]
        print('available books: ',books)
        return 

# when renting a book   # pass an input from user to the get_book method on the controller
# this a normal function, supposed to be on controller
def rent_book():
    book=Book.get_book(input('please input book name: '))
    rented_user=User.get_user(input('name of user: '))
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''UPDATE books SET rented_date = datetime('now','localtime'), rented_user_id = ? WHERE id = ? ''',(rented_user.id,book.id))
    conn.commit()
    cur.execute('SELECT * FROM books WHERE id = ?',(book.id,))
    row = cur.fetchone()
    return row

# when a book is bieng returned
def return_book():
    book=Book.get_book(input('please input book name: '))
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''UPDATE books SET rented_date = ?, rented_user_id = ? WHERE id = ? ''',(None,None,book.id))
    conn.commit()
    cur.execute('SELECT * FROM books WHERE id = ?',(book.id,))
    row = cur.fetchone()
    return row
    