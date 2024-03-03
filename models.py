import uuid
import numpy as np

class Author:
    def __init__(self, name: str):
        # random id
        self.id = np.random.randint(0,1000)

        
        self.name = name
        self.books = []

    def add_book(self, book: object):
        self.books.append(book)

    def get_all_books(self):
        for book in self.books:
            print(f"{book}")

    def delete_object(self):
        print("Author Removed")
        del self



class Book(Author):
    def __init__(self, title: str, genre: str, rating:str, author_id: int):
        self.id = np.random.randint(0,1000)
        self.title = title
        self.genre = genre
        self.rating = rating
        self.author_id = author_id

    def update_rating(self, rating: float):
        self.rating = rating
        print(f"{self.title} is now rated {self.rating}")

    def delete_book(self):
        print("Book Removed")
        del self
