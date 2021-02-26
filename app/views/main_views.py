from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from app import db


bp = Blueprint('main', __name__, url_prefix='/')



@bp.route('/')
def index():
    return render_template('main/book_main.html')


