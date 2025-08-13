"""
app/forms.py — 사용자가 입력하는 '폼'과 유효성 검사 규칙
- Flask-WTF(FlaskForm) + WTForms 를 사용합니다.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    # 이메일은 필수 + 이메일 형식
    email = StringField('Email', validators=[DataRequired(), Email()])
    # 비밀번호는 6~64자
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=64)])
    # 비밀번호 확인은 password 필드와 같아야 함
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
