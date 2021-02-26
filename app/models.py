from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150) , nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(100))
    publisher = db.Column(db.String(30))
    author = db.Column(db.String(30))
    publication_date = db.Column(db.String)
    pages = db.Column(db.Integer)
    isbn = db.Column(db.BIGINT)
    description = db.Column(db.TEXT)
    link = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    stock = db.Column(db.Integer)

    def __init__(self, book_name, publisher, author, publication_date, pages, description, link, rating, isbn,stock):
        self.book_name = book_name
        self.publisher = publisher
        self.author = author
        self.publication_date = publication_date
        self.pages = pages
        self.description = description
        self.link = link
        self.rating = rating
        self.isbn = isbn
        self.stock = stock

class BorrowLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    rental_date = db.Column(db.DateTime(), nullable=False)
    due_date = db.Column(db.DateTime(), nullable=True)


