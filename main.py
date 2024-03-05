from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from models import Author, Book, Rating, Session

# Create a new session
session = Session()


def main():

    print("""
    Author and Book Tracker - CLI Application

    COMMANDS (case insensitive)
    ---------------------------------------------------------------
    Add Author: 'a'
    Find Authors Books: 'f'
    List of Authors: 'a -l'
    Add Book: 'b'
    Add Rating: 'b -r'
    List of Books: 'b -l'
    Remove Author: 'rm -a'
    Remove Book: 'rm -b'

    Cow: 'cow'

    Exit: 'x' 
    ---------------------------------------------------------------
    """)

    response = input().lower()

    while response != "x":

        


        # keep in a while loop
        response = input().lower()

if __name__ == "__main__":
    main()