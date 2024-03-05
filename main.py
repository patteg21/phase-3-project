from utils import *


def main():

    print("""
    Author and Book Tracker - CLI Application

    COMMANDS (case insensitive)
    ---------------------------------------------------------------
    Add Author: 'a'
    Add Book: 'b'
    Add Rating: 'b -r'

    Find Authors Books: 'f'
    List of Authors: 'a -l'
    List of Books: 'b -l'
    Remove Author: 'rm -a'
    Remove Book: 'rm -b'

    Cow: 'cow'

    Exit: 'x' 
    ---------------------------------------------------------------
    """)

    r = input().lower()

    while r != "x":
        
        if r == "a":
            name = input("Name: ")
            add_author(name=name)
            print("Author Added")
        if r == "b":
            authors = all_authors()
            for a in authors:
                print(a)
            title = input("Title: ")
            genre = input("Genre: ")
            author = input("Author (Full Name): ")
            add_book(title, genre, get_one_author(author))
            print("Book Added")
        if r == "b -r":
            books = all_books
            for book in books:
                print(book)
            rating = input("Rating: ")
            review = input("Review: ")
            title = input("Book (Full Name): ")
            add_rating(rating, review, get_one_book(title))


        # keep in a while loop
        r = input().lower()

if __name__ == "__main__":
    main()