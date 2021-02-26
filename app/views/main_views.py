from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from app import db
from app.models import Book, RentalLog


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello~!!'


@bp.route('/')
def index():
    return render_template('main/book_main.html')


@bp.route('/<int:user_id>')
def bookRent(user_id):
    rental_books = []
    books = []
    rental_log = RentalLog.query.filter(RentalLog.user_id == user_id).all()
    for each_log in rental_log:
        rental_books.append(each_log.book_id)

    for book_id2 in rental_books:
        books.append(Book.query.get(book_id2))

    return render_template('rentReturn/rentLog.html', books=books)



#
#
# @bp.route('/return/<int:user_id>/returnBook')
# def returnBook(user_id):
#     rental_books = []
#     books = []
#     rental_log = RentalLog.query.filter(RentalLog.user_id == user_id).all()
#     for each_log in rental_log:
#         rental_books.append(each_log.book_id)
#
#     for book_id2 in rental_books:
#         books.append(Book.query.get(book_id2))
#
#     return render_template('rentReturn/return.html', books=books)