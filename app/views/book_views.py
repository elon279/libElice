import csv
import random
from flask import Blueprint, request, render_template, session, Response, jsonify,g, redirect, url_for
from app import db
from app.models import Book, RentalLog
from datetime import datetime

bp = Blueprint("book", __name__, url_prefix="/book")

@bp.route('/init2834283479283479283710')
def initBook():
    f = open('C:\\Users\\swamy\\OneDrive\\Desktop\\elice\\elice_library\\elice_library\\booklist.csv', encoding='UTF8')
    rdr = csv.reader(f)

    for line in rdr:
        if line[0] == ' ':continue
        rate = random.randrange(6)

        book = Book(book_name=line[1], publisher=line[2], author=line[3], publication_date=line[4], pages=line[5],
                    description=line[7], link=line[8], rating=rate, isbn=line[6])
        db.session.add(book)
        db.session.commit()

    f.close()
    return Response(status=200)

@bp.route('/')
def getAllBook():

    books = Book.query.all()
    data = []

    for book in books:

        temp = {}
        temp['id'] = book.id
        temp['book_name'] = book.book_name
        temp['author'] = book.author
        temp['publication_date'] = book.publication_date
        temp['pages'] = book.pages
        temp['link'] = book.link
        temp['rating'] = book.rating
        temp['isbn'] = book.isbn
        temp['publisher'] = book.publisher
        temp['description'] = book.description
        temp['stock'] = book.stock

        data.append(temp)

    return render_template('main/book_main.html', books=data)


@bp.route('/<int:book_id>')
def bookDetail(book_id):
    book = Book.query.get(book_id)
    return render_template('bookDetail/book_detail.html', book=book)


@bp.route('/bookRent/<int:id>', methods=('GET', 'POST'))
def bookRent(id):
    book = Book.query.get(id)
    book.stock = int(book.stock) - 1
    bookRe = RentalLog(user_id= g.user.id, book_id = id ,rental_date =datetime.now(), due_date= datetime.now())
    db.session.add(bookRe)
    db.session.commit()
    return redirect(url_for('book.bookDetail', book_id=book.id))


