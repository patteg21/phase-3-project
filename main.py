from utils import *
import cowsay


def print_a():
    print("AUTHORS")
    authors = all_authors()
    for a in authors:
        print(a.name)
    print("")

def print_b():
    print("BOOKS")
    books = all_books()
    for book in books:
        print(book.title)
    print("")

def main():

    print("""
    Author and Book Tracker - CLI Application

COMMANDS (case insensitive)
---------------------------------------------------------------
Add Author: 'a'
Add Book: 'b'
Add Rating: 'r'
Remove Author: 'rm -a'
Remove Book: 'rm -b'
Find Books by Author: 'f'
Find Ratings by Book: 'f -b'
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
            print_a()
            title = input("Title: ")
            genre = input("Genre: ")
            author = input("Author (Full Name): ")
            add_book(title, genre, author)
            print("Book Added")
        elif r == "r":
            print_b()
            title = input("Book (Full Name): ")
            rating = input("Rating: ")
            review = input("Review: ")
            add_rating(rating, review, title)
            print("Rating Added")
        elif r == "f":
            print_a()
            name = input("Name: ")
            books = get_author_books(name=name)
            for b in books:
                print(b.title)

        elif r == "f -b":
            print_b()
            title = input("Book (Full Name): ")
            ratings = get_book_ratings(title=title)
            
            for rate in ratings:
                print("")
                print(f"ID: {rate.id}")
                print(f"Rate: {rate.rating}")
                print(f"Review: {rate.review}")
                print("")


        elif r == "rm -a":
            author = input("Author: ")
            delete_author(name=author)
        elif r =="rm -b":
            title = input("Title: ")
            delete_book(title=title)
        elif r == "rm -r":
            uuid = input("UUID: ")
            delete_rating(rating_id=uuid)
        elif r == "cow":
            cowsay.cow("Tell me about bad coding practices...")


        # divider and condition
        print("---------------------------------------------------------------")
        r = input().lower()


    print("""



---------------------------------------------------------------
###############################################################
                        THANK YOU
###############################################################
---------------------------------------------------------------



    """)

if __name__ == "__main__":
    main()