from flask import Blueprint, request, render_template, session, Response, jsonify, g, redirect, url_for
from app import db
from app.models import Book, BorrowLog
from datetime import datetime

bp = Blueprint("borrow", __name__, url_prefix="/borrow")


@bp.route('/<int:user_id>')
def borrowedBooks(user_id):
    borrowed_books = []
    books = []
    borrow_log = BorrowLog.query.filter(BorrowLog.user_id == user_id).all()
    for each_log in borrow_log:
        borrowed_books.append(each_log.book_id)

    for book_id2 in borrowed_books:
        books.append(Book.query.get(book_id2))

    return render_template('borrow_return/borrow_log.html', books=books, borrow_log=borrow_log)


@bp.route('/toReturn/<int:user_id>')
def booksToReturn(user_id):
    borrowed_books = []
    books = []
    borrow_log = BorrowLog.query.filter(BorrowLog.user_id == user_id).all()
    for each_log in borrow_log:
        borrowed_books.append(each_log.book_id)

    for book_id2 in borrowed_books:
        books.append(Book.query.get(book_id2))

    return render_template('borrow_return/return.html', books=books, borrow_log=borrow_log)


@bp.route('/<int:user_id>/<int:book_id>', methods=('GET', 'POST'))
def returnBook(book_id, user_id):
    book = Book.query.filter(Book.id == book_id).first()
    book.stock += 1

    borrow_log = BorrowLog.query.filter(BorrowLog.user_id == user_id, BorrowLog.book_id == book_id).first()
    borrow_log.return_date = datetime.now()
    db.session.commit()

    return redirect(url_for('borrow.booksToReturn', user_id=user_id))
