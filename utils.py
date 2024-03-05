from models import Author, Book, Rating, Session

session = Session()

def add_author(name):
    session.add(Author(name=name))
    session.commit()

def all_authors():
    return session.query(Author).all()

def get_one_author(name):
    return session.query(Author).filter(Author.name == name).first()

def all_books():
    return session.query(Book).all()

def get_one_book(title):
    return session.query(Book).filter(Author.title == title).first()

def add_book(title, genre, author):
    session.add(Book(title=title, genre=genre, author=author))
    session.commit()
    
def add_rating(rating, review, book):
    session.add(Rating(rating=rating, review=rating, book=book))
    session.commit()


#### DELETION FUNCTIONALITY

def delete_rating():
    pass



if __name__ == "__main__":
    pass