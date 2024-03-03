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
List of Authors: 'a -l'
Add Book: 'b'
List of Books: 'b -l'

Remove Author: 'rm -a'
Remove Book: 'rm -b'

### DELUXE
Cow: 'cow'
###

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


        # add a book
    elif response == "b":
        authors = get_all_authors()

        for i,a in authors:
            print(f"ID {i}: {a}")

        print("b")

    elif response == "a -l":

        books = get_all_books()

        for i,a in authors:
            print(f"{books}")



    response = input("").lower()



connection.close()