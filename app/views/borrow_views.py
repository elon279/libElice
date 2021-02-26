from flask import Blueprint, request, render_template, session, Response, jsonify, g, redirect, url_for
from app import db
from app.models import Book, RentalLog
from datetime import datetime

bp = Blueprint("borrow", __name__, url_prefix="/borrow")


@bp.route('/<int:user_id>')
def borrowedBooks(user_id):
    rental_books = []
    books = []
    rental_log = RentalLog.query.filter(RentalLog.user_id == user_id).all()
    for each_log in rental_log:
        rental_books.append(each_log.book_id)

    for book_id2 in rental_books:
        books.append(Book.query.get(book_id2))

    return render_template('borrow_return/borrow_log.html', books=books, rental_log=rental_log)


@bp.route('/toReturn/<int:user_id>')
def booksToReturn(user_id):
    rental_books = []
    books = []
    rental_log = RentalLog.query.filter(RentalLog.user_id == user_id).all()
    for each_log in rental_log:
        rental_books.append(each_log.book_id)

    for book_id2 in rental_books:
        books.append(Book.query.get(book_id2))

    return render_template('borrow_return/return.html', books=books, rental_log=rental_log)


@bp.route('/<int:user_id>/<int:book_id>', methods=('GET', 'POST'))
def returnBook(book_id, user_id):
    book = Book.query.filter(Book.id == book_id).first()
    book.stock = book.stock + 1

    rental_log = RentalLog.query.filter(RentalLog.user_id == user_id, RentalLog.book_id == book_id).first()
    rental_log.due_date = datetime.now()
    db.session.commit()

    return redirect(url_for('book.book_detail', book_id=book.id))