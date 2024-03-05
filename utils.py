from models import Author, Book, Rating, Session

session = Session()

def add_author(name):
    session.add(Author(name=name))
    session.commit()

def all_authors():
    return session.query(Author).all()

def all_books():
    return session.query(Book).all()

def add_book(title, genre, author):
    session.add(Book(title=title, genre=genre, author=author))
    session.commit()
    
def add_rating(rating, review, book):
    session.add(Rating(rating=rating, review=rating, book=book))
    session.commit()



if __name__ == "__main__":
    pass