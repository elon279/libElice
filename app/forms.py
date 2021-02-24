from flask_wtf import FlaskForm
# --------------------------------- [edit] ---------------------------------- #
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp
# --------------------------------------------------------------------------- #


# --------------------------------- [edit] ---------------------------------- #
class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=1, max=25, message='한글자 이상 쓰시죠'), Regexp('^[가-힣]+' , flags = 0, message = ' 한글만 입력가능합니다.')])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), Length(min=8, max=25, message= '8자리 이상 25자 이하로 정해주세요'), EqualTo('password2', '비밀번호가 일치하지 않습니다'), Regexp('(^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,25})|(^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-]).{10,25})|(^(?=.*[a-zA-Z])(?=.*[0-9]).{10,25})|(^(?=.*[!@#$%^*+=-])(?=.*[0-9]).{10,25})', flags = 0, message='영어, 숫자, 특수문자 혼용')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])


class ForeignUserCreateForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=1, max=25, message='more than one letter'), Regexp('^[A-Za-z]+' , flags = 0, message = ' only english')])
    password1 = PasswordField('password', validators=[
        DataRequired(), Length(min=8, max=25, message= 'more than 7, less than 26'), EqualTo('password2', 'password 1 and 2 are not equal')])
    password2 = PasswordField('password check', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])



class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired(), Length(min=8, max=25)])