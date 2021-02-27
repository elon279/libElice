from flask import Blueprint, request, render_template, session, Response, jsonify, g, redirect, url_for
from app import db
from app.models import Book, BorrowLog, Comment
from datetime import datetime
from app.views.auth_views import login_required


bp = Blueprint("book", __name__, url_prefix="/book")


@bp.route('/')
def getAllBook():
    books = Book.query.all()
    # comment =
    return render_template('main/book_main.html', books=books)


@bp.route('/<int:book_id>')
def bookDetail(book_id):
    book = Book.query.get(book_id)
    rating = book.rating
    return render_template('book_detail/book_detail.html', book=book, rating=rating)


@bp.route('/borrow', methods=('GET', 'POST'))
@login_required
def borrowBook():
    bookid = request.form.get("bookid")
    book = Book.query.filter(Book.id == bookid).first()
    if book.stock > 0:
        book.stock -= 1
        borrow_log = BorrowLog(user_id=g.user.id, book_id=book.id, borrow_date=datetime.now(), return_date= datetime(1001,1,1))
        db.session.add(borrow_log)
        db.session.commit()
    return redirect(url_for('book.getAllBook'))



@bp.route('/<int:book_id>/comment' , methods=('GET', 'POST'))
def rateComment(book_id):
    book = Book.query.get(book_id)
    content = request.form['content']
    rating = request.form['rating']
    comment = Comment(content=content, create_date=datetime.now(), book_id=book_id, user_id=g.user.id, rating=rating)
    book.comment_book.append(comment)

    book_comment = Comment.query.get(book_id).all()
    sum_rating = 0
    for book_comment_rating in book_comment:
        sum_rating += book_comment_rating.rating
        sum_
    book.rating = round(book.ratun)
    db.session.commit()
    return redirect(url_for('book.bookDetail', book_id=book_id ))