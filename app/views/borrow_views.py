from flask import Blueprint, request, render_template, session, Response, jsonify, g, redirect, url_for
from app import db
from app.models import Book, BorrowLog
from datetime import datetime

bp = Blueprint("borrow", __name__, url_prefix="/borrow")


@bp.route('/<int:user_id>')
def borrowedBooks(user_id):
    borrow_log = BorrowLog.query.filter(BorrowLog.user_id == user_id).all()
    return render_template('borrow_return/borrow_log.html', borrow_log=borrow_log)


@bp.route('/toReturn/<int:user_id>')
def booksToReturn(user_id):
    borrow_log = BorrowLog.query.filter(BorrowLog.user_id == user_id).all()
    return render_template('borrow_return/return.html', borrow_log=borrow_log)


@bp.route('/<int:user_id>/<int:book_id>', methods=('GET', 'POST'))
def returnBook(book_id, user_id):
    book = Book.query.filter(Book.id == book_id).first()
    book.stock += 1

    borrow_log = BorrowLog.query.filter(BorrowLog.user_id == user_id, BorrowLog.book_id == book_id).first()
    borrow_log.return_date = datetime.now()
    db.session.commit()

    return redirect(url_for('borrow.booksToReturn', user_id=user_id))
