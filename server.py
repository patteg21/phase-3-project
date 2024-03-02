from models import Author, Book
import sqlite3

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
        title TEXT NOT NULL,
        publication_year INTEGER,
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES Author(author_id)
    )
''')




print("""
Author and Book Tracker - CLI Application

COMMANDS (case insensitive)
---------------------------------------------------------------
Add Author: 'a'
Add Book: 'b'
List of Authors: 'l'

Exit: 'x' 
---------------------------------------------------------------
""")

response = input().lower()

while response != "x":

    if response == "a":
        name = input("Name: ")


        # creates a new author with a input name
        author = Author(name=name)
        cursor.execute('''INSERT INTO Author (id, name) VALUES (?, ?, ?)''', 
               (author.id, author.name))

    elif response == "b":
        print("b")


    elif response == "l":
        print("l")



    response = input("").lower()



connection.close()