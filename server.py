from models import Author, Book
import sqlite3
import cowsay

try:
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    print("\nDatabase connected... \n")
except:
    print ("\nDatabase not connected \n")

# Create Author table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Author (
        author_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# Create Book table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Book (
        book_id INTEGER PRIMARY KEY,
        genre TEXT NOT NULL,
        title TEXT NOT NULL,
        rating INTEGER,
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES Author(author_id)
    )
''')

# fetch all author rows
def get_all_authors():
        cursor.execute('''SELECT * FROM Author ''') 
        rows = cursor.fetchall()

        return rows

def get_all_books():
        cursor.execute('''SELECT * FROM Book ''') 
        rows = cursor.fetchall()

        return rows



print("""
Author and Book Tracker - CLI Application

COMMANDS (case insensitive)
---------------------------------------------------------------
Add Author: 'a'
Find Authors Books: 'f'
List of Authors: 'a -l'

Add Book: 'b'
List of Books: 'b -l'

Remove Author: 'rm -a'
Remove Book: 'rm -b'

Cow: 'cow'

Exit: 'x' 
---------------------------------------------------------------
""")

response = input().lower()

while response != "x":

    if response == 'cow':
        cowsay.cow('This shouldnt be here...')

    # adds an author
    if response == "a":
        name = input("Name: ")


        # creates a new author with a input name
        author = Author(name=name)
        cursor.execute('''INSERT INTO Author (author_id, name) VALUES (?, ?)''', 
               (author.id, author.name))

        connection.commit()       
        print('''
        
        Author Succesfully Added
        
        ''')

    # returns all authors
    elif response == "a -l":

        authors = get_all_authors()

        for i,a in authors:
            print(f"ID {i}: {a}")
    
    elif response == 'f':

        authors = get_all_authors()

        for i,a in authors:
            print(f"ID {i}: {a}")
        
        author_id = input("Author ID: ")

        cursor.execute('''SELECT * FROM Book WHERE author_id = ?''', (author_id,))

        author_books = cursor.fetchall()

        for i, b in enumerate(author_books):
            print(f"{i}: {b}")


        # add a book
    elif response == "b":
        authors = get_all_authors()

        print("Authors: ")
        for i,a in authors:
            print(f"ID {i}: {a}")

        title = input("Title: ")
        genre = input("Genre: ")
        rating = input("Rating: ")
        author_id = input("Author ID: ")

        book = Book(title=title, genre=genre, rating=rating, author_id=author_id)
        cursor.execute('''INSERT INTO Book (book_id, title, genre, rating, author_id) VALUES (?, ?, ?, ?, ?)''', 
               (book.id, book.title, book.genre, book.rating, book.author_id))

        connection.commit()
        print('''
        
        Book Succesfully Added
        
        ''')


    elif response == "a -l":

        books = get_all_books()

        for b in books:
            print(f"{b}")



    response = input("").lower()



connection.close()