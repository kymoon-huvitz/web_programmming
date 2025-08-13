from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# (기존) 방명록 폼
class GuestbookForm(FlaskForm):
    name = StringField("이름", validators=[DataRequired(), Length(max=50)])
    message = TextAreaField("내용", validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField("등록")

# 회원가입 폼
class RegisterForm(FlaskForm):
    username = StringField("아이디", validators=[DataRequired(), Length(min=3, max=32)])
    email = StringField("이메일(선택)", validators=[Email(), Length(max=120)])
    password = PasswordField("비밀번호", validators=[DataRequired(), Length(min=6, max=64)])
    password2 = PasswordField("비밀번호 확인", validators=[DataRequired(), EqualTo("password", "비밀번호가 일치하지 않습니다.")])
    submit = SubmitField("회원가입")

# 로그인 폼
class LoginForm(FlaskForm):
    username = StringField("아이디", validators=[DataRequired()])
    password = PasswordField("비밀번호", validators=[DataRequired()])
    remember = BooleanField("로그인 상태 유지")
    submit = SubmitField("로그인")
