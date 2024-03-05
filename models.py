from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import uuid

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class Author(Base):
    __tablename__ = 'authors'
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = 'books'
    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    author_id = Column(String, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books")

class Rating(Base):
    __tablename__ = 'ratings'
    rating_id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    review = Column(String, nullable=False)
    book_id = Column(Integer, ForeignKey('books.book_id'))
    book = relationship("Book", back_populates="ratings")



engine = create_engine('sqlite:///database.db')

# Create all tables
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
