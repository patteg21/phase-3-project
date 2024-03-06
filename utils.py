from models import Author, Book, Rating, Session

session = Session()

### BASICS

def add_author(name):
    session.add(Author(name=name))
    session.commit()

def get_one_author(name):
    return session.query(Author).filter(Author.name == name).first()

def get_one_book(title):
    return session.query(Book).filter(Book.title == title).first()


def add_book(title, genre, author):
    author = get_one_author(name=author)

    new_book = Book(title=title, genre=genre, author_id=author.id, author=author)
    session.add(new_book)
    session.commit()
    
def add_rating(rating, review, title):
    book = get_one_book(title=title)

    new_rating = Rating(rating=int(rating), review=review, book_id=book.id, book=book)
    session.add(new_rating)
    session.commit()

def all_authors():
    return session.query(Author).all()

def all_books():
    return session.query(Book).all()



### RELATIONAL

def get_author_books(name):
    author = get_one_author(name=name)
    return author.books

def get_book_ratings(title):
    book = get_one_book(title=title)
    return book.ratings


### DELETION

def delete_rating(rating_id):
    rating = session.query(Rating).filter(Rating.id == rating_id).first()
    session.delete(rating)

def delete_book(title):
    book = get_one_book(title=title)
    for rating in book.ratings:
        delete_rating(rating_id=rating.id)
    session.delete(book)

def delete_author(name):
    author = get_one_author(name=name)
    for book in author.books:
        delete_book(title=book.title)
    session.delete(author)



if __name__ == "__main__":
    pass