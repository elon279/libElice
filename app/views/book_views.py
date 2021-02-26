from flask import Blueprint, request, render_template, session, Response, jsonify, g, redirect, url_for
from app import db
from app.models import Book, BorrowLog
from datetime import datetime
from app.views.auth_views import login_required

bp = Blueprint("book", __name__, url_prefix="/book")


@bp.route('/')
def getAllBook():
    books = Book.query.all()
    return render_template('main/book_main.html', books=books)


@bp.route('/<int:book_id>')
def bookDetail(book_id):
    book = Book.query.get(book_id)
    return render_template('book_detail/book_detail.html', book=book)


@bp.route('/borrow', methods=('GET', 'POST'))
@login_required
def borrowBook():
    bookid = request.form.get("bookid")
    book = Book.query.filter(Book.id == bookid).first()
    if book.stock > 0:
        book.stock = book.stock - 1
        rental_log = RentalLog(user_id=g.user.id, book_id=book.id, rental_date=datetime.now(), due_date= datetime(1001,1,1))
        db.session.add(rental_log)
        db.session.commit()
    return redirect(url_for('book.getAllBook'))
