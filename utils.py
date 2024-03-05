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
    
def add_rating(rating, review, book):
    book = get_one_book(book)

    session.add(Rating(rating=rating, review=review, book_id=book.id, book=book))
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
    return book.rating


### DELETION

def delete_rating():
    pass



if __name__ == "__main__":
    pass