from utils import *
import cowsay


def main():

    print("""
    Author and Book Tracker - CLI Application

    COMMANDS (case insensitive)
    ---------------------------------------------------------------
    Add Author: 'a'
    Add Book: 'b'
    Add Rating: 'b -r'
    List of Authors: 'a -l'
    List of Books: 'b -l'
    Find Authors Books: 'f'
    Find Book Ratings: 'f -b'

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
        elif r == "b":
            authors = all_authors()
            for a in authors:
                print(a.name)
            title = input("Title: ")
            genre = input("Genre: ")
            author = input("Author (Full Name): ")
            add_book(title, genre, author)
            print("Book Added")
        elif r == "b -r":
            books = all_books()
            for book in books:
                print(book)
            rating = input("Rating: ")
            review = input("Review: ")
            title = input("Book (Full Name): ")
            add_rating(int(rating), review, title)
        elif r == "a -l":
            authors = all_authors()
            for a in authors:
                print(a.name)
        elif r == "b -l":
            books = all_books()
            for book in books:
                print(book.title)
        elif r == "f":
            authors = all_authors()
            for a in authors:
                print(a.name)
            name = input("Name: ")
            get_author_books(name=name)
        elif r == "f -b":
            books = all_books()
            for book in books:
                print(book.title)
            title = input("Book (Full Name): ")
            get_book_ratings(title=title)




        elif r == "cow":
            cowsay.cow("Leave...")

        # keep in a while loop
        r = input().lower()

if __name__ == "__main__":
    main()